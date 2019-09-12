import page_elements
import configure_new_feedback
import time
from selenium.common import exceptions


class NewFormSchedule(configure_new_feedback.NewFeedBackForm):
    def __init__(self):
        super(NewFormSchedule, self).__init__()

        self.event_name_sprint_version_o = 'Sprint_{}'.format(self.sprint_version)

        self.ui_event_tab_n = []
        self.ui_event_search_n = []
        self.ui_event_getbyid_n = []
        self.ui_event_floating_action_n = []
        self.ui_event_applicant_action_n = []
        self.ui_applicant_search_n = []
        self.ui_change_applicant_status_action_n = []
        self.ui_applicant_schedule_n = []

    def event_applicant_schedule_to_new_form_stage(self):
        try:
            # --------------------------------- event details ----------------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            time.sleep(3)
            self.xpath.click()
            self.ui_event_tab_n = 'Pass'

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
            self.ui_event_search_n = 'Pass'
            self.ui_event_getbyid_n = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['View_Applicants'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"
            self.ui_event_floating_action_n = 'Pass'
            self.ui_event_applicant_action_n = 'Pass'

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
            self.ui_applicant_search_n = 'Pass'

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['Change_applicant_status'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['change_stage'])
            self.xpath.send_keys(self.interview_stage)

            self.x_path_element_webdriver_wait(page_elements.event['change_status'])
            self.xpath.send_keys(self.interview_status)

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer'])
            time.sleep(2)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Interviewer_selection_done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['comment'])
            time.sleep(2)
            self.xpath.send_keys(self.interview_comment)

            self.x_path_element_webdriver_wait(page_elements.event['change_button'])
            self.xpath.click()
            self.ui_change_applicant_status_action_n = 'Pass'
            # --------------------------- Applicant Get By Id ----------------------------------------------------------

            time.sleep(3)
            self.x_path_element_webdriver_wait(
                page_elements.event['applicant_getbyid'].format(self.event_name_sprint_version_o))
            self.xpath.click()
            self.driver.switch_to.window(self.driver.window_handles[1])

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format(self.interview_status))
            if current_status.text == 'Scheduled':
                print "-------------------- Applicant Schedule to Interview ------------------------"
                self.ui_applicant_schedule_n = 'Pass'
                time.sleep(5)
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print error
