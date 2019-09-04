import provide_feedback
import page_elements
import time
from selenium.common import exceptions


class Settings(provide_feedback.OldProvideFeedback):
    def __init__(self):
        super(Settings, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

    def settings_on(self):

        try:
            self.driver.implicitly_wait(5)
            self.x_path_element_webdriver_wait(page_elements.settings['settings_icon'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['settings'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['Interview_module'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.settings['new_interview_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['on'])
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - On ------------------------"

        except exceptions.ElementNotInteractableException as error:
            print error

    def settings_off(self):

        try:
            self.driver.implicitly_wait(5)
            self.x_path_element_webdriver_wait(page_elements.settings['settings_icon'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['settings'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['Interview_module'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.settings['new_interview_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['off'])
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - Off ------------------------"

        except exceptions.ElementNotInteractableException as error:
            print error


# Object = Settings()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.settings_on()
#     Object.settings_off()

# Object.browser_close()
