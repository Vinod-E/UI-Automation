import time
import datetime
import page_elements
from logger_settings import api_logger
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
            self.more_tab()
            self.ui_more_tabs = 'Pass'

            time.sleep(3)
            self.embrace_tab()
            self.ui_embrace_module = 'Pass'

            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.tabs['embrace_candidate_tab'])
            self.xpath.click()
            print('**-------->>> Embrace app login')

            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.embrace['candidates_advance_search'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.embrace['candidate_text_box'])
            self.xpath.send_keys(self.event_sprint_version)

            time.sleep(2.2)
            self.x_path_element_webdriver_wait(page_elements.embrace['search_button'])
            self.xpath.click()
            self.ui_embrace_advance_search = 'Pass'

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.embrace['submit_behalf_of'])
            self.xpath.click()

            time.sleep(1)
            self.name_element_webdriver_wait(page_elements.embrace['task_acceptance'])
            self.name.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.embrace['submit_task'])
            self.xpath.click()
            self.ui_submit_behalf = 'Pass'

            time.sleep(1.5)

        except Exception as error:
            api_logger.error(error)

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

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['manage_task'])
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(5)

            # ---------------- Total tasks --------------
            total = self.driver.find_element_by_xpath(page_elements.embrace['total_tasks'])
            if str(self.total_tasks) in total.text:
                self.ui_total_tasks = 'Pass'
                self.ui_a2_assignment = 'Pass'

            # ---------------- Approved tasks --------------
            approved = self.driver.find_element_by_xpath(page_elements.embrace['approved_tasks'])
            if str(self.completed_tasks) in approved.text:
                self.ui_approved_tasks = 'Pass'

            # ---------------- Pending tasks --------------
            pending = self.driver.find_element_by_xpath(page_elements.embrace['pending_tasks'])
            if str(self.pending_tasks) in pending.text:
                self.ui_pending_tasks = 'Pass'

            # ---------------- Submitted tasks --------------
            submitted = self.driver.find_element_by_xpath(page_elements.embrace['submitted_tasks'])
            if str(self.submitted_tasks) in submitted.text:
                self.ui_submitted_tasks = 'Pass'

            # ---------------- Rejected tasks --------------
            rejected = self.driver.find_element_by_xpath(page_elements.embrace['rejected_tasks'])
            if str(self.rejected_tasks) in rejected.text:
                self.ui_rejected_tasks = 'Pass'

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(3)

        except Exception as error:
            api_logger.error(error)
