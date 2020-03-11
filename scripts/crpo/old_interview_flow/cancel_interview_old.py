import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import re_schedule_old


class CancelInterview(re_schedule_old.ReSchedule):
    def __init__(self):
        super(CancelInterview, self).__init__()

        self.ui_grid_cancel_action = []
        self.ui_cancel_interview = []
        self.ui_candidate_getby_c = []
        self.ui_applicant_current_status = []

    def cancel_interview(self):
        try:
            time.sleep(0.5)
            self.check_box()

            self.web_element_click_id(page_elements.grid_actions['cancel_interview'])
            self.web_element_send_keys_xpath(page_elements.interview['comment'], self.xl_cancel_request_comment_o)
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buttons['cancel_confirm'])

            # ------- Validation check -----------------------
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buckets['cancel_interviews'])
            self.web_element_click_id(page_elements.grid_actions['refresh'])

            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.current_status_validation('Cancelled')
            if self.applicant_current_status == 'Cancelled':
                # -------------------- output report values ----------------
                self.ui_grid_cancel_action = 'Pass'
                self.ui_cancel_interview = 'Pass'
                self.ui_candidate_getby_c = 'Pass'
                self.ui_applicant_current_status = 'Pass'
            time.sleep(1.2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -----logout from interviewer
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
            time.sleep(3)

        except Exception as cancel:
            api_logger.error(cancel)
