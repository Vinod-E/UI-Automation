import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.new_interview_flow import provide_feedback_new


class DraftNew(provide_feedback_new.ProvideFeedbackNew):
    def __init__(self):
        super(DraftNew, self).__init__()

        self.ui_event_tab_n = []
        self.ui_advance_search_n = []
        self.ui_event_details_n = []
        self.ui_event_validation_n = []
        self.ui_floating_action_n = []
        self.ui_event_interviews_action_n = []
        self.ui_provide_feedback_action_n = []
        self.ui_save_draft_n = []

    def save_draft_new(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_int1, self.xl_int1)

            # -------------------------------- Save Draft Process ------------------------------------------------------
            time.sleep(1)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.job_sprint_version_n, 'Event')
            self.event_getby_name()
            self.event_validation('save draft process')
            self.actions_dropdown()
            time.sleep(0.5)
            self.floating_action('event_interviews')

            self.check_box()
            self.provide_feedback_new(self.xl_comment_n)

            # ------------- save draft
            self.driver.execute_script("window.scrollTo(0,100);")
            button_click.button(self, 'Save as Draft')

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------------------- output report values ----------------
            self.ui_event_tab_n = 'Pass'
            self.ui_advance_search_n = 'Pass'
            self.ui_event_details_n = 'Pass'
            self.ui_event_validation_n = 'Pass'
            self.ui_floating_action_n = 'Pass'
            self.ui_event_interviews_action_n = 'Pass'
            self.ui_provide_feedback_action_n = 'Pass'
            self.ui_save_draft_n = 'Pass'

        except Exception as error:
            ui_logger.error(error)
