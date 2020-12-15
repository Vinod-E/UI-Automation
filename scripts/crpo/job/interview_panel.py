import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.job import job_automation
from scripts.crpo.common import button_click


class InterviewPanel(job_automation.JobAutomation):
    def __init__(self):
        super(InterviewPanel, self).__init__()

        self.ui_tag_interviews = ''
        self.ui_interview_panel_action = ''
        self.ui_job_owners_tab = ''
        self.job_owners_total = ""

    def tag_interview_panel(self):
        self.driver.execute_script("window.scrollTo(0,-200);")
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name == self.job_name_sprint_version:
            print('**-------->>> Tag interview panel configuring to job:: {}'.format(self.job_name_sprint_version))
            try:
                # --------------------------------------- Tag Interviewers----------------------------------------------
                time.sleep(1)
                self.actions_dropdown()
                self.floating_action('tag_interviewers')
                self.ui_interview_panel_action = 'Pass'

                self.web_element_click_xpath(page_elements.job_config['interview_panel'].format(self.tag_interviewers))
                self.web_element_click_xpath(page_elements.job_config['add_interviewers_to_table'])

                time.sleep(1)
                button_click.button(self, 'Save')
                self.dismiss_message()

                # ----------------------------- Validation -------------------------------------------------------------
                time.sleep(2)
                self.sub_tab('job_owners')
                time.sleep(1)
                self.web_element_text_xpath(page_elements.job_config['owners_number'])
                self.job_owners_total = self.text_value
                if self.job_owners_total.strip() == 'Job Owners (3)':
                    print('**-------->>> Interviewers are added to job role')
                    self.ui_tag_interviews = 'Pass'
                    self.ui_job_owners_tab = 'Pass'
                else:
                    print('**-------->>> Failed to tag interviewers to job role')

            except Exception as config_message:
                ui_logger.error('Tag interviewers :: ', config_message)
