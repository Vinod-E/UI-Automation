import page_elements
from logger_settings import api_logger
from scripts.crpo.common import login


class Settings(login.Login):
    def __init__(self):
        super(Settings, self).__init__()

        self.enable_disable_validation = ''

    def settings(self, module):
        try:
            self.x_path_element_webdriver_wait(page_elements.login['login_success'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.setting_modules['settings'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(module)
            self.xpath.click()

        except Exception as setting_error:
            api_logger.error(setting_error)

    def enable_new_feedback_form(self, on_or_off, enable_disable):
        try:
            self.driver.execute_script("window.scrollTo(0,200);")
            self.x_path_element_webdriver_wait(page_elements.setting_modules['enable_new_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(on_or_off)
            self.xpath.click()
            print('**-------->>> {} new feedback form'.format(enable_disable))
            self.enable_disable_validation = 'True'
        except Exception as interview_module_error:
            api_logger.error(interview_module_error)
