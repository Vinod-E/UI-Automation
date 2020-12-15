import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.applicant_actions import event_applicant_actions


class JobApplicants(event_applicant_actions.EventApplicantActions):
    def __init__(self):
        super(JobApplicants, self).__init__()

        self.job_validation_check = ''

        self.ui_job_tab_ja = []
        self.ui_job_advance_search_ja = []
        self.ui_job_validation_ja = []
        self.ui_job_get_by = []
        self.ui_floating_action_ja = []
        self.ui_job_applicant_action_ja = []
        self.ui_applicant_advance_search_ja = []

    def job_more_actions(self):
        self.web_element_click_xpath(page_elements.applicant_actions['job_more_actions'])

    def job_tab_search(self):
        try:
            self.advance_search(page_elements.tabs['job_tab'])
            self.name_search(self.event_sprint_version_a, 'Job')
            self.job_getby_name(self.event_sprint_version_a)
            time.sleep(0.5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.getby_details_screen(self.event_sprint_version_a)

            self.actions_dropdown()
            self.floating_action('View_Applicants')
            time.sleep(0.5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.job_applicant_name_search(self._applicant_name)

            # -------------------- output report values ----------------
            if self.search == 'Pass':
                self.ui_job_tab_ja = 'Pass'
                self.ui_job_advance_search_ja = 'Pass'
            if self.header_name.strip() == self.event_sprint_version_a:
                print('**-------->>> Job get by name is working')
                self.ui_job_validation_ja = 'Pass'
                self.ui_job_get_by = 'Pass'
                self.ui_floating_action_ja = 'Pass'
                self.ui_job_applicant_action_ja = 'Pass'
            if self.job_search == 'True':
                self.ui_applicant_advance_search_ja = 'Pass'

            time.sleep(3)
        except Exception as error:
            ui_logger.error(error)
