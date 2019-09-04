import cancel_interview
import page_elements
import config
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class OldProvideFeedback(cancel_interview.CancelAndRequest):
    def __init__(self):
        super(OldProvideFeedback, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

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

        except exceptions.NoSuchElementException as error:
            print error

    def provide_feedback(self):
        try:
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


Object = OldProvideFeedback()
Object.login()
if Object.status_of_login == 'administrator':
    Object.old_interview_excel_read()
    # Object.settings_on()
    Object.event_applicant_schedule()
    Object.interviewer_login()
    # Object.cancel_interview()
    Object.cancel_interview_request()
    Object.provide_feedback()
    # Object.settings_off()


# Object.browser_close()

# ------ Cancel -> Bug has to be fix to be continue ---------------
