# ############################################################################### #
# Autoreduction Repository : https://github.com/ISISScientificComputing/autoreduce
#
# Copyright &copy; 2021 ISIS Rutherford Appleton Laboratory UKRI
# SPDX - License - Identifier: GPL-3.0-or-later
# ############################################################################### #
"""
View functions for displaying Variable data
This imports into another view, thus no middleware
"""
import logging
import os

from django.shortcuts import redirect, render
from autoreduce_db.instrument.models import InstrumentVariable
from autoreduce_db.reduction_viewer.models import Instrument, ReductionRun
from autoreduce_qp.queue_processor.variable_utils import VariableUtils

from autoreduce_frontend.autoreduce_webapp.view_utils import (check_permissions, login_and_uows_valid, render_with)
from autoreduce_frontend.reduction_viewer.utils import ReductionRunUtils

LOGGER = logging.getLogger(__package__)


# pylint:disable=too-many-locals
def summarize_variables(request, instrument, last_run_object):
    """
    Handles view request for the instrument summary page
    """
    # pylint:disable=no-member
    instrument = Instrument.objects.get(name=instrument)

    # pylint:disable=invalid-name
    current_variables = [runvar.variable.instrumentvariable for runvar in last_run_object.run_variables.all()]

    upcoming_variables_by_run = InstrumentVariable.objects.filter(start_run__gt=last_run_object.run_number,
                                                                  instrument=instrument)
    upcoming_variables_by_experiment = InstrumentVariable.objects.filter(
        experiment_reference__gte=last_run_object.experiment.reference_number, instrument=instrument)

    # There's a known issue with inaccurate display of tracks script:
    # https://github.com/ISISScientificComputing/autoreduce/issues/1187
    # Creates a nested dictionary for by-run
    upcoming_variables_by_run_dict = {}
    for variable in upcoming_variables_by_run:
        if variable.start_run not in upcoming_variables_by_run_dict:
            upcoming_variables_by_run_dict[variable.start_run] = {
                'run_start': variable.start_run,
                'run_end': 0,  # We'll fill this in after
                'tracks_script': variable.tracks_script,
                'variables': [],
                'instrument': instrument,
            }
        upcoming_variables_by_run_dict[variable.start_run]['variables'].append(variable)

    # Fill in the run end numbers
    run_end = 0
    for run_number in sorted(upcoming_variables_by_run_dict.keys(), reverse=True):
        upcoming_variables_by_run_dict[run_number]['run_end'] = run_end
        run_end = max(run_number - 1, 0)

    if current_variables:
        current_start = current_variables[0].start_run
        next_run_starts = list(
            filter(lambda start: start > current_start, sorted(upcoming_variables_by_run_dict.keys())))
        current_end = next_run_starts[0] - 1 if next_run_starts else 0

        current_vars = {
            'run_start': current_start,
            'run_end': current_end,
            'tracks_script': not any((var.tracks_script for var in current_variables)),
            'variables': current_variables,
            'instrument': instrument,
        }
    else:
        current_vars = {}

    # Move the upcoming vars into an ordered list
    upcoming_variables_by_run_ordered = []
    for key in sorted(upcoming_variables_by_run_dict):
        upcoming_variables_by_run_ordered.append(upcoming_variables_by_run_dict[key])

    # Create a nested dictionary for by-experiment
    upcoming_variables_by_experiment_dict = {}
    for variables in upcoming_variables_by_experiment:
        if variables.experiment_reference not in upcoming_variables_by_experiment_dict:
            upcoming_variables_by_experiment_dict[variables.experiment_reference] = {
                'experiment': variables.experiment_reference,
                'variables': [],
                'instrument': instrument,
            }
        upcoming_variables_by_experiment_dict[variables.experiment_reference]['variables'].\
            append(variables)

    # Move the upcoming vars into an ordered list
    upcoming_variables_by_experiment_ordered = []
    for key in sorted(upcoming_variables_by_experiment_dict):
        upcoming_variables_by_experiment_ordered.append(upcoming_variables_by_experiment_dict[key])
    sorted(upcoming_variables_by_experiment_ordered, key=lambda r: r['experiment'])

    context_dictionary = {
        'instrument': instrument,
        'current_variables': current_vars,
        'upcoming_variables_by_run': upcoming_variables_by_run_ordered,
        'upcoming_variables_by_experiment': upcoming_variables_by_experiment_ordered,
    }

    return render(request, 'snippets/instrument_summary_variables.html', context_dictionary)


