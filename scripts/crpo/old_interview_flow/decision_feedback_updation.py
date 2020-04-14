import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import unlock_feedback


class DecisionFeedbackUpdate(unlock_feedback.UnlockFeedbackForm):
    def __init__(self):
        super(DecisionFeedbackUpdate, self).__init__()

        self.updated_decision = ''
        self.updated_feedback = ''
        self.update_feedback_comment = ''

        self.ui_completed_interviews_bucket_ud = []
        self.ui_provide_feedback_action_ud = []
        self.ui_submit_feedback_ud = []
        self.ui_update_decision = []
        self.ui_decision_validation = []

        self.ui_completed_interviews_bucket_uf = []
        self.ui_provide_feedback_action_uf = []
        self.ui_submit_feedback_uf = []
        self.ui_update_feedback = []
        self.ui_feedback_validation = []

    def decision_feedback_update(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_username_int1_o, self.xl_password_int1_o)
            # -------------------------------- unlock feedback form -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('unlock feedback form')
            self.floating_action()
            time.sleep(0.5)

            self.web_element_click_xpath(page_elements.floating_actions['event_interviews'])
            time.sleep(0.3)
            self.web_element_click_xpath(page_elements.buckets['completed_interviews'])
            self.web_element_click_id(page_elements.grid_actions['refresh'])

            self.check_box()
            self.provide_feedback(page_elements.interview['shortlist'],
                                  self.xl_update_feedback_comment_o)

            # ------ Submitted
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['submit_feedback'])
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(0.7)
            self.web_element_click_xpath(page_elements.buttons['agree'].format("'", 'submitWithouChange', "'"))
            self.web_element_click_xpath(page_elements.buttons['agree'].format("'", 'agreeToChange', "'"))
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------- validation check
            self.decision_feedback_validation()

            time.sleep(0.5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------------------- output report values ----------------
            if self.updated_decision.strip() == 'Shortlisted':
                self.ui_completed_interviews_bucket_ud = 'Pass'
                self.ui_provide_feedback_action_ud = 'Pass'
                self.ui_submit_feedback_ud = 'Pass'
                self.ui_update_decision = 'Pass'
                self.ui_decision_validation = 'Pass'
            if self.update_feedback_comment in self.updated_feedback.strip():
                self.ui_completed_interviews_bucket_uf = 'Pass'
                self.ui_provide_feedback_action_uf = 'Pass'
                self.ui_submit_feedback_uf = 'Pass'
                self.ui_update_feedback = 'Pass'
                self.ui_feedback_validation = 'Pass'
        except Exception as error:
            ui_logger.error(error)

    def decision_feedback_validation(self):
        try:
            self.web_element_click_id(page_elements.grid_actions['view_feedback'])
            self.driver.switch_to.window(self.driver.window_handles[1])

            time.sleep(0.5)
            self.web_element_text_xpath(page_elements.interview['approve'].format('Shortlisted'))
            self.updated_decision = self.text_value
            if self.updated_decision.strip() == 'Shortlisted':
                print('**-------->>> Decision updated successfully')

            time.sleep(0.5)
            for i in self.xl_update_feedback_comment_o:
                self.update_feedback_comment = i
            self.web_element_text_xpath(
                page_elements.interview['approve'].format('Through UI Automation Scheduling to interviewUpdated '
                                                          'feedback And Decision Maybe to Shortlist'))
            self.updated_feedback = self.text_value
            if self.update_feedback_comment in self.updated_feedback.strip():
                print('**-------->>> Feedback updated successfully')

        except Exception as error:
            ui_logger.error(error)
