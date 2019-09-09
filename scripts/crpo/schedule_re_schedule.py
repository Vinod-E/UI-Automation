import crpo_login
import page_elements
import webdriver_wait
import config
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions


class ScheduleReSchedule(crpo_login.CrpoLogin, webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(ScheduleReSchedule, self).__init__()

        # ---------------------------------- Excel data ----------------------------------------------------------------
        self.xl_event_name_o = []
        self.xl_change_applicant_stage_o = []
        self.xl_change_applicant_status_o = []
        self.xl_change_status_comment_o = []
        self.xl_username_int1_o = []
        self.xl_password_int1_o = []
        self.xl_username_int2_o = []
        self.xl_password_int2_o = []
        self.xl_cancel_reschedule_comment_o = []
        self.xl_cancel_request_reason_o = []
        self.xl_cancel_request_comment_o = []
        self.xl_update_feedback_comment_o = []

        self.event_name_sprint_version_o = []

        self.ui_event_search_o = []
        self.ui_event_floating_action_o = []
        self.ui_event_applicant_action_o = []
        self.ui_applicant_search_o = []
        self.ui_change_applicant_status_action_o = []
        self.ui_applicant_schedule_o = []

        self.ui_int1_login_o = []
        self.ui_event_getby_id_o = []
        self.ui_event_float_o = []
        self.ui_event_interviews_o = []
        self.ui_reschedule_action_o = []
        self.ui_rescheduled_o = []

        # ---------------------------------- which excel sheet data to be proceed --------------------------------------
        schedule_workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['old_interview_file'])
        if self.login_server == 'beta':
            self.feedback_sheet1 = schedule_workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = schedule_workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = schedule_workbook.sheet_by_index(1)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def old_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_o.append(rows[0])
            if rows[1]:
                self.xl_change_applicant_stage_o.append(str(rows[1]))
            if rows[2]:
                self.xl_change_applicant_status_o.append(str(rows[2]))
            if rows[3]:
                self.xl_change_status_comment_o.append(str(rows[3]))
            if rows[4]:
                self.xl_username_int1_o.append(str(rows[4]))
            if rows[5]:
                self.xl_password_int1_o.append(str(rows[5]))
            if rows[6]:
                self.xl_username_int2_o.append(str(rows[6]))
            if rows[7]:
                self.xl_password_int2_o.append(str(rows[7]))
            if rows[8]:
                self.xl_cancel_reschedule_comment_o.append(str(rows[8]))
            if rows[9]:
                self.xl_cancel_request_reason_o.append(str(rows[9]))
            if rows[10]:
                self.xl_cancel_request_comment_o.append(str(rows[10]))
            if rows[11]:
                self.xl_update_feedback_comment_o.append((str(rows[11])))

            for j in self.xl_event_name_o:
                event_name = j
                self.event_name_sprint_version_o = event_name.format(self.sprint_version)
            print self.event_name_sprint_version_o

    def event_applicant_schedule(self):
        try:
            # --------------------------------- event details ----------------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event Details screen ------------------------"
            self.ui_event_search_o = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"
            self.ui_event_floating_action_o = 'Pass'
            self.ui_event_applicant_action_o = 'Pass'

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
            self.ui_applicant_search_o = 'Pass'

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
            time.sleep(2)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection_done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['comment'])
            time.sleep(2)
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.event['change_button'])
            self.xpath.click()
            self.ui_change_applicant_status_action_o = 'Pass'
            # --------------------------- Applicant Get By Id ----------------------------------------------------------

            time.sleep(3)
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format(self.event_name_sprint_version_o))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format('Scheduled'))
            if current_status.text == 'Scheduled':
                print "-------------------- Applicant Schedule to Interview ------------------------"
                self.ui_applicant_schedule_o = 'Pass'
                time.sleep(5)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print error

    def re_schedule(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            time.sleep(2)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "------------------ Interviewer1 Login successfully ------------------------"
            self.ui_int1_login_o = 'Pass'

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(5)
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
            self.ui_event_getby_id_o = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"
            self.ui_event_float_o = 'Pass'
            self.ui_event_interviews_o = 'Pass'

            # --------------------------------- Re-schedule interview --------------------------------------------------

            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['more'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['reschedule1'])
            self.xpath.click()
            self.ui_reschedule_action_o = 'Pass'

            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.event['reschedule_comment'])
            self.xpath.send_keys(self.xl_cancel_reschedule_comment_o)

            self.x_path_element_webdriver_wait(page_elements.event['reschedule_save'])
            self.xpath.click()

            # --------------------------- Applicant Get By Id ----------------------------------------------------------

            time.sleep(5)
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format(self.event_name_sprint_version_o))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[2])

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format('Rescheduled'))
            if current_status.text == 'Rescheduled':
                print "-------------------- Applicant Re-Schedule successfully -----------------"
                self.ui_rescheduled_o = 'Pass'
            time.sleep(3)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print error


# Object = ScheduleReSchedule()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.old_interview_excel_read()
#     Object.event_applicant_schedule()
#     Object.re_schedule()

# Object.browser_close()
