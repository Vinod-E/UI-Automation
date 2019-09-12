import create_job_role
import page_elements
import Settings_New_Old_Form
import time
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions


class NewFeedBackForm(create_job_role.CreateJobRole, Settings_New_Old_Form.Settings):
    def __init__(self):
        super(NewFeedBackForm, self).__init__()
        self.job_name_sprint_version = 'Sprint_{}'.format(self.sprint_version)
        self.interview_stage = 'Skill 1 - Tech'
        self.interview_status = 'Scheduled'
        self.interview_comment = 'With New Form'
        self.interview_template = 'Bosch'

        self.ui_Floating_actions = []
        self.ui_getbyid_menu_feedback_form = []
        self.ui_interview_stage = []
        self.ui_new_form_configured = []

    def login(self):
        self.excel_read()
        self.crpo_login()

    def new_from_on(self):
        self.settings_on()

    def jobrole_search(self):
        time.sleep(3)
        self.job_advance_search()
        self.browser_close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def new_feedback_form(self):
        try:
            # -------------------------- Interview stage / feedback form configuration -----------------------------
            time.sleep(3)
            self.driver.refresh()
            self.x_path_element_webdriver_wait(page_elements.job['Floating_actions'])
            self.xpath.click()
            self.ui_Floating_actions = 'Pass'

            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.job['getbyid_menu_feedback_form'])
            self.xpath.click()
            self.ui_getbyid_menu_feedback_form = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.job['getbyid_feedback_form_configure'])
            self.xpath.click()

            self.xpath.send_keys(self.interview_stage)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)
            self.ui_interview_stage = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.job['getbyid_feedback_from_name_search'])
            self.xpath.send_keys(self.interview_template)

            self.x_path_element_webdriver_wait(page_elements.job['new_getbyid_feedback_from_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.job['new_getbyid_feedback_form_use'])
            self.xpath.click()
            self.ui_new_form_configured = 'Pass'
            time.sleep(2)

        except exceptions.NoSuchElementException as error:
            print error

    def new_from_off(self):
        time.sleep(3)
        self.settings_off()
