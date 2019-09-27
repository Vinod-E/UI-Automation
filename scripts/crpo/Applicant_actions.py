import crpo_login
import page_elements
import config
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import webdriver_wait


class ApplicantActions(crpo_login.CrpoLogin, webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(ApplicantActions, self).__init__()
        self.ui_event_tab = []
        self.ui_event_advance_search = []
        self.ui_event_get_by_id = []
        self.ui_event_floating_actions = []
        self.ui_event_applicants = []
        self.ui_candidate_status_changed = []
        self.ui_compose_mail = []
        self.ui_applicant_advance_search = []
        self.ui_candidate_get_by_id = []
        self.ui_candidate_tab = []
        self.ui_candidate_advance_search = []
        self.ui_tag_to_event = []

    def event_advance_search(self):
        # --------------------------------- event details ----------------------------------------------------------
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
        self.xpath.click()
        self.ui_event_tab = 'Pass'

        time.sleep(5)
        self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.event['event_names'])
        self.name.send_keys('Sprint_{}'.format(self.sprint_version))

        self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
        self.xpath.click()
        self.ui_event_advance_search = 'Pass'

        print "-------------------- Event Advance search ------------------------"

    def event_get_by_id(self):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
        self.xpath.click()
        self.ui_event_get_by_id = 'Pass'

    def event_applicants(self):
        time.sleep(2)
        # --------------------------------- event floating actions -------------------------------------------------
        self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
        self.xpath.click()
        self.ui_event_floating_actions = 'Pass'

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
        self.xpath.click()
        self.ui_event_applicants = 'Pass'
        print "-------------------- Floating action ------------------------"

    def change_applicant_status(self):
        # --------------------------- Change Applicant Status to Schedule ------------------------------------------
        time.sleep(3)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event['Change_applicant_status'])
        time.sleep(2)
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.event['change_stage'])
        self.xpath.send_keys('Group Discussion')

        self.x_path_element_webdriver_wait(page_elements.event['change_status'])
        self.xpath.send_keys('Shortlisted')

        self.x_path_element_webdriver_wait(page_elements.event['comment'])
        self.xpath.send_keys('Changed by UI Automation')

        self.x_path_element_webdriver_wait(page_elements.event['change_button'])
        self.xpath.click()
        time.sleep(3)
        print "-------------------- Applicant Schedule to Interview ------------------------"

    def compose_mail(self):
        # --------------------------- Change Applicant Status to Schedule ------------------------------------------
        time.sleep(3)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event['Compose_Mail'])
        time.sleep(2)
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.event['mail_subject'])
        self.xpath.send_keys('UI Automation Mail')

        self.x_path_element_webdriver_wait(page_elements.event['mail_content'])
        self.xpath.send_keys('All Copy rights from Hirepro')

        self.x_path_element_webdriver_wait(page_elements.event['mail_send'])
        self.xpath.click()
        time.sleep(3)
        self.ui_compose_mail = 'Pass'
        print "-------------------- Compose Mail to candidate ------------------------"

    def candidate_tab(self, candidate_name):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Candidate_Tab'])
        self.xpath.click()
        self.ui_candidate_tab = 'Pass'

        time.sleep(5)
        self.x_path_element_webdriver_wait(page_elements.candidate['candidate_search'])
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.candidate['candidate_name'])
        self.name.send_keys('Sprint_{}'.format(candidate_name))

        self.x_path_element_webdriver_wait(page_elements.candidate['Search_button'])
        self.xpath.click()
        self.ui_candidate_advance_search = 'Pass'

        self.name_element_webdriver_wait(page_elements.candidate['candidate_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.candidate['More'])
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.candidate['Tag_candidate_to_event'])
        self.xpath.click()

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Event_name'])
        self.xpath.send_keys('Sprint_{}'.format(self.sprint_version))
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Tag_to_event'])
        self.xpath.click()
        self.ui_tag_to_event = 'Pass'

        # ------------------------- Moving to event tab --------------------------------------
        self.event_advance_search()
        self.event_get_by_id()
        self.event_applicants()

    def applicant_advance_search(self, candidate_name):
        # ------------------------------- Applicant Advance search -------------------------------------------------
        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.event['applicant_advance_search'])
        time.sleep(3)
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.event['applicant_name'])
        self.name.send_keys('Sprint_{}'.format(candidate_name))

        self.x_path_element_webdriver_wait(page_elements.event['applicant_search_button'])
        time.sleep(2)
        self.xpath.click()
        print "-------------------- Applicant Advance search ------------------------"
        self.ui_applicant_advance_search = 'Pass'

    def candidate_get_by_id(self, status):
        # --------------------------- Applicant Get By Id ----------------------------------------------------------

        time.sleep(5)
        self.x_path_element_webdriver_wait(
            page_elements.event['applicant_getbyid'].format('Sprint_{}'.format(self.sprint_version)))
        self.xpath.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        current_status = self.driver.find_element_by_xpath(
            page_elements.event['current_status'].format(status))
        if current_status.text == status:
            print "-------------------- Candidate/Applicant status changed " \
                  "to {} successfully -----------------".format(status)
            self.ui_candidate_status_changed = 'Pass'
            self.ui_candidate_get_by_id = 'Pass'
        time.sleep(3)
        self.browser_close()
        self.driver.switch_to.window(self.driver.window_handles[0])
