import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.quick_interview_flow import submit_feedback


class InterviewFeedbackSubmit(submit_feedback.ProvideFeedback):
    def __init__(self):
        super(InterviewFeedbackSubmit, self).__init__()

        self.ui_event_tab_q_int1 = ''
        self.ui_advance_search_q_int1 = ''
        self.ui_event_details_q_int1 = ''
        self.ui_event_validation_q_int1 = ''
        self.ui_floating_action_q_int1 = ''
        self.ui_event_interviews_action_q_int1 = ''
        self.ui_provide_feedback_action_q_int1 = ''
        self.ui_submit_feedback_q_int1 = ''

        self.ui_event_tab_q_int2 = ''
        self.ui_advance_search_q_int2 = ''
        self.ui_event_details_q_int2 = ''
        self.ui_event_validation_q_int2 = ''
        self.ui_floating_action_q_int2 = ''
        self.ui_event_interviews_action_q_int2 = ''
        self.ui_provide_feedback_action_q_int2 = ''
        self.ui_submit_feedback_q_int2 = ''
        self.ui_completed_bucket_q_int2 = ''
        self.ui_applicant_getby_q_int2 = ''
        self.ui_applicant_current_status_q_int2 = ''
        self.ui_submitted_validation_q_int2 = ''

    def submitted_feedback_int1(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_int1, self.xl_int1)

            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_q, 'Event')
            self.event_getby_details()
            self.event_validation('submit feedback process')
            self.floating_action()
            time.sleep(0.5)
            if self.event_validation_check == 'True':
                # -------------------- output report values ----------------
                self.ui_event_tab_q_int1 = 'Pass'
                self.ui_advance_search_q_int1 = 'Pass'
                self.ui_event_details_q_int1 = 'Pass'
                self.ui_event_validation_q_int1 = 'Pass'
                self.ui_floating_action_q_int1 = 'Pass'
                self.ui_event_interviews_action_q_int1 = 'Pass'

            self.web_element_click_xpath(page_elements.floating_actions['event_interviews'])

            time.sleep(0.5)
            self.check_box()
            self.provide_feedback(page_elements.interview['Quick_shortlist'], self.xl_comment_q)

        except Exception as error:
            ui_logger.error(error)

    def submitted_feedback_int2(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_int2, self.xl_int2)

            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_q, 'Event')
            self.event_getby_details()
            self.event_validation('submit feedback process')
            self.floating_action()
            time.sleep(0.5)

            self.web_element_click_xpath(page_elements.floating_actions['event_interviews'])

            time.sleep(0.5)
            self.check_box()
            self.provide_feedback(page_elements.interview['Quick_shortlist'], self.xl_comment_q)

            self.submitted_validation('Shortlisted')
            if self.applicant_current_status.strip() == 'Shortlisted':
                print('**-------->>> Feedback submitted successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_q_int2 = 'Pass'
                self.ui_advance_search_q_int2 = 'Pass'
                self.ui_event_details_q_int2 = 'Pass'
                self.ui_event_validation_q_int2 = 'Pass'
                self.ui_floating_action_q_int2 = 'Pass'
                self.ui_event_interviews_action_q_int2 = 'Pass'
                self.ui_provide_feedback_action_q_int2 = 'Pass'
                self.ui_provide_feedback_action_q_int1 = 'Pass'
                self.ui_submit_feedback_q_int1 = 'Pass'
                self.ui_submit_feedback_q_int2 = 'Pass'
                self.ui_completed_bucket_q_int2 = 'Pass'
                self.ui_applicant_getby_q_int2 = 'Pass'
                self.ui_applicant_current_status_q_int2 = 'Pass'
                self.ui_submitted_validation_q_int2 = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def submitted_validation(self, status):
        try:
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buckets['completed_interviews'])

            self.applicant_getby_details(self.event_sprint_version_q)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation(status)

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)
