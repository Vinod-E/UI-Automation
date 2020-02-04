import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.common import task_config


class ChangeStatus(task_config.TaskConfig):
    def __init__(self):
        super(ChangeStatus, self).__init__()

    def applicant_status_change(self, stage, status, comment):
        try:
            # --------------------------- Change Applicant Status -------------------
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(2)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['Change_applicant_status'])
            self.xpath.click()

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['change_stage'])
            self.xpath.send_keys(stage)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['change_status'])
            self.xpath.send_keys(status)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['comment'])
            self.xpath.send_keys(comment)

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['status_change_button'])
            self.xpath.click()

        except Exception as e:
            api_logger.error(e)

    def applicant_schedule_status_change(self, stage, status, comment):
        try:
            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,-100);")

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['Change_applicant_status'])
            self.xpath.click()
            time.sleep(2.9)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['change_stage'])
            self.xpath.send_keys(stage)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['change_status'])
            time.sleep(2)
            self.xpath.send_keys(status)

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['Interviewer'])
            time.sleep(2)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['Interviewer_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['Interviewer_selection_done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.change_applicant_status['comment'])
            time.sleep(2)
            self.xpath.send_keys(comment)

            self.x_path_element_webdriver_wait(page_elements.buttons['status_change_button'])
            self.xpath.click()

        except Exception as e:
            api_logger.error(e)
