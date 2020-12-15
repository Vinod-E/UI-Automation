import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.job import old_feedbackform
from scripts.crpo.common import button_click


class JobAutomation(old_feedbackform.FeedbackForm):
    def __init__(self):
        super(JobAutomation, self).__init__()

        self.ui_hopping_config = []
        self.ui_job_automation_tab = []

    def job_automation_config(self):
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name.strip() == self.job_name_sprint_version:
            print('**-------->>> Job automations are configuring to job:: {}'.format(self.job_name_sprint_version))

            try:
                time.sleep(2)
                self.sub_tab('job_automation_tab')
                self.ui_job_automation_tab = 'Pass'

                # --------------- Aptitude stage hopping --------------------------------
                self.web_element_click_xpath(page_elements.job_config['aptitude_stage_hop'])
                time.sleep(0.5)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_stage'], self.xl_hop_a_stage)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_status'], self.xl_hop_a_status)

                # --------------- Eligibility stage hopping --------------------------------
                self.web_element_click_xpath(page_elements.job_config['eligibility_stage_hop'])
                time.sleep(0.5)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_stage'], self.xl_hop_e_stage)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_status'], self.xl_hop_e_status)

                # --------------- Registration stage hopping --------------------------------
                self.web_element_click_xpath(page_elements.job_config['registration_stage_hop'])
                time.sleep(0.5)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_stage'], self.xl_hop_r_stage)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_status'], self.xl_hop_r_status)

                # -------------- Test Automation & EC On config ---------------------
                self.web_element_click_xpath(page_elements.job_config['test_automation_button'])
                time.sleep(0.5)

                self.web_element_click_xpath(page_elements.job_config['ec_on_button'])
                time.sleep(0.5)

                self.driver.execute_script("window.scrollTo(0,200);")

                # --------------- Interview stage hopping --------------------------------
                self.web_element_click_xpath(page_elements.job_config['Hr_Interview_stage_hop'])
                time.sleep(0.5)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_stage'], self.xl_hop_hr_stage)

                self.web_element_send_keys_xpath(page_elements.job_config['hop_status'], self.xl_hop_hr_status)
                time.sleep(0.5)

                self.web_element_click_xpath(page_elements.job_config['ready_schedule_button'])

                self.driver.execute_script("window.scrollTo(0,200);")
                time.sleep(1)
                button_click.button(self, 'Save')
                time.sleep(2)
                self.dismiss_message()

                print('**-------->>> Job Hopping, Automation set done')
                self.ui_hopping_config = 'Pass'

            except Exception as config_message:
                ui_logger.error(config_message)
