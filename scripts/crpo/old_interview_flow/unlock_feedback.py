import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.old_interview_flow import submit_feedback_old


class UnlockFeedbackForm(submit_feedback_old.SubmittedFeedback):
    def __init__(self):
        super(UnlockFeedbackForm, self).__init__()

        self.ui_event_tab_un = []
        self.ui_advance_search_un = []
        self.ui_event_details_un = []
        self.ui_event_validation_un = []
        self.ui_floating_action_un = []
        self.ui_event_interviews_action_un = []
        self.ui_all_interviews_bucket_un = []
        self.ui_all_completed_bucket_un = []
        self.ui_unlock_feedback_action = []

    def unlock_feedback_form(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
            # -------------------------------- unlock feedback form -------------------------------------------------
            time.sleep(5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_name()
            self.event_validation('unlock feedback form')
            self.actions_dropdown()
            self.floating_action('event_interviews')
            time.sleep(0.5)

            self.web_element_click_xpath(page_elements.buckets['all_interviews'])
            self.web_element_click_xpath(page_elements.buckets['completed_interviews'])
            self.web_element_click_id(page_elements.grid_actions['refresh'])

            self.check_box()
            self.web_element_click_id(page_elements.grid_actions['unlock_feedback'])

            self.all_check_box_unlock()
            time.sleep(0.5)
            button_click.click_button(self, "'", 'unlockFeedback', "'")

            self.web_element_send_keys_xpath(page_elements.interview['c_r_comment'], self.xl_update_feedback_comment_o)

            button_click.all_buttons(self, 'OK')
            time.sleep(0.5)
            self.dismiss_message()

            time.sleep(0.5)
            button_click.button(self, 'Close')

            # -------------------- output report values ----------------
            self.ui_event_tab_un = 'Pass'
            self.ui_advance_search_un = 'Pass'
            self.ui_event_details_un = 'Pass'
            self.ui_event_validation_un = 'Pass'
            self.ui_floating_action_un = 'Pass'
            self.ui_event_interviews_action_un = 'Pass'
            self.ui_all_interviews_bucket_un = 'Pass'
            self.ui_all_completed_bucket_un = 'Pass'
            self.ui_unlock_feedback_action = 'Pass'

        except Exception as error:
            ui_logger.error(error)
