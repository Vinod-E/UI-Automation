from logger_settings import api_logger
from scripts.crpo.output import help_desk_output


class HelpDeskFlow(help_desk_output.HelpDeskOutput):
    def __init__(self):
        super(HelpDeskFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def help_desk_configuration(self):
        try:
            self.query_configuration()
            self.default_configuration()
            self.event_configuration()

        except Exception as error:
            api_logger.error(error)


Object = HelpDeskFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.help_desk_configuration()

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
