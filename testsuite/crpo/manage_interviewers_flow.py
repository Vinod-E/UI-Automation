from logger_settings import api_logger
from scripts.crpo.output import manage_interviewers_output


class ManageInterviewFlow(manage_interviewers_output.ManageInterviewersOutput):
    def __init__(self):
        super(ManageInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def event_interviewers_configuration(self):
        try:
            self.event_search()
            self.admin_config_output()

        except Exception as error:
            api_logger.error(error)


Object = ManageInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.event_interviewers_configuration()

        Object.overall_status()
        # Object.browser_close()

    except Exception as flow_error:
        api_logger.error(flow_error)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        api_logger.error(flow_error)
