import time
import datetime
import page_elements
from logger_settings import ui_logger
from scripts.crpo.event import event_manage_task


class EmbraceApp(event_manage_task.EventManageTask):
    def __init__(self):
        super(EmbraceApp, self).__init__()

        self.ui_more_tabs = []
        self.ui_embrace_module = []
        self.ui_embrace_advance_search = []
        self.ui_submit_behalf = []
        self.ui_call_back_activity = []
        self.ui_a2_assignment = []
        self.ui_total_tasks = []
        self.ui_approved_tasks = []
        self.ui_pending_tasks = []
        self.ui_submitted_tasks = []
        self.ui_rejected_tasks = []

    def embrace_app_to_submit_task(self):
        try:
            time.sleep(0.5)
            self.more_tab()
            self.ui_more_tabs = 'Pass'
            self.embrace_tab()
            self.ui_embrace_module = 'Pass'

            self.driver.switch_to.window(self.driver.window_handles[1])

            time.sleep(1)
            self.web_element_click_xpath(page_elements.tabs['embrace_candidate_tab'])
            print('**-------->>> Embrace app login')

            time.sleep(1)
            self.web_element_click_xpath(page_elements.embrace['candidates_advance_search'])

            self.web_element_send_keys_xpath(page_elements.embrace['candidate_text_box'],
                                             self.event_sprint_version)

            self.web_element_click_xpath(page_elements.embrace['search_button'])
            self.ui_embrace_advance_search = 'Pass'

            self.web_element_click_xpath(page_elements.embrace['submit_behalf_of'])

            time.sleep(0.5)
            self.web_element_click_name(page_elements.embrace['task_acceptance'])

            self.web_element_click_xpath(page_elements.embrace['submit_task'])
            self.ui_submit_behalf = 'Pass'

            time.sleep(1.5)
        except Exception as error:
            ui_logger.error(error)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)

    def submit_task_verification(self):
        try:
            self.applicant_get_by()
            self.driver.switch_to.window(self.driver.window_handles[1])

            # ------------ Validation ----------------------------------
            self.applicant_current_status_validation(self.call_back_status)
            if self.applicant_current_status.strip() == self.call_back_status:
                self.ui_call_back_activity = 'Pass'
                print('**-------->>> Activity call Back happened')
            else:
                print('*Failed Activity call Back <<<----------**')

            self.floating_action()

            self.web_element_click_xpath(page_elements.floating_actions['manage_task'])
            self.driver.switch_to.window(self.driver.window_handles[2])

            # ---------------- Total tasks --------------
            self.web_element_text_xpath(page_elements.embrace['total_tasks'])
            if str(self.total_tasks) in self.text_value:
                self.ui_total_tasks = 'Pass'
                self.ui_a2_assignment = 'Pass'

            # ---------------- Approved tasks --------------
            self.web_element_text_xpath(page_elements.embrace['approved_tasks'])
            if str(self.completed_tasks) in self.text_value:
                self.ui_approved_tasks = 'Pass'

            # ---------------- Pending tasks --------------
            self.web_element_text_xpath(page_elements.embrace['pending_tasks'])
            if str(self.pending_tasks) in self.text_value:
                self.ui_pending_tasks = 'Pass'

            # ---------------- Submitted tasks --------------
            self.web_element_text_xpath(page_elements.embrace['submitted_tasks'])
            if str(self.submitted_tasks) in self.text_value:
                self.ui_submitted_tasks = 'Pass'

            # ---------------- Rejected tasks --------------
            self.web_element_text_xpath(page_elements.embrace['rejected_tasks'])
            if str(self.rejected_tasks) in self.text_value:
                self.ui_rejected_tasks = 'Pass'

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(0.5)

        except Exception as error:
            ui_logger.error(error)
