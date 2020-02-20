import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import partial_feedback


class SubmittedFeedback(partial_feedback.PartialFeedback):
    def __init__(self):
        super(SubmittedFeedback, self).__init__()

        self.ui_event_tab_su = []
        self.ui_advance_search_su = []
        self.ui_event_details_su = []
        self.ui_event_validation_su = []
        self.ui_floating_action_su = []
        self.ui_event_interviews_action_su = []
        self.ui_provide_feedback_action_su = []
        self.ui_submit_feedback_su = []
        self.ui_completed_bucket_su = []
        self.ui_applicant_getby = []
        self.ui_applicant_current_status_su = []
        self.ui_submitted_validation = []

    def submitted_feedback(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_username_int2_o, self.xl_password_int2_o)

            # -------------------------------- Submit feedback Process -------------------------------------------------
            time.sleep(2.5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('submit feedback process')
            self.floating_action()
            time.sleep(1.5)

            self.x_path_element_webdriver_wait(page_elements.floating_actions['event_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.check_box()
            self.provide_feedback(page_elements.interview['maybe'],
                                  self.xl_change_status_comment_o)

            # ------ Submitted
            self.x_path_element_webdriver_wait(page_elements.buttons['submit_feedback'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['agree'].format("'", 'submitWithouChange', "'"))
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['agree'].format("'", 'agreeToChange', "'"))
            self.xpath.click()
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

            # ---- validation check
            self.submitted_validation('May be')
            if self.applicant_current_status.strip() == 'May be':
                print('**-------->>> Feedback submitted successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_su = 'Pass'
                self.ui_advance_search_su = 'Pass'
                self.ui_event_details_su = 'Pass'
                self.ui_event_validation_su = 'Pass'
                self.ui_floating_action_su = 'Pass'
                self.ui_event_interviews_action_su = 'Pass'
                self.ui_provide_feedback_action_su = 'Pass'
                self.ui_submit_feedback_su = 'Pass'
                self.ui_completed_bucket_su = 'Pass'
                self.ui_applicant_getby = 'Pass'
                self.ui_applicant_current_status_su = 'Pass'
                self.ui_submitted_validation = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def submitted_validation(self, status):
        try:
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.buckets['completed_interviews'])
            self.xpath.click()

            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation(status)

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            api_logger.error(error)
