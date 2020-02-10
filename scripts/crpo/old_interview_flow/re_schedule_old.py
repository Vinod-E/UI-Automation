import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import schedule_old


class ReSchedule(schedule_old.Schedule):
    def __init__(self):
        super(ReSchedule, self).__init__()

    def interview_re_schedule(self):
        try:
            # --------------------------- New tab to login as interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerONE', self.xl_username_int1_o, self.xl_password_int1_o)

            # ----------------------- Reschedule Process --------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('reschedule process')
            self.floating_action()

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['event_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.check_box()

            self.x_path_element_webdriver_wait(page_elements.grid_actions['reschedule'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.interview['comments'])
            self.xpath.send_keys(self.xl_cancel_reschedule_comment_o)

            self.x_path_element_webdriver_wait(page_elements.buttons['create-save'])
            self.xpath.click()

            time.sleep(1)
            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])

            # ------- Validation check -----------------------
            self.current_status_validation('Rescheduled')
            time.sleep(1.2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as reschedule:
            api_logger.error(reschedule)
