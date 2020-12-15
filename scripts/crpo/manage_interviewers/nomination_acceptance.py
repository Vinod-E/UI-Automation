import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.manage_interviewers import manage_interviewers


class NominationAcceptance(manage_interviewers.ManageInterviewers):
    def __init__(self):
        super(NominationAcceptance, self).__init__()

        self.ui_event_tab_mi_int1 = ''
        self.ui_advance_search_mi_int1 = ''
        self.ui_event_details_mi_int1 = ''
        self.ui_event_validation_mi_int1 = ''
        self.ui_nomination_tab_int1 = ''
        self.ui_request_validation_int1 = ''
        self.ui_skill_request_int1 = ''
        self.ui_request_accepted_int1 = ''

        self.ui_event_tab_mi_int2 = ''
        self.ui_advance_search_mi_int2 = ''
        self.ui_event_details_mi_int2 = ''
        self.ui_event_validation_mi_int2 = ''
        self.ui_nomination_tab_int2 = ''
        self.ui_request_validation_int2 = ''
        self.ui_skill_request_int2 = ''
        self.ui_request_accepted_int2 = ''

    def interviewer_acceptance(self, login_name, password):
        try:
            self.crpo_logout()
            self.login('InterviewerONE', login_name, password)

            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_mi, 'Event')
            self.event_getby_name()
            self.getby_details_screen(self.event_sprint_version_mi)
            if self.header_name.strip() == self.event_sprint_version_mi:
                print('**-------->>> Event Validated and continuing '
                      'with {} created event :: {}'.format('Interviewer in', self.event_sprint_version_mi))

        except Exception as error:
            ui_logger.error(error)

    def nomination_int1(self):
        try:
            self.interviewer_acceptance(self.xl_user1_mi, self.xl_user1_mi)
            time.sleep(1)
            # -------------------- output report values ----------------
            if self.header_name.strip() == self.event_sprint_version_mi:
                self.ui_event_tab_mi_int1 = 'Pass'
                self.ui_advance_search_mi_int1 = 'Pass'
                self.ui_event_details_mi_int1 = 'Pass'
                self.ui_event_validation_mi_int1 = 'Pass'

            self.web_element_click_xpath(page_elements.tabs['nomination_tab'])
            time.sleep(1)
            self.web_element_text_xpath(page_elements.title['title'].format(self.event_sprint_version_mi))
            if self.text_value == self.event_sprint_version_mi:
                self.ui_nomination_tab_int1 = 'Pass'
                self.ui_request_validation_int1 = 'Pass'
                print('**-------->>> Entered into Nomination tab with interviewer1')
                print('**-------->>> Request validated with sent by event manger')
            time.sleep(0.3)

            self.web_element_text_xpath(page_elements.manage_interviews['skill_validate'])
            if self.skill1 in self.text_value:
                self.ui_skill_request_int1 = 'Pass'
            button_click.button(self, 'Confirm')
            button_click.all_buttons(self, 'OK')
            time.sleep(0.3)

            self.driver.refresh()
            time.sleep(2)
            self.web_element_text_xpath(page_elements.manage_interviews['no_invitation_message'])
            if self.text_value == "You don't have any nomination requests":
                self.ui_request_accepted_int1 = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def nomination_int2(self):
        try:
            self.interviewer_acceptance(self.xl_user2_mi, self.xl_user2_mi)
            time.sleep(1)
            # -------------------- output report values ----------------
            if self.header_name.strip() == self.event_sprint_version_mi:
                self.ui_event_tab_mi_int2 = 'Pass'
                self.ui_advance_search_mi_int2 = 'Pass'
                self.ui_event_details_mi_int2 = 'Pass'
                self.ui_event_validation_mi_int2 = 'Pass'

            self.web_element_click_xpath(page_elements.tabs['nomination_tab'])
            time.sleep(1)
            self.web_element_text_xpath(page_elements.title['title'].format(self.event_sprint_version_mi))
            if self.text_value == self.event_sprint_version_mi:
                self.ui_nomination_tab_int2 = 'Pass'
                self.ui_request_validation_int2 = 'Pass'
                print('**-------->>> Entered into Nomination tab with interviewer1')
                print('**-------->>> Request validated with sent by event manger')
            time.sleep(0.3)

            self.web_element_text_xpath(page_elements.manage_interviews['skill_validate'])
            if self.skill2 in self.text_value:
                self.ui_skill_request_int2 = 'Pass'
            button_click.button(self, 'Confirm')
            button_click.all_buttons(self, 'OK')
            time.sleep(0.3)

            self.driver.refresh()
            time.sleep(2)
            self.web_element_text_xpath(page_elements.manage_interviews['no_invitation_message'])
            if self.text_value == "You don't have any nomination requests":
                self.ui_request_accepted_int2 = 'Pass'

        except Exception as error:
            ui_logger.error(error)
