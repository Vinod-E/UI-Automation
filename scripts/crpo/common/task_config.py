import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.common import floating_action
from selenium.webdriver.common.keys import Keys


class TaskConfig(floating_action.FloatingAction):
    def __init__(self):
        super(TaskConfig, self).__init__()

    def task_config(self, configure_button, event_or_job, name,
                    assign_stage, positive_stage, negative_stage, activity):
        try:

            self.driver.refresh()
            time.sleep(4)

            self.x_path_element_webdriver_wait(configure_button)
            self.xpath.click()
            time.sleep(3)

            self.x_path_element_webdriver_wait(page_elements.job_config['new_task_row'])
            self.xpath.click()
            time.sleep(2)

            self.x_path_element_webdriver_wait(event_or_job)
            self.xpath.send_keys(name)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            time.sleep(1)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                               format('Select Stage And Status'))
            self.xpath.send_keys(assign_stage)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            time.sleep(1)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                               format('Select Positive Stage - Status'))
            self.xpath.send_keys(positive_stage)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            time.sleep(1)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                               format('Select Negative Stage - Status'))
            self.xpath.send_keys(negative_stage)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            time.sleep(2)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                               format('Select Activity'))
            self.xpath.send_keys(activity)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            time.sleep(3)

            self.x_path_element_webdriver_wait(page_elements.job_config['Task_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.job_config['select_all_task'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.buttons['done'])
            self.xpath.click()
            time.sleep(2)

            self.x_path_element_webdriver_wait(page_elements.buttons['job_task_config_save'])
            self.xpath.click()

            print('**-------->>> Task configuration done for {}'.format(name))
            time.sleep(3)

        except Exception as config_message:
            api_logger.error(config_message)
