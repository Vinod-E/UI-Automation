import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.common import floating_action
from selenium.webdriver.common.keys import Keys


class TaskConfig(floating_action.FloatingAction):
    def __init__(self):
        super(TaskConfig, self).__init__()
        self.task_configure_success = ''

    def task_config(self, configure_button, event_or_job, name,
                    assign_stage, positive_stage, negative_stage, activity):
        try:

            self.driver.refresh()
            time.sleep(4)

            self.web_element_click_xpath(configure_button)

            self.web_element_click_xpath(page_elements.job_config['new_task_row'])

            self.web_element_send_keys_xpath(event_or_job, name)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                             format('Select Stage And Status'), assign_stage)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                             format('Select Positive Stage - Status'), positive_stage)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                             format('Select Negative Stage - Status'), negative_stage)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                             format('Select Activity'), activity)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.job_config['Task_selection'])

            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])

            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_click_xpath(page_elements.buttons['job_task_config_save'])

            print('**-------->>> Task configuration done for {}'.format(name))
            self.task_configure_success = 'Pass'
            time.sleep(1.7)

        except Exception as config_message:
            api_logger.error(config_message)
