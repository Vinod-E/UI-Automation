from scripts.embrace.output import form_creation_output


class FormCreationFlow(form_creation_output.FormOutputReport):
    def __init__(self):
        super(FormCreationFlow, self).__init__()

    def form(self):
        self.create_form()
        self.validation()


Object = FormCreationFlow()
Object.form()
Object.overall_status()
