import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.live_interview_flow import behalf_feedback


class SubmitFeedbackInt1(behalf_feedback.BehalfFeedback):
    def __init__(self):
        super(SubmitFeedbackInt1, self).__init__()

        self.ui_event_tab_int1 = []
        self.ui_advance_search_int1 = []
        self.ui_event_details_int1 = []
        self.ui_event_validation_int1 = []
        self.ui_floating_action_int1 = []
        self.ui_live_interviews_action_int1 = []

        self.ui_live_interview_validation_int1 = []
        self.ui_live_schedule_int1 = []
        self.ui_provide_feedback_button_int1 = []
        self.ui_provide_feedback_submitted_int1 = []

    def submit_feedback_live_int1(self):

        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_int1_l, self.xl_int1_l)

            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_l, 'Event')
            self.event_getby_details()
            self.event_validation('live-interview-schedule')
            self.floating_action()

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['live_interview'])
            self.xpath.click()

            # ---------- Validation
            self.live_screen_validation()

            self.x_path_element_webdriver_wait(page_elements.buckets['select_interview_stage'].format(self.stage2_l))
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Candidate Name'))
            self.xpath.send_keys(self.event_sprint_version_l)
            time.sleep(0.6)
            self.x_path_element_webdriver_wait(page_elements.buttons['live_applicant_search'])
            self.xpath.click()

            time.sleep(0.6)
            self.all_check_box_unlock()
            self.x_path_element_webdriver_wait(page_elements.buttons['live_schedule_multiple'])
            self.xpath.click()

            time.sleep(0.5)
            self.x_path_element_webdriver_wait(page_elements.live_interview['int2_select'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.buttons['live_schedule'])
            self.xpath.click()

# ----------- feedback providing
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.live_interview['down'])
            self.xpath.click()

            self.provide_feedback(page_elements.live_interview['shortlist'],
                                  self.xl_comment_l)

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

            # -------------------- output report values ----------------
            if self.get_event_name.strip() == self.event_sprint_version_l:
                self.ui_event_tab_int1 = 'Pass'
                self.ui_advance_search_int1 = 'Pass'
                self.ui_event_details_int1 = 'Pass'
                self.ui_event_validation_int1 = 'Pass'
                self.ui_floating_action_int1 = 'Pass'
                self.ui_live_interviews_action_int1 = 'Pass'

            if self.event_sprint_version_l in self.event_name_in_live:
                self.ui_live_interview_validation_int1 = 'Pass'
                self.ui_live_schedule_int1 = 'Pass'
                self.ui_provide_feedback_button_int1 = 'Pass'
                self.ui_provide_feedback_submitted_int1 = 'Pass'

        except Exception as error:
            api_logger.error(error)
