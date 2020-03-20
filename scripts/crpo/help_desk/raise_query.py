import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.help_desk import candidate_login


class RaiseQuery(candidate_login.CandidateLogin):
    def __init__(self):
        super(RaiseQuery, self).__init__()

        self.file = test_data_inputpath.attachments['query']
        self.message = 'Your request has been sent successfully. We will try to resolve the issue asap'

        self.ui_candidate_login_success = []
        self.ui_help_desk_module = []
        self.ui_raise_query_module = []
        self.ui_default_raise_query = []
        self.ui_job_raise_query = []
        self.ui_event_raise_query = []

    def help_desk_tab(self):
        try:
            if self.candidate_login_success == 'True':
                self.web_element_click_xpath(page_elements.tabs['help_desk_tab'])
                self.web_element_click_xpath(page_elements.tabs['raise_query_tab'])

                self.ui_candidate_login_success = 'Pass'
                self.ui_help_desk_module = 'Pass'
                self.ui_raise_query_module = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def raise_query_elements(self, category):
        try:
            self.web_element_click_xpath(page_elements.help_desk['query_choose'])
            self.web_element_send_keys_xpath(page_elements.help_desk['query_choose'], category)
            self.xpath_send_keys.send_keys(Keys.ENTER)
            self.web_element_send_keys_name(page_elements.help_desk['subject'], category)
            self.web_element_send_keys_xpath(page_elements.help_desk['message'], category)
            self.web_element_send_keys_xpath(page_elements.file['upload_file'], self.file)
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['query_raise'])

        except Exception as error:
            api_logger.error(error)

    def raise_query(self):
        try:
            time.sleep(1)
            self.help_desk_tab()
            self.raise_query_elements(self.category_1)
            self.glowing_messages(self.message)
            self.dismiss_message()
            if self.message_validation == 'True':
                self.ui_default_raise_query = 'Pass'

            time.sleep(1.5)
            self.raise_query_elements(self.category_2)
            self.glowing_messages(self.message)
            self.dismiss_message()
            if self.message_validation == 'True':
                self.ui_job_raise_query = 'Pass'

            time.sleep(1.5)
            self.raise_query_elements(self.category_3)
            self.glowing_messages(self.message)
            self.dismiss_message()
            if self.message_validation == 'True':
                self.ui_event_raise_query = 'Pass'

        except Exception as error:
            api_logger.error(error)
