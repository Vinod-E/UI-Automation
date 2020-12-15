import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.event import create_event
from scripts.crpo.common import button_click


class TestTaskConfig(create_event.CreateEvent):
    def __init__(self):
        super(TestTaskConfig, self).__init__()

        self.activity_name = ''

        self.ui_event_config_tab = ''
        self.ui_event_task_config = ''
        self.task_validation = ''
        self.ui_event_test_config = ''
        self.test_validation = []

    def event_test_task_configure(self):

        self.getby_details_screen(self.event_sprint_version)
        if self.header_name.strip() == self.event_sprint_version:
            print('**-------->>> Event Validated and continuing '
                  'with task and test configuration to created event :: {}'.format(self.event_sprint_version))
            try:
                self.sub_tab('event_configuration_tab')
                self.ui_event_config_tab = 'Pass'
                # ---------------------- Task configuration ------------------------------------------------------------
                self.task_config(page_elements.event_config['event_task_configure'],
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

                # ---------------------- Test configuration ------------------------------------------------------------
                self.driver.refresh()
                time.sleep(3)

                self.web_element_click_xpath(page_elements.event_config['event_test_configure'])

                time.sleep(0.5)
                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Job Role'),
                                                 self.job_name_sprint_version)
                self.drop_down_selection()

                time.sleep(1)
                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Stage'),
                                                 self.xl_event_test_stage)
                self.drop_down_selection()

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Test'),
                                                 self.event_test_sprint_version)
                self.drop_down_selection()

                self.web_element_click_xpath(page_elements.event_config['test_active'])

                time.sleep(0.5)
                button_click.button(self, 'Save')

                self.driver.refresh()
                time.sleep(1)

                # ------------------ Validation ----------------------------
                self.event_test_validation(self.event_sprint_version)
                if self.test_validation == 'Pass':
                    self.ui_event_test_config = 'Pass'
                    print('**-------->>> Event Test configuration has been done')
                else:
                    print('Event Test configuration failed <<<--------**')

            except Exception as error:
                ui_logger.error(error)

    def event_task_validation(self, event_name):
        try:
            for i in self.xl_activity:
                self.activity_name = i

            self.web_element_text_xpath(page_elements.event_config['task_is_config'])
            no_task_config = self.text_value
            if no_task_config.strip() == self.activity_name:
                self.task_validation = 'Pass'
                print('**-------->>> Event task config validated and continuing with event:: {}'.format(event_name))
            else:
                print('Event task config validation failed <<<--------**')
        except Exception as error:
            ui_logger.error(error)

    def event_test_validation(self, event_name):
        try:
            self.driver.refresh()
            time.sleep(1)
            self.web_element_text_xpath(page_elements.event_config['test_is_config'])
            no_test_config = self.text_value
            if no_test_config.strip() == self.event_sprint_version:
                self.test_validation = 'Pass'
                print('**-------->>> Event test config validated and continuing with event:: {}'.format(event_name))
            else:
                print('Event test config validation failed <<<--------**')
        except Exception as error:
            ui_logger.error(error)
