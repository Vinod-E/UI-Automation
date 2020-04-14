import page_elements
from logger_settings import ui_logger
from scripts.crpo.help_desk import query_configuration


class SetConfiguration(query_configuration.QueryConfig):
    def __init__(self):
        super(SetConfiguration, self).__init__()

        self.ui_default_config = ''
        self.ui_job_config = ''
        self.ui_event_config = ''

    def default_configuration(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.help_desk['default_category'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_category_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['user'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_user_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.help_desk['sla'], self.xl_sla_1)
            self.web_element_click_xpath(page_elements.buttons['query_save'])

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_default_config = 'Pass'
                self.dismiss_message()

        except Exception as error:
            ui_logger.error(error)

    def job_configuration(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.help_desk['job_category'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_category_2)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['job_job'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['job_users'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_user_2)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.help_desk['job_sla'].format(1), self.xl_sla_2)
            self.web_element_click_xpath(page_elements.buttons['query_save'])

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_job_config = 'Pass'
                self.dismiss_message()

        except Exception as error:
            ui_logger.error(error)

    def event_configuration(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.help_desk['event_category'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_category_3)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['event_job'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['event_event'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.help_desk['event_users'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_user_3)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.help_desk['event_sla'].format(1), self.xl_sla_3)
            self.web_element_click_xpath(page_elements.buttons['query_save'])

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_event_config = 'Pass'
                self.dismiss_message()

        except Exception as error:
            ui_logger.error(error)
