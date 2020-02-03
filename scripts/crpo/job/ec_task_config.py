import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import selection_process
from selenium.webdriver.common.keys import Keys


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

                self.x_path_element_webdriver_wait(page_elements.tabs['job_configuration_tab'])
                self.xpath.click()
                self.ui_job_configure_tab = 'Pass'
                time.sleep(5)

                self.x_path_element_webdriver_wait(page_elements.job_config['ec_configure'])
                self.xpath.click()
                time.sleep(3)

                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                                   format('Select Eligibility Criteria'))
                self.xpath.send_keys(self.xl_eligibility_criteria)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                                   format('Select Stage'))
                self.xpath.send_keys(self.xl_ec_stage)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].
                                                   format('Select status'))
                self.xpath.send_keys(self.xl_positive_status)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.job_config['ec_negative_stage'])
                self.xpath.send_keys(self.xl_ec_stage)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.job_config['ec_negative_status'])
                self.xpath.send_keys(self.xl_negative_status)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                self.x_path_element_webdriver_wait(page_elements.buttons['job_ec_save'])
                self.xpath.click()
                print('**-------->>> Eligibility configuration done')
                self.ui_ec_configure = 'Pass'
                time.sleep(4)

                # ---------------------- Task configuration ------------------------------------------------------------
                self.task_config(page_elements.task_config['job_task_configure'],
                                 page_elements.text_fields['text_field'].format('Select Event'),
                                 self.job_name_sprint_version,
                                 self.xl_assign_stage_status,
                                 self.xl_positive_stage_status_job,
                                 self.xl_negative_stage_status_job,
                                 self.xl_A1)
                self.ui_task_configure = 'Pass'

            except Exception as config_message:
                api_logger.error(config_message)


# ob = ECTaskconfig()
# ob.job_ec_configuration()
