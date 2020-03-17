import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.help_desk import query_configuration


class SetConfiguration(query_configuration.QueryConfig):
    def __init__(self):
        super(SetConfiguration, self).__init__()

    def default_configuration(self):
        try:
            self.web_element_click_xpath(page_elements.requirement['default_category'].format(1))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_category_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.requirement['user'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_user_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.requirement['sla'], self.xl_sla_1)

        except Exception as error:
            api_logger.error(error)

    def event_configuration(self):
        try:
            self.web_element_click_xpath(page_elements.requirement['default_category'].format(1))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_category_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.requirement['user'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.xl_user_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.requirement['sla'].format(1), self.xl_sla_1)

        except Exception as error:
            api_logger.error(error)

    def job_configuration(self):
        try:
            pass
        except Exception as error:
            api_logger.error(error)
