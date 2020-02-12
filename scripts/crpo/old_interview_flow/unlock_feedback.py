import time
import page_elements
from logger_settings import api_logger
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
            time.sleep(1)
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
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
            self.x_path_element_webdriver_wait(page_elements.buckets['all_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buckets['completed_interviews'])
            self.xpath.click()

            self.check_box()
            self.id_element_webdriver_wait(page_elements.grid_actions['unlock_feedback'])
            self.id.click()

            self.all_check_box_unlock()
            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['agree'].format("'", 'unlockFeedback', "'"))
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.interview['c_r_comment'])
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.buttons['ok'])
            self.xpath.click()

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.buttons['done'])
            self.xpath.click()

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
            api_logger.error(error)
