from scripts.embrace.form_creation import catalog_validations
from logger_settings import api_logger

class CheckboxValidations(catalog_validations.CatalogValidations):
    def __init__(self):
        super(CheckboxValidations, self).__init__()
        self.ui_checkbox = ''
        self.checkbox_value = []


    def checkbox_validation(self):
        try:
            self.web_element_text_xpath('/html/body/div[2]/div/section/div/div/div/div/div/div/div[2]/div[1]/div[4]/div[2]/div/div[2]'
                                        '/div/form-preview/div[2]/form/div[1]/div[5]/div/div/div/label[1]')

            if self.text_value == 'india':
                self.checkbox_value.append(self.text_value)
                print('checkbox is india')

            self.web_element_text_xpath('/html/body/div[2]/div/section/div/div/div/div/div/div/div[2]/div[1]/div[4]/div'
                                        '[2]/div/div[2]/div/form-preview/div[2]/form/div[1]/div[5]/div/div/div/label[2]')
            if self.text_value == 'pakistan':
                self.checkbox_value.append(self.text_value)
                print('checkbox is pakistan')
                self.ui_checkbox = 'Pass'
            self.list_of_checkbox = ', '.join(self.checkbox_value)


        except Exception as error:
            api_logger.error(error)