# pylint:disable=unused-argument
@login_and_uows_valid
@check_permissions
def delete_instrument_variables(request, instrument=None, start=0, end=0, experiment_reference=None):
    """
    Handles request for deleting instrument variables

    :param instrument: Name of the instrument for which variables are being deleted
    :param start: The start run from which variables are being deleted
    :param end: Used to limit how many variables get deleted, otherwise a delete would wipe ALL variables > start
    :param experiment_reference: If provided - use the experiment reference to delete variables instead of start_run
    """

    # We "save" an empty list to delete the previous variables.
    if experiment_reference is not None:
        InstrumentVariable.objects.filter(instrument__name=instrument,
                                          experiment_reference=experiment_reference).delete()
    else:
        start_run_kwargs = {"start_run__gte": start}
        if end > 0:
            start_run_kwargs["start_run__lte"] = end
        InstrumentVariable.objects.filter(instrument__name=instrument, **start_run_kwargs).delete()

    return redirect('instrument:variables_summary', instrument=instrument)


@login_and_uows_valid
@check_permissions
@render_with('variables_summary.html')
# pylint:disable=no-member
def instrument_variables_summary(request, instrument):
    """
    Handles request to view instrument variables
    """
    instrument = Instrument.objects.get(name=instrument)
    context_dictionary = {'instrument': instrument, 'last_instrument_run': instrument.reduction_runs.last()}
    return context_dictionary


@login_and_uows_valid
@check_permissions
@render_with('snippets/variables/form.html')
def current_default_variables(request, instrument=None):
    """
    Handles request to view default variables
    """

    try:
        current_variables = VariableUtils.get_default_variables(instrument)
    except (FileNotFoundError, ImportError, SyntaxError) as err:
        return {"message": str(err)}
    standard_vars = current_variables["standard_vars"]
    advanced_vars = current_variables["advanced_vars"]

    context_dictionary = {
        'instrument': instrument,
        'standard_variables': standard_vars,
        'advanced_variables': advanced_vars,
    }
    return context_dictionary


def render_run_variables(request, instrument_name, run_number, run_version=0):
    """
    Handles request to view the summary of a run
    """
    # pylint:disable=no-member
    reduction_run = ReductionRun.objects.get(instrument__name=instrument_name,
                                             run_number=run_number,
                                             run_version=run_version)

    vars_kwargs = ReductionRunUtils.make_kwargs_from_runvariables(reduction_run)
    standard_vars = vars_kwargs["standard_vars"]
    advanced_vars = vars_kwargs["advanced_vars"]

    try:
        default_variables = VariableUtils.get_default_variables(instrument_name)
        default_standard_variables = default_variables["standard_vars"]
        default_advanced_variables = default_variables["advanced_vars"]
    except (FileNotFoundError, ImportError, SyntaxError):
        default_standard_variables = {}
        default_advanced_variables = {}

    final_standard = _combine_dicts(standard_vars, default_standard_variables)
    final_advanced = _combine_dicts(advanced_vars, default_advanced_variables)

    context_dictionary = {
        'run_number': run_number,
        'run_version': run_version,
        'standard_variables': final_standard,
        'advanced_variables': final_advanced,
        'instrument': reduction_run.instrument,
    }
    return render(request, 'snippets/run_variables.html', context_dictionary)


def _combine_dicts(current: dict, default: dict):
    """
    Combines the current and default variable dictionaries, into a single dictionary
    which can be more easily rendered into the webapp.

    If no current variables are provided, it returns the default as both current and default.
    """
    if not current:
        current = default.copy()

    final = {}
    for name, var in current.items():
        final[name] = {"current": var, "default": default.get(name, None)}
    return final
