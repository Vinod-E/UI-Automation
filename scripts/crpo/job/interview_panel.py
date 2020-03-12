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
                self.floating_action()

                time.sleep(1)
                self.web_element_click_xpath(page_elements.floating_actions['tag_interviewers'])
                self.ui_interview_panel_action = 'Pass'

                self.web_element_click_xpath(page_elements.job_config['interview_panel'].format(
                    self.tag_interviewers))

                self.web_element_click_xpath(page_elements.job_config['add_interviewers_to_table'])

                time.sleep(1)
                self.web_element_click_xpath(page_elements.buttons['save_interviewers_to_panel'])

                # ----------------------------- Validation -------------------------------------------------------------
                time.sleep(1)
                self.web_element_click_xpath(page_elements.tabs['job_owners'])

                self.web_element_text_xpath(page_elements.job_validations['owners'])
                self.job_owners_total = self.text_value
                if self.job_owners_total == '(Total : 3)':
                    print('**-------->>> Interviewers are added to job role')
                    self.ui_tag_interviews = 'Pass'
                    self.ui_job_owners_tab = 'Pass'
                else:
                    print('**-------->>> Failed to tag interviewers to job role')
                time.sleep(1)

            except Exception as config_message:
                api_logger.error('Tag interviewers :: ', config_message)
