import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.event import create_event
from selenium.webdriver.common.keys import Keys


class TestTaskConfig(create_event.CreateEvent):
    def __init__(self):
        super(TestTaskConfig, self).__init__()

        self.activity_name = ''

        self.ui_event_config_tab = []
        self.ui_event_task_config = []
        self.task_validation = []
        self.ui_event_test_config = []
        self.test_validation = []

    def event_test_task_configure(self):

        self.event_validation('task and test configuration')
        if self.validation_check == 'True':

            try:
                self.x_path_element_webdriver_wait(page_elements.tabs['event_configuration_tab'])
                self.xpath.click()
                self.ui_event_config_tab = 'Pass'
                # ---------------------- Task configuration ------------------------------------------------------------
                self.task_config(page_elements.task_config['event_task_configure'],
                                 page_elements.text_fields['text_field'].format('Select Job Role'),
                                 self.event_sprint_version,
                                 self.xl_stage_status,
                                 self.xl_positive_stage_status_Event,
                                 self.xl_negative_stage_status_job,
                                 self.xl_activity)

                # ------------------ Validation ----------------------------
                self.event_task_validation(self.event_sprint_version)
                if self.task_validation == 'Pass':
                    self.ui_event_task_config = 'Pass'
                    print('**-------->>> Event Task configuration has been done')
                else:
                    print('Event Task configuration failed <<<--------**')
                time.sleep(2.2)

                # ---------------------- Test configuration ------------------------------------------------------------
                self.driver.refresh()
                time.sleep(3)

                self.x_path_element_webdriver_wait(page_elements.event_config['Event_test_configure'])
                self.xpath.click()

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Job Role'))
                self.xpath.send_keys(self.job_name_sprint_version)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Stage'))
                self.xpath.send_keys(self.xl_event_test_stage)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Test'))
                self.xpath.send_keys(self.event_test_sprint_version)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.event_config['test_active'])
                self.xpath.click()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.buttons['event_test_save'])
                self.xpath.click()

                self.driver.refresh()
                time.sleep(3)

                # ------------------ Validation ----------------------------
                self.event_test_validation(self.event_sprint_version)
                if self.test_validation == 'Pass':
                    self.ui_event_test_config = 'Pass'
                    print('**-------->>> Event Test configuration has been done')
                else:
                    print('Event Test configuration failed <<<--------**')
                time.sleep(3)

            except Exception as error:
                api_logger.error(error)

    def event_task_validation(self, event_name):
        try:
            for i in self.xl_activity:
                self.activity_name = i

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event_config['task_is_config'])
            no_task_config = self.xpath.text
            if no_task_config.strip() == self.activity_name:
                self.task_validation = 'Pass'
                print('**-------->>> Event task config validated and continuing with event:: {}'.format(event_name))
            else:
                print('Event task config validation failed <<<--------**')
        except Exception as error:
            api_logger.error(error)

    def event_test_validation(self, event_name):
        try:
            self.driver.refresh()
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event_config['test_is_config'])
            no_test_config = self.xpath.text
            if no_test_config.strip() == self.event_sprint_version:
                self.test_validation = 'Pass'
                print('**-------->>> Event test config validated and continuing with event:: {}'.format(event_name))
            else:
                print('Event test config validation failed <<<--------**')
        except Exception as error:
            api_logger.error(error)
