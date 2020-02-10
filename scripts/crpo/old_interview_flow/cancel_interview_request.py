import time
import page_elements
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.old_interview_flow import cancel_interview_old


class CancelInterviewRequest(cancel_interview_old.CancelInterview):
    def __init__(self):
        super(CancelInterviewRequest, self).__init__()

    def cancel_interview_request(self):
        try:
            # ---------------------------- New tab to login as interviewer ---------------------------------------------
            time.sleep(1)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_username_int2_o, self.xl_password_int2_o)
            # ----------------------- cancel request Process -----------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('cancel request process')
            self.floating_action()

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['event_interviews'])
            self.xpath.click()

            time.sleep(1)
            self.check_box()
            self.id_element_webdriver_wait(page_elements.grid_actions['cancel_interview_request'])
            self.id.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Reason'))
            time.sleep(2)
            self.xpath.send_keys(self.xl_cancel_request_reason_o)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.interview['comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.buttons['cancel_request'])
            self.xpath.click()

        except Exception as cancel_request:
            api_logger.error(cancel_request)
