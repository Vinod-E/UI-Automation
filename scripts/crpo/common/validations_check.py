import time
import page_elements
from scripts.crpo.common import (settings, applicant_actions)


class ValidationCheck(settings.Settings):
    def __init__(self):
        super(ValidationCheck, self).__init__()
        self.message_validation = ''
        self.applicant_with_id = ''
        self.task_validation_check = ''
        self.enable_link_validation_check = ''
        self.disable_link_validation_check = ''

    def glowing_messages(self, message):
        self.web_element_text_xpath(page_elements.glowing_messages['notifier'])
        if self.text_value == message:
            self.message_validation = 'True'
            print('**-------->>> Message/UI notifier validated successfully - {}'.format(message))
        else:
            print('Message/UI notifier validation failed - {} <<<---------**'.format(self.text_value))

    def dismiss_message(self):
        self.web_element_click_xpath(page_elements.glowing_messages['dismiss'])

    def manage_task_validation(self, candidate_name):
        time.sleep(2.5)
        self.web_element_text_xpath(page_elements.validations['task_candidate_name'])
        if candidate_name in self.text_value:
            self.task_validation_check = 'True'
            print('**-------->>> Manage task screen verified :: {}'.format(self.text_value))
        else:
            print('Wrong applicant manage task <<<---------**'.format(self.text_value))

    def enable_link_validation(self, event_name):
        # ----------------------------- View Registration Link ----------------------------
        applicant_actions.action(self, 'View Registration Link')
        # ----------------------------- link ---------------------
        self.web_element_click_xpath(page_elements.event_applicant['open_RL_new_tab'])
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.web_element_text_xpath(page_elements.microSite['micro_site_campus_details'])
        if self.text_value == event_name:
            self.enable_link_validation_check = 'True'
            print('**-------->>> link is validated by event name :: {}'.format(self.text_value))
        else:
            print('Something else is wrong with the link <<<---------**')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.web_element_click_xpath(page_elements.buttons['done'])
        time.sleep(2)

    def disable_link_validation(self):
        # ----------------------------- View Registration Link ----------------------------
        applicant_actions.action(self, 'View Registration Link')
        # ----------------------------- link ---------------------
        self.web_element_click_xpath(page_elements.event_applicant['open_RL_new_tab'])
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.web_element_text_xpath(page_elements.microSite['micro_site_page_closed'])
        if self.text_value.strip() == "Registration Closed/Expired":
            self.disable_link_validation_check = 'True'
            print('**-------->>> link is validated by 404 page :: {}'.format("Registration Closed/Expired"))
        else:
            print('Something else is wrong with the link <<<---------**')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.web_element_click_xpath(page_elements.buttons['done'])
        time.sleep(2)
