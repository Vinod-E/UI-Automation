from logger_settings import ui_logger
from scripts.crpo.output import manage_interviewers_output
import time


class ManageInterviewFlow(manage_interviewers_output.ManageInterviewersOutput):
    def __init__(self):
        super(ManageInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def event_interviewers_configuration(self):
        try:
            self.event_search()
            self.admin_config_output()

            self.invite_interviewers_config()
            time.sleep(2)
            self.invite_int_config_output()

            self.skill1_filter()
            self.skill2_filter()
            self.manage_interviewers_output()

        except Exception as error:
            ui_logger.error(error)

    def nomination_acceptance(self):
        try:
            self.nomination_int1()
            self.acceptance_int1_output()

            self.nomination_int2()
            self.acceptance_int2_output()

        except Exception as error:
            ui_logger.error(error)

    def manager_approve(self):
        try:
            self.em_approve()
            self.em_skill1_filter()
            self.em_skill2_filter()
            self.approve_sync()
            self.event_manager_output()

        except Exception as error:
            ui_logger.error(error)


Object = ManageInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.event_interviewers_configuration()
        Object.nomination_acceptance()
        Object.manager_approve()

        Object.overall_status()
        # Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
