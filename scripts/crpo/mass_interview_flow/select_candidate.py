import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import Interview_login


class SelectCandidate(Interview_login.InterviewLogin):
    def __init__(self):
        super(SelectCandidate, self).__init__()

        self.lobby_cid = ''
        self.invite_candidate = ''

        self.ui_select_candidate_action_m = ''
        self.ui_select_candidate_m = ''
        self.ui_invite_candidate_action = ''
        self.ui_invited_candidate_to_VC = ''

    def select_candidate(self):
        try:
            time.sleep(2)
            button_click.button(self, 'Select Candidate')

            time.sleep(5)
            self.web_element_text_xpath(page_elements.mass_interview['lobby_cid'])
            self.lobby_cid = self.text_value

            if self.lobby_cid.strip() == str(self.candidate_id_m):
                print('**-------->>> Select Candidate is proper as per the flow')
                self.ui_select_candidate_action_m = 'Pass'
                self.ui_select_candidate_m = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def video_interview(self):
        try:
            if self.lobby_cid.strip() == str(self.candidate_id_m):
                button_click.button(self, 'Invite Candidate & Go to Interview')
                print('**-------->>> Invite Candidate & Go to Interview successfully')
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()

                time.sleep(1)
                self.driver.switch_to.window(self.driver.window_handles[0])

            self.web_element_text_xpath(page_elements.buttons['common_button'].format('Interview is Finished'))
            self.invite_candidate = self.text_value

            if self.invite_candidate == 'Interview is Finished':
                print('**-------->>> Interview page opened and closed by automation script')
                self.ui_invite_candidate_action = 'Pass'
                self.ui_invited_candidate_to_VC = 'Pass'

        except Exception as error:
            ui_logger.error(error)
