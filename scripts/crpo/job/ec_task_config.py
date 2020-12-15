import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.job import selection_process
from scripts.crpo.common import button_click


class ECTaskconfig(selection_process.SelectionProcess):
    def __init__(self):
        super(ECTaskconfig, self).__init__()

        self.ui_ec_configure = []
        self.ui_task_configure = []
        self.ui_job_configure_tab = []

    def job_ec_task_configuration(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-200);")
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name.strip() == self.job_name_sprint_version:
            print('**-------->>> Job EC and Task configuring to job:: {}'.format(self.job_name_sprint_version))
            try:
                self.sub_tab('job_configuration_tab')
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

                time.sleep(0.5)
                button_click.button(self, 'Save')
                print('**-------->>> Eligibility configuration done')
                self.ui_ec_configure = 'Pass'

                # ---------------------- Task configuration ------------------------------------------------------------
                self.task_config(page_elements.job_config['task_configure'],
                                 page_elements.text_fields['text_field'].format('Select Event'),
                                 self.job_name_sprint_version,
                                 self.xl_assign_stage_status,
                                 self.xl_positive_stage_status_job,
                                 self.xl_negative_stage_status_job,
                                 self.xl_A1)
                if self.task_configure_success == 'Pass':
                    self.ui_task_configure = 'Pass'

            except Exception as config_message:
                ui_logger.error(config_message)
