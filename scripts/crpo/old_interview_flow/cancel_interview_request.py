import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.old_interview_flow import cancel_interview_old


class CancelInterviewRequest(cancel_interview_old.CancelInterview):
    def __init__(self):
        super(CancelInterviewRequest, self).__init__()

        self.ui_event_tab_cr = []
        self.ui_advance_search_cr = []
        self.ui_event_details_cr = []
        self.ui_event_validation_cr = []
        self.ui_floating_action_cr = []
        self.ui_event_interviews_action_cr = []
        self.ui_cancel_request_action = []
        self.ui_cancel_request_raise = []

    def cancel_interview_request(self):
        try:
            # ---------------------------- New tab to login as interviewer ---------------------------------------------
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_username_int2_o, self.xl_password_int2_o)
            # ----------------------- cancel request Process -----------------------------------------------------------
            time.sleep(3)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_name()
            self.event_validation('cancel request process')
            self.actions_dropdown()
            self.floating_action('event_interviews')

            time.sleep(0.5)
            self.check_box()
            self.web_element_click_id(page_elements.grid_actions['cancel_interview_request'])

            time.sleep(1.5)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Reason'),
                                             self.xl_cancel_request_reason_o)
            time.sleep(1)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.interview['comment'], self.xl_cancel_request_comment_o)
            time.sleep(2)
            button_click.button(self, 'Save')
            time.sleep(0.5)
            self.dismiss_message()

            # -------------------- output report values ----------------
            self.ui_event_tab_cr = 'Pass'
            self.ui_advance_search_cr = 'Pass'
            self.ui_event_details_cr = 'Pass'
            self.ui_event_validation_cr = 'Pass'
            self.ui_floating_action_cr = 'Pass'
            self.ui_event_interviews_action_cr = 'Pass'
            self.ui_cancel_request_action = 'Pass'
            self.ui_cancel_request_raise = 'Pass'

        except Exception as cancel_request:
            ui_logger.error(cancel_request)
