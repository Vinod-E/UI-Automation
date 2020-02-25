import time
import page_elements
from scripts.crpo.common import settings


class ValidationCheck(settings.Settings):
    def __init__(self):
        super(ValidationCheck, self).__init__()
        self.message_validation = ''
        self.applicant_with_id = ''
        self.task_validation_check = ''

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
        self.web_element_text_xpath(page_elements.validations['task_candidate_name'])
        if candidate_name in self.text_value:
            self.task_validation_check = 'True'
            print('**-------->>> Manage task screen verified :: {}'.format(self.text_value))
        else:
            print('Wrong applicant manage task <<<---------**'.format(self.text_value))
