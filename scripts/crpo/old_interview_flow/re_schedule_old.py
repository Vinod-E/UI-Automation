import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import schedule_old


class ReSchedule(schedule_old.Schedule):
    def __init__(self):
        super(ReSchedule, self).__init__()

        self.ui_event_tab_r = []
        self.ui_advance_search_r = []
        self.ui_event_details_r = []
        self.ui_event_validation_r = []
        self.ui_floating_action_r = []
        self.ui_event_interviews_action = []
        self.ui_grid_reschedule_action = []
        self.ui_reschedule = []
        self.ui_candidate_getby_r = []
        self.ui_change_applicant_status = []

    def interview_re_schedule(self):
        try:
            # --------------------------- New tab to login as interviewer ---------------------------------------------
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_username_int1_o, self.xl_password_int1_o)

            # ----------------------- Reschedule Process --------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('reschedule process')
            self.floating_action()

            self.web_element_click_xpath(page_elements.floating_actions['event_interviews'])

            time.sleep(0.5)
            self.check_box()

            self.web_element_click_id(page_elements.grid_actions['reschedule'])
            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.interview['comments'], self.xl_cancel_reschedule_comment_o)
            self.web_element_click_xpath(page_elements.buttons['create-save'])

            time.sleep(1)
            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])

            # ------- Validation check -----------------------
            self.current_status_validation('Rescheduled')
            if self.applicant_current_status.strip() == 'Rescheduled':
                print('**-------->>> Interview re-schedule happened successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_r = 'Pass'
                self.ui_advance_search_r = 'Pass'
                self.ui_event_details_r = 'Pass'
                self.ui_event_validation_r = 'Pass'
                self.ui_floating_action_r = 'Pass'
                self.ui_event_interviews_action = 'Pass'
                self.ui_grid_reschedule_action = 'Pass'
                self.ui_reschedule = 'Pass'
                self.ui_candidate_getby_r = 'Pass'
                self.ui_change_applicant_status = 'Pass'

            time.sleep(1.2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as reschedule:
            ui_logger.error(reschedule)
