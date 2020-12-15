import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.live_interview_flow import behalf_feedback
from scripts.crpo.common import button_click


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
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_int1_l, self.xl_int1_l)

            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_l, 'Event')
            self.event_getby_name()
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.getby_details_screen(self.event_sprint_version_l)
            if self.header_name.strip() == self.event_sprint_version_l:
                print('**-------->>> Event Validated and continuing '
                      'with {} created event :: {}'.format('live-interview-schedule', self.event_sprint_version_l))
            self.actions_dropdown()
            self.floating_action('live_interview')

            # ---------- Validation
            time.sleep(6)
            self.live_screen_validation()

            self.web_element_click_xpath(page_elements.buckets['select_interview_stage'].format(self.stage2_l))

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Candidate Name'),
                                             self.event_sprint_version_l)
            self.web_element_click_xpath(page_elements.buttons['live_applicant_search'])

            time.sleep(0.5)
            self.all_check_box_unlock()
            button_click.button(self, 'Schedule Selected')
            self.web_element_click_xpath(page_elements.live_interview['int2_select'])
            button_click.button(self, ' Schedule')

# ----------- feedback providing
            time.sleep(1)
            self.web_element_click_xpath(page_elements.live_interview['down'])

            self.is_behalf_int = 0
            self.live_provide_feedback(page_elements.live_interview['shortlist'], self.xl_comment_l)

            # -------------------- output report values ----------------
            if self.header_name.strip() == self.event_sprint_version_l:
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
            ui_logger.error(error)
