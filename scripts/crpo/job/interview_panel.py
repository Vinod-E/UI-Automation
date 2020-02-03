import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import job_automation


class InterviewPanel(job_automation.JobAutomation):
    def __init__(self):
        super(InterviewPanel, self).__init__()

        self.ui_tag_interviews = []
        self.ui_interview_panel_action = []
        self.ui_job_owners_tab = []
        self.job_owners_total = ""

    def tag_interview_panel(self):
        self.job_validation('tagging interview panel')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                # --------------------------------------- Tag Interviewers----------------------------------------------
                self.driver.refresh()
                time.sleep(5)
                self.floating_action()

                time.sleep(3)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['tag_interviewers'])
                self.xpath.click()
                self.ui_interview_panel_action = 'Pass'

                time.sleep(5)
                self.x_path_element_webdriver_wait(page_elements.job_config['interview_panel'].format(
                    self.tag_interviewers))
                self.xpath.click()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.job_config['add_interviewers_to_table'])
                self.xpath.click()

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.buttons['save_interviewers_to_panel'])
                self.xpath.click()
                time.sleep(3)

                # ----------------------------- Validation -------------------------------------------------------------
                self.x_path_element_webdriver_wait(page_elements.tabs['job_owners'])
                self.xpath.click()

                self.x_path_element_webdriver_wait(page_elements.job_validations['owners'])
                self.job_owners_total = self.xpath.text
                if self.job_owners_total == '(Total : 3)':
                    print('**-------->>> Interviewers are added to job role')
                    self.ui_tag_interviews = 'Pass'
                    self.ui_job_owners_tab = 'Pass'
                else:
                    print('**-------->>> Failed to tag interviewers to job role')
                time.sleep(5)

            except Exception as config_message:
                api_logger.error('Tag interviewers :: ', config_message)


# ob = InterviewPanel()
# ob.tag_interview_panel()
