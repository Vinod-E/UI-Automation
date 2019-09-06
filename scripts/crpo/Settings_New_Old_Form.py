import webdriver_wait
import page_elements
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class Settings(webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(Settings, self).__init__()

        self.ui_settings_icon = []
        self.ui_interview_module = []
        self.ui_new_interview_feedback_form_on = []
        self.ui_new_interview_feedback_form_off = []

    def settings_on(self):

        try:
            self.driver.implicitly_wait(5)
            self.x_path_element_webdriver_wait(page_elements.settings['settings_icon'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['settings'])
            self.xpath.click()
            self.ui_settings_icon = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.settings['Interview_module'])
            self.xpath.click()
            self.ui_interview_module = 'Pass'

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.settings['new_interview_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['on'])
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - On ------------------------"
            self.ui_new_interview_feedback_form_on = 'Pass'
            time.sleep(3)

        except exceptions.ElementNotInteractableException as error:
            print error

    def settings_off(self):

        try:
            time.sleep(5)
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
            time.sleep(2)
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - Off ------------------------"
            self.ui_new_interview_feedback_form_off = 'Pass'
            time.sleep(5)

        except exceptions.ElementNotInteractableException as error:
            print error


# Object = Settings()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.settings_on()
#     Object.settings_off()

# Object.browser_close()
