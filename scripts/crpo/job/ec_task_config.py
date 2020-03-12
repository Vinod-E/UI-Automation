import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import selection_process


class ECTaskconfig(selection_process.SelectionProcess):
    def __init__(self):
        super(ECTaskconfig, self).__init__()

        self.ui_ec_configure = []
        self.ui_task_configure = []
        self.ui_job_configure_tab = []

    def job_ec_task_configuration(self):
        self.job_validation('Job EC configuration')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.web_element_click_xpath(page_elements.tabs['job_configuration_tab'])
                self.ui_job_configure_tab = 'Pass'

                self.web_element_click_xpath(page_elements.job_config['ec_configure'])

                time.sleep(2)
                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                                 format('Select Eligibility Criteria'), self.xl_eligibility_criteria)
                self.drop_down_selection()

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                                 format('Select Stage'), self.xl_ec_stage)
                self.drop_down_selection()

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].
                                                 format('Select status'), self.xl_positive_status)
                self.drop_down_selection()

                self.web_element_send_keys_xpath(page_elements.job_config['ec_negative_stage'], self.xl_ec_stage)
                self.drop_down_selection()

                self.web_element_send_keys_xpath(
                    page_elements.job_config['ec_negative_status'], self.xl_negative_status)
                self.drop_down_selection()

                self.web_element_click_xpath(page_elements.buttons['job_ec_save'])
                print('**-------->>> Eligibility configuration done')
                self.ui_ec_configure = 'Pass'

                # ---------------------- Task configuration ------------------------------------------------------------
                self.task_config(page_elements.task_config['job_task_configure'],
                                 page_elements.text_fields['text_field'].format('Select Event'),
                                 self.job_name_sprint_version,
                                 self.xl_assign_stage_status,
                                 self.xl_positive_stage_status_job,
                                 self.xl_negative_stage_status_job,
                                 self.xl_A1)
                if self.task_configure_success == 'Pass':
                    self.ui_task_configure = 'Pass'

            except Exception as config_message:
                api_logger.error(config_message)
