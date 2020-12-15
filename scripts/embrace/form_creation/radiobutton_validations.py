from scripts.embrace.form_creation import screening_rule_creation
from logger_settings import ui_logger

class RadiobuttonValidations(screening_rule_creation.screening_rule_input):
    def __init__(self):
        super(RadiobuttonValidations, self).__init__()
        self.ui_radiobutton = ''
        self.radiobutton_value = []

    def radiobutton_validation(self):
        try:
            self.web_element_text_xpath('/html/body/div[2]/div/section/div/div/div/div/div/div/div[2]/div[1]/div[4]/'
                                        'div[2]/div/div[2]/div/form-preview/div[2]/form/div[2]/div[3]/div/div/div/label[1]')

            if self.text_value == 'male':
                self.radiobutton_value.append(self.text_value)
                print('radiobutton is male')

            self.web_element_text_xpath('/html/body/div[2]/div/section/div/div/div/div/div/div/div[2]/div[1]/div[4]/div'
                                        '[2]/div/div[2]/div/form-preview/div[2]/form/div[2]/div[3]/div/div/div/label[2]')
            if self.text_value == 'female':
                self.radiobutton_value.append(self.text_value)
                print('radiobutton is female')
                self.ui_radiobutton = 'Pass'
            self.list_of_radiobutton = ', '.join(self.radiobutton_value)

        except Exception as error:
            ui_logger.error(error)