from logger_settings import ui_logger
from scripts.crpo.output import help_desk_output


class HelpDeskFlow(help_desk_output.HelpDeskOutput):
    def __init__(self):
        self.user_name_of_candidate = input("Candidate Email ID :: ")
        self.password_of_candidate = input("Candidate Password :: ")
        super(HelpDeskFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def help_desk_configuration(self):
        try:
            self.query_configuration()
            self.default_configuration()
            self.job_configuration()
            self.event_configuration()
            self.admin_config_output()

        except Exception as error:
            ui_logger.error(error)

    def candidate_login(self):
        try:
            self.login_of_candidate(self.user_name_of_candidate, self.password_of_candidate)
            self.raise_query()
            self.candidate_raise_query_output()

        except Exception as error:
            ui_logger.error(error)

    def staffing_login(self):
        try:
            self.default_config_reply()
            self.default_level_output()

            self.job_config_reply()
            self.job_level_output()

            self.event_config_reply()
            self.event_level_output()

        except Exception as error:
            ui_logger.error(error)


Object = HelpDeskFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.help_desk_configuration()
        Object.candidate_login()
        Object.staffing_login()

        Object.overall_status()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
