import crpo_login
import page_elements
import webdriver_wait
import config
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions


class OldInterview(crpo_login.CrpoLogin, webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(OldInterview, self).__init__()

        # ---------------------------------- Excel data ----------------------------------------------------------------
        self.xl_event_name_o = []
        self.xl_change_applicant_stage_o = []
        self.xl_change_applicant_status_o = []
        self.xl_change_status_comment_o = []
        self.xl_username_int1_o = []
        self.xl_password_int1_o = []
        self.xl_username_int2_o = []
        self.xl_password_int2_o = []

        self.event_name_sprint_version_o = []

        # ---------------------------------- which excel sheet data to be proceed --------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['old_interview_file'])
        if self.login_server == 'beta':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.job_sheet1 = workbook.sheet_by_index(1)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def old_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.job_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.job_sheet1.row_values(number)

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

            for j in self.xl_event_name_o:
                event_name = j
                self.event_name_sprint_version_o = event_name.format(self.sprint_version)
            print self.event_name_sprint_version_o

    def settings_on(self):

        try:
            self.x_path_element_webdriver_wait(page_elements.settings['settings_icon'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['settings'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['Interview_module'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.settings['new_interview_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['on'])
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - On ------------------------"

        except exceptions.NoSuchElementException as error:
            print error

    def settings_off(self):

        try:
            self.x_path_element_webdriver_wait(page_elements.settings['settings_icon'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['settings'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['Interview_module'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.settings['new_interview_feedback_form'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.settings['off'])
            self.xpath.click()
            print "-------------------- New_interview_feedback_form - Off ------------------------"

        except exceptions.NoSuchElementException as error:
            print error

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

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            # ------------------------------- Applicant Advance search -------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['applicant_search_button'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['applicant_name'])
            self.name.send_keys(self.event_name_sprint_version_o)
            print "-------------------- Applicant Advance search ------------------------"

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

    def interviewer_login(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
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
            print "-------------------- Interviewer Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            # --------------------------------- event interviews -------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()
            print "-------------------- provide feedback opened ------------------------"

            # --------------------------------- Provide feedback -------------------------------------------------------
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[2])

            self.x_path_element_webdriver_wait(page_elements.feedback['maybe'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['save_draft'])
            self.xpath.click()
            print "-------------------- Save as Draft ------------------------"

        except exceptions.NoSuchElementException as error:
            print error


Object = OldInterview()
Object.login()
if Object.status_of_login == 'administrator':
    Object.old_interview_excel_read()
    # Object.settings_on()
    # Object.event_applicant_schedule()
    Object.interviewer_login()
    # Object.settings_off()


# Object.browser_close()
