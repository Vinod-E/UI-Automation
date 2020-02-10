import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import cancel_interview_request


class CancelRequestAcceptance(cancel_interview_request.CancelInterviewRequest):
    def __init__(self):
        super(CancelRequestAcceptance, self).__init__()

        self.cancel_reason = ''
        self.reason = ''

    def cancel_request_acceptance(self):
        try:
            # ---------------------------- New tab to login as interviewer ---------------------------------------------
            time.sleep(7)
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
            # ----------------------- cancel request Process -----------------------------------------------------------
            time.sleep(2.5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('cancel request acceptance process')

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.tabs['event_tracking'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.tabs['interview_cancel_request'])
            self.xpath.click()
            time.sleep(1)
            # --- validation check --------
            self.cancel_request_validation()
            # ------------------------------
            self.x_path_element_webdriver_wait(page_elements.interview['approve'].format('Approve Request'))
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.interview['c_r_comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            self.x_path_element_webdriver_wait(page_elements.buttons['ok'])
            self.xpath.click()

        except Exception as acceptance_error:
            api_logger.error(acceptance_error)

    def cancel_request_validation(self):
        try:
            for i in self.xl_cancel_request_reason_o:
                self.reason = i

            self.x_path_element_webdriver_wait(
                page_elements.interview['approve'].format(self.reason))
            self.cancel_reason = self.xpath.text
            if self.cancel_reason.strip() == self.reason:
                print('**-------->>> Interview cancellation request raised :: {}'.format(self.cancel_reason))

        except Exception as error:
            api_logger.error(error)
