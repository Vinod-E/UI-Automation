import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import unlock_feedback


class DecisionFeedbackUpdate(unlock_feedback.UnlockFeedbackForm):
    def __init__(self):
        super(DecisionFeedbackUpdate, self).__init__()

        self.updated_decision = ''
        self.updated_feedback = ''
        self.update_feedback_comment = ''

    def decision_feedback_update(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(7)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_username_int1_o, self.xl_password_int1_o)
            # -------------------------------- unlock feedback form -------------------------------------------------
            time.sleep(2.5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('unlock feedback form')
            self.floating_action()
            time.sleep(1.5)

            self.x_path_element_webdriver_wait(page_elements.floating_actions['event_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buckets['completed_interviews'])
            self.xpath.click()

            self.check_box()
            self.provide_feedback(page_elements.interview['shortlist'],
                                  self.xl_update_feedback_comment_o)

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

            # -------- validation check
            self.decision_feedback_validation()

        except Exception as error:
            api_logger.error(error)

    def decision_feedback_validation(self):
        try:
            self.id_element_webdriver_wait(page_elements.grid_actions['view_feedback'])
            self.id.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.interview['approve'].format('Shortlisted'))
            self.updated_decision = self.xpath.text
            if self.updated_decision.strip() == 'Shortlisted':
                print('**-------->>> Decision updated successfully')

            time.sleep(1)
            for i in self.xl_update_feedback_comment_o:
                self.update_feedback_comment = i
            self.x_path_element_webdriver_wait(
                page_elements.interview['approve'].format('Through UI Automation Scheduling to interviewUpdated '
                                                          'feedback And Decision Maybe to Shortlist'))
            self.updated_feedback = self.xpath.text
            if self.update_feedback_comment in self.updated_feedback.strip():
                print('**-------->>> Feedback updated successfully')

        except Exception as error:
            api_logger.error(error)
