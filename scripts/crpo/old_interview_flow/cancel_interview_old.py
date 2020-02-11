import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import re_schedule_old


class CancelInterview(re_schedule_old.ReSchedule):
    def __init__(self):
        super(CancelInterview, self).__init__()

    def cancel_interview(self):
        try:
            time.sleep(2)
            self.check_box()

            self.id_element_webdriver_wait(page_elements.grid_actions['cancel_interview'])
            self.id.click()

            self.x_path_element_webdriver_wait(page_elements.interview['comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            time.sleep(2.5)
            self.x_path_element_webdriver_wait(page_elements.buttons['cancel_confirm'])
            self.xpath.click()

            # ------- Validation check -----------------------
            self.x_path_element_webdriver_wait(page_elements.buckets['cancel_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation('Cancelled')
            time.sleep(1.2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -----logout from interviewer
            # ---------------------------- New tab to login as Interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
            time.sleep(2.5)

        except Exception as cancel:
            api_logger.error(cancel)
