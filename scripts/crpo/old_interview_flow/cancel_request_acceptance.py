import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.old_interview_flow import cancel_interview_request


class CancelRequestAcceptance(cancel_interview_request.CancelInterviewRequest):
    def __init__(self):
        super(CancelRequestAcceptance, self).__init__()

        self.cancel_reason = ''
        self.reason = ''

        self.ui_event_tab_cr_a = []
        self.ui_advance_search_cr_a = []
        self.ui_event_details_cr_a = []
        self.ui_event_validation_cr_a = []
        self.ui_tracking_tab = []
        self.ui_cancel_request_sub_tab = []
        self.ui_request_validation = []
        self.ui_approve = []

    def cancel_request_acceptance(self):
        try:
            # ---------------------------- New tab to login as Admin ---------------------------------------------
            self.crpo_logout()
            self.login('Admin', self.xl_username, self.xl_password)
            # ----------------------- cancel request Process -----------------------------------------------------------
            time.sleep(5)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_name()
            self.event_validation('cancel request acceptance process', self.event_sprint_version_o)

            self.web_element_click_xpath(page_elements.tabs['event_tracking'])
            button_click.all_buttons(self, 'Interview Cancel Request')

            # --- validation check --------
            self.cancel_request_validation()
            # ------------------------------
            self.x_path_element_webdriver_wait(page_elements.interview['approve'].format('Approve Request'))
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.interview['c_r_comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            button_click.all_buttons(self, 'OK')

            # -------------------- output report values ----------------
            if self.cancel_reason.strip() == self.reason:
                self.ui_event_tab_cr_a = 'Pass'
                self.ui_advance_search_cr_a = 'Pass'
                self.ui_event_details_cr_a = 'Pass'
                self.ui_event_validation_cr_a = 'Pass'
                self.ui_tracking_tab = 'Pass'
                self.ui_cancel_request_sub_tab = 'Pass'
                self.ui_request_validation = 'Pass'
                self.ui_approve = 'Pass'

        except Exception as acceptance_error:
            ui_logger.error(acceptance_error)

    def cancel_request_validation(self):
        try:
            for i in self.xl_cancel_request_reason_o:
                self.reason = i

            self.web_element_text_xpath(
                page_elements.interview['approve'].format(self.reason))
            self.cancel_reason = self.text_value
            if self.cancel_reason.strip() == self.reason:
                print('**-------->>> Interview cancellation request raised :: {}'.format(self.cancel_reason))

        except Exception as error:
            ui_logger.error(error)
