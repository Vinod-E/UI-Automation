import schedule_re_schedule
import page_elements
import config
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class CancelAndRequest(schedule_re_schedule.ScheduleReSchedule):
    def __init__(self):
        super(CancelAndRequest, self).__init__()

        self.ui_cancel_interview_o = []
        self.ui_int2_login_o = []
        self.ui_event_getby_id__int2_o = []
        self.ui_event_float_int2_o = []
        self.ui_event_interviews_int2_o = []
        self.ui_cancel_interview_request_int2_o = []
        self.ui_interview_cancel_int2_o = []
        self.ui_approve_cancel_request_o = []
        self.ui_cancel_interview_request_action_o = []

    def cancel_interview(self):
        try:
            # --------------------------------- event interviews -------------------------------------------------------
            time.sleep(2)
            self.driver.refresh()
            time.sleep(3)
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['more'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['cancel_1'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['cancel_confirm'])
            self.xpath.click()
            time.sleep(2)

        except exceptions.ElementNotInteractableException as error:
            print error

    def schedule_again(self):
        try:
            # --------------------------- New tab to login as admin ----------------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- admin login ------------------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_ams_username)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_ams_password)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "------------------ Admin Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            time.sleep(2)
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            # ------------------------------- Applicant Advance search -------------------------------------------------
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
            time.sleep(3)
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['applicant_name'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['applicant_search_button'])
            time.sleep(2)
            self.xpath.click()
            print "-------------------- Applicant Advance search ------------------------"

            # --------------------------- Applicant Get By Id ----------------------------------------------------------

            time.sleep(5)
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format(self.event_name_sprint_version_o))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format('Cancelled'))
            if current_status.text == 'Cancelled':
                print "-------------------- Interview cancelled successfully -----------------"
                self.ui_cancel_interview_o = 'Pass'
            time.sleep(3)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['Change_applicant_status'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['change_stage'])
            self.xpath.send_keys(self.xl_change_applicant_stage_o)

            self.x_path_element_webdriver_wait(page_elements.event['change_status'])
            self.xpath.send_keys(self.xl_change_applicant_status_o)

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection_done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.event['change_button'])
            self.xpath.click()
            time.sleep(3)
            print "-------------------- Applicant Schedule to Interview ------------------------"

        except exceptions.NoSuchElementException as error:
            print error

    def cancel_interview_request(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab3');")
            self.driver.switch_to.window("tab3")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "------------------ Interviewer2 Login successfully ------------------------"
            self.ui_int2_login_o = 'Pass'
            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            time.sleep(2)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"
            self.ui_event_getby_id__int2_o = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"
            self.ui_event_float_int2_o = 'Pass'
            self.ui_event_interviews_int2_o = 'Pass'

            # --------------------------- cancel request raising -------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['cancel_request'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['cancel_request_reason'])
            time.sleep(2)
            self.xpath.send_keys(self.xl_cancel_request_reason_o)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.feedback['comment'])
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['cancel_request_save'])
            self.xpath.click()
            print "-------------------- Interview cancel request raised ------------------------"
            self.ui_cancel_interview_request_action_o = 'Pass'
            self.ui_cancel_interview_request_int2_o = 'Pass'
            time.sleep(3)

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print error

    def cancel_request_acceptance(self):
        try:
            # --------------------------- New tab to login as admin ----------------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- admin login ------------------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_ams_username)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_ams_password)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "------------------ Admin Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            time.sleep(2)
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event Details screen ------------------------"

            # ---------------------------------- Request Tracking ------------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['tracking_module'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['tracking_request'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['approve'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['request_comment'])
            time.sleep(2)
            self.xpath.send_keys(self.xl_cancel_request_comment_o)

            self.x_path_element_webdriver_wait(page_elements.event['request_ok'])
            self.xpath.click()
            self.ui_approve_cancel_request_o = 'Pass'
            print "-------------------- Interview cancellation request approved ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
            time.sleep(1.5)
            self.xpath.click()
            print "-------------------- Event Floating action ------------------------"

            # ------------------------------- Applicant Advance search -------------------------------------------------
            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['applicant_name'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['applicant_search_button'])
            time.sleep(2)
            self.xpath.click()
            print "-------------------- Applicant Advance search ------------------------"

            # --------------------------- Applicant Get By Id ----------------------------------------------------------

            time.sleep(3)
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format(self.event_name_sprint_version_o))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format('Cancelled'))
            if current_status.text == 'Cancelled':
                print "-------------------- Applicant Schedule to Interview ------------------------"
                self.ui_interview_cancel_int2_o = 'Pass'
            time.sleep(5)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print error

# Object = CancelAndRequest()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.old_interview_excel_read()
#     Object.event_applicant_schedule()
#     Object.re_schedule()

# Object.browser_close()
