import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.mass_interview_flow import manage_candidate


class InterviewLogin(manage_candidate.ManageCandidate):
    def __init__(self):
        super(InterviewLogin, self).__init__()

        self.int_name_verification = ''

        self.ui_int1_login_m = ''
        self.ui_event_tab_m_2 = ''
        self.ui_advance_search_m_2 = ''
        self.ui_event_details_m_2 = ''
        self.ui_event_validation_m_3 = ''
        self.ui_floating_action_m_4 = ''
        self.ui_view_interview_panel_action_m = ''
        self.int1_panel_validation_m = ''

    def int1_login(self):
        try:
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_int1_user, self.xl_int1_pwd)
            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_m, 'Event')
            self.event_getby_name()
            self.event_validation('Interview lobby', self.event_sprint_version_m)
            self.actions_dropdown()
            self.floating_action('view_interview_panel')
            time.sleep(0.5)

            # -------------------- output report values ----------------
            if self.event_validation_check == 'True':
                print('**-------->>> Landed into event screen successfully')
                self.ui_int1_login_m = 'Pass'
                self.ui_event_tab_m_2 = 'Pass'
                self.ui_advance_search_m_2 = 'Pass'
                self.ui_event_details_m_2 = 'Pass'
                self.ui_event_validation_m_3 = 'Pass'
                self.ui_floating_action_m_4 = 'Pass'
                self.ui_view_interview_panel_action_m = 'Pass'

            self.interview_panel_validation()
            if self.int_name_verification == 'Welcome {}'.format(self.interviewer_1_name):
                self.int1_panel_validation_m = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def interview_panel_validation(self):
        try:
            self.web_element_text_xpath(page_elements.mass_interview['interviewer_name'])
            self.int_name_verification = self.text_value
            if self.int_name_verification == 'Welcome {}'.format(self.interviewer_1_name):
                print('**-------->>> Entered into Interview panel lobby')

        except Exception as error:
            ui_logger.error(error)
