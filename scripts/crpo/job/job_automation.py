import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import old_feedbackform
from selenium.webdriver.common.keys import Keys


class JobAutomation(old_feedbackform.FeedbackForm):
    def __init__(self):
        super(JobAutomation, self).__init__()

        self.ui_hopping_config = []
        self.ui_job_automation_tab = []

    def job_automation_config(self):
        self.job_validation('Automation Config')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                self.driver.implicitly_wait(5)
                self.x_path_element_webdriver_wait(page_elements.tabs['job_automation_tab'])
                self.xpath.click()
                self.ui_job_automation_tab = 'Pass'

                # --------------- Aptitude stage hopping --------------------------------
                self.x_path_element_webdriver_wait(page_elements.job_config['aptitude_stage_hop'])
                self.xpath.click()
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_stage'])
                self.xpath.send_keys(self.xl_hop_a_stage)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_status'])
                self.xpath.send_keys(self.xl_hop_a_status)

                # --------------- Eligibility stage hopping --------------------------------
                self.x_path_element_webdriver_wait(page_elements.job_config['eligibility_stage_hop'])
                self.xpath.click()
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_stage'])
                self.xpath.send_keys(self.xl_hop_e_stage)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_status'])
                self.xpath.send_keys(self.xl_hop_e_status)

                # --------------- Registration stage hopping --------------------------------
                self.x_path_element_webdriver_wait(page_elements.job_config['registration_stage_hop'])
                self.xpath.click()
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_stage'])
                self.xpath.send_keys(self.xl_hop_r_stage)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_status'])
                self.xpath.send_keys(self.xl_hop_r_status)
                time.sleep(2)

                # -------------- Test Automation & EC On config ---------------------
                self.x_path_element_webdriver_wait(page_elements.job_config['test_automation_button'])
                self.xpath.click()
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['ec_on_button'])
                self.xpath.click()
                time.sleep(2)

                self.driver.execute_script("window.scrollTo(0,100);")

                # --------------- Interview stage hopping --------------------------------
                self.x_path_element_webdriver_wait(page_elements.job_config['Hr_Interview_stage_hop'])
                self.xpath.click()
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_stage'])
                self.xpath.send_keys(self.xl_hop_hr_stage)

                self.x_path_element_webdriver_wait(page_elements.job_config['hop_status'])
                self.xpath.send_keys(self.xl_hop_hr_status)
                time.sleep(2)

                self.x_path_element_webdriver_wait(page_elements.job_config['ready_schedule_button'])
                self.xpath.click()

                self.driver.implicitly_wait(3)
                self.x_path_element_webdriver_wait(page_elements.buttons['Hopping_save_button'])
                self.xpath.send_keys(Keys.UP)
                self.xpath.click()
                time.sleep(4)

                print('**-------->>> Job Hopping, Automation set done')
                self.ui_hopping_config = 'Pass'

            except Exception as config_message:
                api_logger.error(config_message)


# ob = JobAutomation()
# ob.job_automation_config()
