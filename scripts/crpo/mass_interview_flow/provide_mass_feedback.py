import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import select_candidate


class MassFeedback(select_candidate.SelectCandidate):
    def __init__(self):
        super(MassFeedback, self).__init__()
        self.message_m = ''

        self.ui_provide_feedback_action_m = ''
        self.ui_p_f_screen_validate = ''
        self.ui_decision_select = ''
        self.ui_p_f_submit_button = ''
        self.ui_p_f_submitted = ''
        self.ui_view_profile_action = ''
        self.ui_profile_screen_validate = ''
        self.ui_candidate_status_m = ''
        self.ui_interview_finish_button = ''
        self.ui_finished_interview = ''
        self.ui_next_candidate_screen_validate = ''

    def mass_feedback(self):
        try:
            button_click.all_buttons(self, 'Provide Feedback')
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.web_element_click_xpath(page_elements.interview['shortlist'])
            self.web_element_send_keys_xpath(page_elements.interview['rating_1'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_1'], self.xl_comment_m)
            self.web_element_send_keys_xpath(page_elements.interview['rating_2'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_2'], self.xl_comment_m)
            self.web_element_send_keys_xpath(page_elements.mass_interview['overall_comment'], self.xl_comment_m)

            # ------ Submitted
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,200);")
            button_click.all_buttons(self, 'Submit Feedback')
            time.sleep(0.3)
            button_click.all_buttons(self, 'Agree and Submit')
            button_click.all_buttons(self, 'Agree and Submit')
            time.sleep(7)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)

    def candidate_feedback_status(self):
        try:
            button_click.all_buttons(self, 'View Profile')
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.applicant_current_status_validation(self.xl_shortlist_m[0])
            time.sleep(2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # ------- Interview Finished ------------------
            button_click.button(self, 'Interview is Finished')
            time.sleep(0.6)
            button_click.button(self, 'Interview is Finished')
            time.sleep(1.5)
            self.validation_next_candidate_screen()

        except Exception as error:
            ui_logger.error(error)

    def validation_next_candidate_screen(self):
        try:
            self.web_element_text_xpath(page_elements.mass_interview['message'])
            self.message_m = self.text_value
            if self.message_m.strip() == self.xl_message_m[0]:
                self.ui_provide_feedback_action_m = 'Pass'
                self.ui_p_f_screen_validate = 'Pass'
                self.ui_decision_select = 'Pass'
                self.ui_p_f_submit_button = 'Pass'
                self.ui_p_f_submitted = 'Pass'
                self.ui_view_profile_action = 'Pass'
                self.ui_profile_screen_validate = 'Pass'
                self.ui_candidate_status_m = 'Pass'
                self.ui_interview_finish_button = 'Pass'
                self.ui_finished_interview = 'Pass'
                self.ui_next_candidate_screen_validate = 'Pass'
        except Exception as error:
            ui_logger.error(error)
