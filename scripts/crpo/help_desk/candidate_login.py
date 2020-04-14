import time
import config
import page_elements
import image_capture
from logger_settings import ui_logger
from scripts.crpo.help_desk import set_configuration


class CandidateLogin(set_configuration.SetConfiguration):
    def __init__(self):
        super(CandidateLogin, self).__init__()

        self.candidate_login_success = ''

    def candidate_server(self):
        try:
            self.driver.get(config.sever_config['candidate'].format(self.login_server))
        except Exception as error:
            ui_logger.error(error)
    
    def login_of_candidate(self, username, password):
        try:
            time.sleep(3)
            self.candidate_server()
            self.name_element_webdriver_wait(page_elements.embrace_login['username'])
            self.name.send_keys(username)
            self.name_element_webdriver_wait(page_elements.embrace_login['password'])
            self.name.send_keys(password)
            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()

            time.sleep(3)
            image_capture.screen_shot(self, 'Candidate_login_successfully')
            self.candidate_login_validation()

        except Exception as login_failed:
            ui_logger.error(login_failed)

    def candidate_login_validation(self):
        try:
            self.web_element_text_xpath(page_elements.login['candidate_login_success'])
            if self.sprint_version in self.text_value.strip():
                self.candidate_login_success = 'True'
                print('**-------->>> Candidate login successfully')

        except Exception as error:
            ui_logger.error(error)
