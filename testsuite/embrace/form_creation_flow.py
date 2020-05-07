from logger_settings import ui_logger
from scripts.embrace.output import form_creation_output
import time


class FormCreationFlow(form_creation_output.FormOutputReport):
    def __init__(self):
        super(FormCreationFlow, self).__init__()

    def form(self):
        self.create_form()
        self.field_validation()
        self.create_form_field_output()

        self.label_validation()
        self.create_form_label_output()

        self.group_validation()
        self.create_form_group_output()

        self.college_catalogs()
        self.create_form_dropdown_output()

        self.checkbox_validation()
        self.create_form_checkbox_output()

        self.radiobutton_validation()
        self.create_form_radiobutton_output()


Object = FormCreationFlow()
Object.embrace_login()
if Object.status_of_login.strip() == 'Admin':
    try:
        Object.form()
        Object.overall_status()
        Object.browser_close()
    except Exception as usecase:
        ui_logger.error(usecase)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
