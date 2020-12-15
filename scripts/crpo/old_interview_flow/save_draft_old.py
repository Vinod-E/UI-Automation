import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import provide_feedback


class SaveAsDraft(provide_feedback.ProvideFeedback):
    def __init__(self):
        super(SaveAsDraft, self).__init__()

        self.ui_event_tab_d = []
        self.ui_advance_search_d = []
        self.ui_event_details_d = []
        self.ui_event_validation_d = []
        self.ui_floating_action_d = []
        self.ui_event_interviews_action_d = []
        self.ui_provide_feedback_action_d = []
        self.ui_save_draft = []

    def save_as_draft_old(self):
        try:
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_username_int1_o, self.xl_password_int1_o)

            # -------------------------------- Save Draft Process ------------------------------------------------------
            time.sleep(5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_name()
            self.event_validation('save draft process')
            self.actions_dropdown()
            self.floating_action('event_interviews')
            time.sleep(0.5)
            self.check_box()

            time.sleep(1)
            self.provide_feedback(page_elements.interview['maybe'],
                                  self.xl_change_status_comment_o)

            # ------------- save draft
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.web_element_click_xpath(page_elements.buttons['Save_draft'])

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------------------- output report values ----------------
            self.ui_event_tab_d = 'Pass'
            self.ui_advance_search_d = 'Pass'
            self.ui_event_details_d = 'Pass'
            self.ui_event_validation_d = 'Pass'
            self.ui_floating_action_d = 'Pass'
            self.ui_event_interviews_action_d = 'Pass'
            self.ui_provide_feedback_action_d = 'Pass'
            self.ui_save_draft = 'Pass'

        except Exception as error:
            ui_logger.error(error)
