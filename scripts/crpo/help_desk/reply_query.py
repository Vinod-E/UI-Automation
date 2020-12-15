import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.help_desk import raise_query
from scripts.crpo.common import button_click


class RaiseQuery(raise_query.RaiseQuery):
    def __init__(self):
        super(RaiseQuery, self).__init__()

        self.ui_helpdesk_user1 = ''
        self.ui_query_choosen_1 = ''
        self.ui_query_reply_1 = ''
        self.ui_inprogress_query_choosen_1 = ''
        self.ui_inprogress_query_reply_1 = ''
        self.ui_query_close_1 = ''

        self.ui_helpdesk_user2 = ''
        self.ui_query_choosen_2 = ''
        self.ui_query_reply_2 = ''
        self.ui_inprogress_query_choosen_2 = ''
        self.ui_inprogress_query_reply_2 = ''
        self.ui_query_close_2 = ''

        self.ui_helpdesk_user3 = ''
        self.ui_query_choosen_3 = ''
        self.ui_query_reply_3 = ''
        self.ui_inprogress_query_choosen_3 = ''
        self.ui_inprogress_query_reply_3 = ''
        self.ui_query_close_3 = ''

    def default_config_reply(self):
        try:
            self.staff_login(self.xl_login_1, self.xl_password_he, self.user_1)
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_1))
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_1)
            self.web_element_click_xpath(page_elements.title['title'].format('Reply'))

# ------ In progress module
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.help_desk['open/inprogress/close'], 'In Progress')
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_1))
            self.web_element_text_xpath(page_elements.title['title'].format(self.category_1))  # ------ text
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_1)
            button_click.button(self, 'Mark as Closed')
            button_click.button(self, 'OK')
            time.sleep(1)

# ------ Validation
            if self.staff_logging == 'True':
                self.ui_helpdesk_user1 = 'Pass'

            if self.text_value == self.category_1:
                self.ui_query_choosen_1 = 'Pass'
                self.ui_query_reply_1 = 'Pass'
                self.ui_inprogress_query_choosen_1 = 'Pass'
                self.ui_inprogress_query_reply_1 = 'Pass'

            time.sleep(2)
            self.web_element_text_xpath(page_elements.help_desk['total_records'])
            if '0' in self.text_value:
                self.ui_query_close_1 = 'Pass'

        except Exception as default:
            ui_logger.error(default)

    def job_config_reply(self):
        try:
            self.staff_login(self.xl_login_2, self.xl_password_he, self.user_2)
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_2))
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_2)
            self.web_element_click_xpath(page_elements.title['title'].format('Reply'))

            # ------ In progress module
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.help_desk['open/inprogress/close'], 'In Progress')
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_2))
            self.web_element_text_xpath(page_elements.title['title'].format(self.category_2))  # ------ text
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_2)
            button_click.button(self, 'Mark as Closed')
            button_click.button(self, 'OK')
            time.sleep(2)

# ------ Validation
            if self.staff_logging == 'True':
                self.ui_helpdesk_user2 = 'Pass'

            if self.text_value == self.category_2:
                self.ui_query_choosen_2 = 'Pass'
                self.ui_query_reply_2 = 'Pass'
                self.ui_inprogress_query_choosen_2 = 'Pass'
                self.ui_inprogress_query_reply_2 = 'Pass'

            time.sleep(2)
            self.web_element_text_xpath(page_elements.help_desk['total_records'])
            if '0' in self.text_value:
                self.ui_query_close_2 = 'Pass'

        except Exception as job:
            ui_logger.error(job)

    def event_config_reply(self):
        try:
            self.staff_login(self.xl_login_3, self.xl_password_he, self.user_3)
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_3))
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_3)
            self.web_element_click_xpath(page_elements.title['title'].format('Reply'))

            # ------ In progress module
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.help_desk['open/inprogress/close'], 'In Progress')
            self.web_element_click_xpath(page_elements.title['title'].format(self.category_3))
            self.web_element_text_xpath(page_elements.title['title'].format(self.category_3))  # ------ text
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Your message here...'),
                                             self.category_3)
            button_click.button(self, 'Mark as Closed')
            button_click.button(self, 'OK')
            time.sleep(2)

# ------ Validation
            if self.staff_logging == 'True':
                self.ui_helpdesk_user3 = 'Pass'

            if self.text_value == self.category_3:
                self.ui_query_choosen_3 = 'Pass'
                self.ui_query_reply_3 = 'Pass'
                self.ui_inprogress_query_choosen_3 = 'Pass'
                self.ui_inprogress_query_reply_3 = 'Pass'

            time.sleep(2)
            self.web_element_text_xpath(page_elements.help_desk['total_records'])
            if '0' in self.text_value:
                self.ui_query_close_3 = 'Pass'

        except Exception as event:
            ui_logger.error(event)
