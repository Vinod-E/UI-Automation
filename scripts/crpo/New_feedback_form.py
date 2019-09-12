import New_form_schedule
import schedule_re_schedule
import config
import page_elements
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class NewFeedBack(New_form_schedule.NewFormSchedule,
                  schedule_re_schedule.ScheduleReSchedule):
    def __init__(self):
        super(NewFeedBack, self).__init__()

        self.ui_int1_login_PF_n = []
        self.ui_int1_login_ET_n = []
        self.ui_int1_login_EAS_n = []
        self.ui_int1_login_EAS_getbyid_n = []
        self.ui_int1_login_EFA_n = []
        self.ui_int1_login_EFA_EI_n = []
        self.ui_int1_feedback_action_n = []
        self.ui_int1_feedback_screen_n = []
        self.ui_saveasdraft_n = []
        self.ui_int1_auto_decision = []
        self.ui_int1_submit_feedback = []

        self.ui_int2_login_PF_n = []
        self.ui_int2_feedback_screen_n = []
        self.ui_int2_manual_decision = []
        self.ui_int2_submit_feedback = []

    def interviewer_login_details(self):
        self.old_interview_excel_read()

    def login_int1(self):
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
            print "-------------------- Interviewer1 Login successfully ------------------------"
            self.ui_int1_login_PF_n = 'Pass'

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()
            self.ui_int1_login_ET_n = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"
            self.ui_int1_login_EAS_n = 'Pass'
            self.ui_int1_login_EAS_getbyid_n = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()
            self.ui_int1_login_EFA_n = 'Pass'

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"
            self.ui_int1_login_EFA_EI_n = 'Pass'

        except exceptions.NoSuchElementException as error:
            print error

    def new_save_draft_int1(self):
        try:
            # --------------------------------- event interviews -------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()
            print "-------------------- provide feedback opened ------------------------"
            self.ui_int1_feedback_action_n = 'Pass'

            # --------------------------------- Provide feedback -------------------------------------------------------
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.new_feedback['overall'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['duration'])
            self.xpath.send_keys('143')

            self.x_path_element_webdriver_wait(page_elements.new_feedback['save_as_draft'])
            self.xpath.click()
            print "-------------------- Save as Draft ------------------------"
            self.ui_int1_feedback_screen_n = 'Pass'
            self.ui_saveasdraft_n = 'Pass'

            time.sleep(1.5)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.NoSuchElementException as error:
            print error

    def new_provide_feedback_int1(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()

            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q1'])
            self.xpath.send_keys(Keys.PAGE_DOWN)
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q1_comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q2'])
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q2_comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q3'])
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['submit_feedback'])
            self.xpath.click()
            self.ui_int1_auto_decision = 'Pass'
            self.ui_int1_submit_feedback = 'Pass'
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions as error:
            print error

    def login_int2(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "-------------------- Interviewer2 Login successfully ------------------------"
            self.ui_int2_login_PF_n = 'Pass'

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()
            self.ui_int1_login_ET_n = 'Pass'

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

        except exceptions.NoSuchElementException as error:
            print error

    def new_provide_feedback_int2(self):
        try:
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()

            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q1'])
            self.xpath.send_keys(Keys.PAGE_DOWN)
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q1_comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q2'])
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q2_comment'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['Q3'])
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['maybe'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.new_feedback['overall'])
            self.xpath.send_keys(self.xl_change_status_comment_o)

            self.x_path_element_webdriver_wait(page_elements.new_feedback['submit_feedback'])
            self.xpath.click()
            self.ui_int2_feedback_screen_n = 'Pass'
            self.ui_int2_manual_decision = 'Pass'
            self.ui_int2_submit_feedback = 'Pass'
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions as error:
            print error
