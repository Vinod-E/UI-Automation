import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.common import task_config


class ChangeStatus(task_config.TaskConfig):
    def __init__(self):
        super(ChangeStatus, self).__init__()

        self.applicant_statuschange = []
        self.applicant_schedule_statuschange = ''

    def applicant_status_change(self, stage, status, comment):
        try:
            # --------------------------- Change Applicant Status -------------------
            self.driver.execute_script("window.scrollTo(0,200);")

            self.web_element_click_id(page_elements.applicant_actions['Change_applicant_status'])
            time.sleep(3)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_stage'], stage)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_status'], status)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['comment'], comment)
            self.web_element_click_xpath(page_elements.buttons['status_change_button'])

            self.applicant_statuschange = 'True'

        except Exception as e:
            api_logger.error(e)

    def applicant_schedule_status_change(self, stage, status, comment):
        try:
            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,-100);")

            self.web_element_click_id(page_elements.applicant_actions['Change_applicant_status'])
            time.sleep(3)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_stage'], stage)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_status'], status)
            self.web_element_click_xpath(page_elements.change_applicant_status['Interviewer'])
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.change_applicant_status['Interviewer_selection_done'])
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['comment'], comment)
            self.web_element_click_xpath(page_elements.buttons['status_change_button'])

            self.applicant_schedule_statuschange = 'True'

        except Exception as e:
            api_logger.error(e)

    def job_applicant_status_change(self, stage, status, comment):
        try:
            # --------------------------- Change Applicant Status -------------------
            self.driver.execute_script("window.scrollTo(0,200);")

            self.web_element_click_id(page_elements.applicant_actions['job_Change_applicant_status'])
            time.sleep(3)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_stage'], stage)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['change_status'], status)
            self.web_element_send_keys_xpath(page_elements.change_applicant_status['comment'], comment)
            self.web_element_click_xpath(page_elements.buttons['status_change_button'])

            self.applicant_statuschange = 'True'

        except Exception as e:
            api_logger.error(e)
