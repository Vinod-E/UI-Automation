import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.help_desk import query_configuration
from scripts.crpo.common import button_click


class SetConfiguration(query_configuration.QueryConfig):
    def __init__(self):
        super(SetConfiguration, self).__init__()

        self.ui_default_config = ''
        self.ui_job_config = ''
        self.ui_event_config = ''

    def default_configuration(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.help_desk['category'])
            self.multi_selection_search(self.xl_category_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['user'])
            self.multi_selection_search(self.xl_user_1)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_send_keys_xpath(page_elements.help_desk['sla'], self.xl_sla_1)
            button_click.button(self, 'Save')
            time.sleep(0.5)

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_default_config = 'Pass'
                self.dismiss_message()
                time.sleep(1.5)

        except Exception as error:
            ui_logger.error(error)

    def job_configuration(self):
        try:
            self.web_element_click_xpath(page_elements.help_desk['category'])
            self.multi_selection_search(self.xl_category_2)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['job'])
            self.multi_selection_search(self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['job_users'])
            self.multi_selection_search(self.xl_user_2)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_send_keys_xpath(page_elements.help_desk['job_sla'], self.xl_sla_2)
            button_click.button(self, 'Save')

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_job_config = 'Pass'
                self.dismiss_message()
                time.sleep(1.5)

        except Exception as error:
            ui_logger.error(error)

    def event_configuration(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.help_desk['category'])
            self.multi_selection_search(self.xl_category_3)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['event_job'])
            self.multi_selection_search(self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['event'])
            self.multi_selection_search(self.requirement_sprint_version)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.help_desk['event_users'])
            self.multi_selection_search(self.xl_user_3)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_send_keys_xpath(page_elements.help_desk['event_sla'], self.xl_sla_3)
            button_click.button(self, 'Save')

# validation ----
            self.glowing_messages('Configuration saved successfully')
            if self.message_validation == 'True':
                self.ui_event_config = 'Pass'
                self.dismiss_message()
                time.sleep(1.5)

        except Exception as error:
            ui_logger.error(error)
