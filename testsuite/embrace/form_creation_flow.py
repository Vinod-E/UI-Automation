from logger_settings import api_logger
from scripts.embrace.output import form_creation_output


class FormCreationFlow(form_creation_output.FormOutputReport):
    def __init__(self):
        super(FormCreationFlow, self).__init__()

    def form(self):
        self.create_form()
        self.validation()

        self.create_form_output()


Object = FormCreationFlow()
Object.embrace_login()
if Object.status_of_login.strip() == 'Admin':
    try:
        Object.form()
        Object.overall_status()

        Object.browser_close()
    except Exception as usecase:
        api_logger.error(usecase)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        api_logger.error(flow_error)
