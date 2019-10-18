import Event_Applicant_actions
import page_elements
import time
from selenium.webdriver.common.keys import Keys


class CandidateActions(Event_Applicant_actions.ApplicantActions):
    def __init__(self):
        super(CandidateActions, self).__init__()

    def candidate_tab(self, candidate_name):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Candidate_Tab'])
        self.xpath.click()
        self.ui_candidate_tab = 'Pass'

        time.sleep(5)
        self.x_path_element_webdriver_wait(page_elements.candidate['candidate_search'])
        self.xpath.click()

        self.name_element_webdriver_wait(page_elements.candidate['candidate_name'])
        self.name.send_keys(candidate_name)

        self.x_path_element_webdriver_wait(page_elements.candidate['Search_button'])
        self.xpath.click()
        self.ui_candidate_advance_search = 'Pass'

    def candidate_tag_to_event(self):
        self.name_element_webdriver_wait(page_elements.candidate['candidate_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.candidate['More'])
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.candidate['Tag_candidate_to_event'])
        time.sleep(2)
        self.xpath.click()

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Event_name'])
        self.xpath.send_keys('Sprint_{}'.format(self.sprint_version))
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)

        # time.sleep(2)
        # self.x_path_element_webdriver_wait(page_elements.candidate['Job_name'])
        # self.xpath.send_keys('Sprint_{}'.format(self.sprint_version))
        # self.xpath.send_keys(Keys.ARROW_DOWN)
        # self.xpath.send_keys(Keys.ENTER)

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.candidate['Tag_to_event'])
        self.xpath.click()
        self.ui_tag_to_event = 'Pass'
        time.sleep(3)

        # ------------------------- Moving to event tab --------------------------------------
        # self.event_advance_search()
        # self.event_get_by_id()
        # self.event_applicants()
