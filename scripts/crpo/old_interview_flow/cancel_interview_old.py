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
            self.name_element_webdriver_wait(page_elements.grid['check_box'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.grid_actions['cancel_interview'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.interview['c_comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            time.sleep(2.5)
            self.x_path_element_webdriver_wait(page_elements.interview['cancel_confirm'])
            self.xpath.click()

            # --------------------------- New login as Admin ---------------------------------------------
            time.sleep(7)
            self.crpo_logout(page_elements.login['int_logout'])
            self.login('Admin', self.xl_username, self.xl_password)
            time.sleep(3)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('cancel process')
            self.floating_action()
            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['View_Applicants'])
            self.xpath.click()

            time.sleep(1.8)
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_o, 'Applicant grid')
            self.applicant_getby_details(self.event_sprint_version_o)
            self.driver.switch_to.window(self.driver.window_handles[1])

            # ------- Validation check -----------------------
            self.current_status_validation('Cancelled')
            time.sleep(1.2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as cancel:
            api_logger.error(cancel)
