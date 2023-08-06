# ############################################################################### #
# Autoreduction Repository : https://github.com/ISISScientificComputing/autoreduce
#
# Copyright &copy; 2019 ISIS Rutherford Appleton Laboratory UKRI
# SPDX - License - Identifier: GPL-3.0-or-later
# ############################################################################### #
"""
Utility functions for the reduction viewer models

Note: This file has a large number of pylint disable as it was un unit tested
at the time of fixing the pylint issues. Once unit tested properly, these disables
should be able to be removed. Many are relating to imports
"""
import time

from autoreduce_db.reduction_viewer.models import ReductionRun
from autoreduce_utils.message.message import Message
from autoreduce_utils.clients.queue_client import QueueClient

from autoreduce_frontend.autoreduce_webapp.settings import FACILITY


class ReductionRunUtils:
    """
    Utilities for the ReductionRun model
    """
    @staticmethod
    def make_kwargs_from_runvariables(reduction_run, use_value=False) -> dict:
        """
        Given a reduction run and optionally use_value create a kwarg dict from its variables
        :param reduction_run: The ReductionRun
        :param use_value: Flag whether to use the variable values
        :return: kwarg dict of the variables
        """
        if reduction_run.run_variables.count() == 0:
            return {"standard_vars": {}, "advanced_vars": {}}

        return ReductionRunUtils.make_kwargs_from_variables(
            [runvar.variable for runvar in reduction_run.run_variables.all()], use_value)

    @staticmethod
    def make_kwargs_from_variables(variables, use_value=False) -> dict:
        """
        Given a list of variables, create a kwarg dict of the variables
        :param variables: The variables to make into a kwarg dict
        :param use_value: Flag whether to use the variable values
        :return: Kwarg dict of variables
        """
        standard_vars = {}
        advanced_vars = {}

        for variable in variables:
            if variable.is_advanced:
                advanced_vars[variable.name] = variable.value if use_value else variable
            else:
                standard_vars[variable.name] = variable.value if use_value else variable

        return {"standard_vars": standard_vars, "advanced_vars": advanced_vars}

    @staticmethod
    def send_retry_message(user_id: int, most_recent_run: ReductionRun, run_description: str, script_text: str,
                           new_script_arguments: dict, overwrite_previous_data: bool) -> None:
        """
        Creates & sends a retry message given the parameters

        :param user_id: The user submitting the run
        :param most_recent_run: The most recent run, used for common things across the two runs like
                                run number, instrument name, etc
        :param run_description: Description of the rerun
        :param script_text: The script that will NOT be used for this reduction, because of a known issue
                            https://github.com/ISISScientificComputing/autoreduce/issues/1115
        :param new_script_arguments: Dict of arguments that will be used for the reduction
        :param overwrite_previous_data: Whether to overwrite the previous data in the data location
        """
        message = Message(started_by=user_id,
                          description=run_description,
                          run_number=most_recent_run.run_number,
                          instrument=most_recent_run.instrument.name,
                          rb_number=most_recent_run.experiment.reference_number,
                          data=most_recent_run.data_location.first().file_path,
                          reduction_script=script_text,
                          reduction_arguments=new_script_arguments,
                          run_version=most_recent_run.run_version,
                          facility=FACILITY,
                          software=str(most_recent_run.software),
                          overwrite=overwrite_previous_data)
        MessagingUtils.send(message)

    @staticmethod
    def send_retry_message_same_args(user_id: int, most_recent_run: ReductionRun):
        """
        Sends a retry message using the parameters from the most_recent_run
        """
        ReductionRunUtils.send_retry_message(
            user_id, most_recent_run, "Re-run from the failed queue", most_recent_run.script,
            ReductionRunUtils.make_kwargs_from_runvariables(most_recent_run, use_value=True), most_recent_run.overwrite)


class ScriptUtils:
    """
    Utilities for the scripts field
    """
    @staticmethod
    def get_reduce_scripts(scripts):
        """
        Returns a tuple of (reduction script, reduction vars script),
        each one a string of the contents of the script, given a list of script objects.
        """
        script_out = None
        script_vars_out = None
        for script in scripts:
            if script.file_name == "reduce.py":
                script_out = script
            elif script.file_name == "reduce_vars.py":
                script_vars_out = script
        return script_out, script_vars_out

    def get_cache_scripts_modified(self, scripts):
        """
        :returns: The last time the scripts in the database were
        modified (in seconds since epoch).
        """
        script_modified = None
        script_vars_modified = None

        for script in scripts:
            if script.file_name == "reduce.py":
                script_modified = self._convert_time_from_string(str(script.created))
            elif script.file_name == "reduce_vars.py":
                script_vars_modified = self._convert_time_from_string(str(script.created))
        return script_modified, script_vars_modified

    @staticmethod
    def _convert_time_from_string(string_time):
        """
        :return: time as integer for epoch
        """
        time_format = "%Y-%m-%d %H:%M:%S"
        string_time = string_time[:string_time.find('+')]
        return int(time.mktime(time.strptime(string_time, time_format)))


class MessagingUtils:
    """
    Utilities for sending messages to ActiveMQ
    """
    @staticmethod
    def send(message):
        """ Sends message to ReductionPending (with the specified delay) """
        message_client = QueueClient()
        message_client.connect()

        message_client.send('/queue/DataReady', message, priority='1')
        message_client.disconnect()
