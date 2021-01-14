import time

from selenium.webdriver.common.by import By

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
        self.ui_validate_video_proctor_page = ''

        self.ui_interview_finish_button = ''
        self.ui_finished_interview = ''
        self.ui_next_candidate_screen_validate = ''

    def select_candidate(self):
        try:
            self.driver.refresh()
            time.sleep(2)
            button_click.button(self, 'Select Candidate')

            time.sleep(5)
            self.web_element_text_xpath(page_elements.mass_interview['lobby_cid'])
            self.lobby_cid = self.text_value

            if self.lobby_cid.strip() == str(self.candidate_id_m):
                print('**--------->>> Select Candidate is proper as per the flow')
                self.ui_select_candidate_action_m = 'Pass'
                self.ui_select_candidate_m = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def invite_video_interview(self):
        try:
            if self.lobby_cid.strip() == str(self.candidate_id_m):
                button_click.button(self, 'Invite Candidate & Go to Interview')
                print('**-------->>> Invite Candidate & Go to Interview successfully')
                time.sleep(2)
                self.web_element_click_xpath(page_elements.mass_interview['declare'])
                time.sleep(0.5)
                button_click.button(self, 'Proceed To Interview')
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                try:
                    self.web_element(By.TAG_NAME, 'h4')
                    print(self.text_value)
                    if self.text_value == 'Online Proctoring Setup':
                        print('**-------->>> Landed in Video Proctoring page')
                        self.ui_invite_candidate_action = 'Pass'
                        self.ui_invited_candidate_to_VC = 'Pass'
                        self.ui_validate_video_proctor_page = 'Pass'
                except Exception as error:
                    ui_logger.error(error)

                self.driver.close()
                time.sleep(5)
                self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as error:
            ui_logger.error(error)

    def finish_interview(self):
        try:
            time.sleep(2)
            button_click.button(self, 'Interview is Finished')
            self.web_element_click_xpath(page_elements.mass_interview['finish_interview'])
            time.sleep(5)
            self.driver.refresh()
            time.sleep(3)

            self.web_element_text_xpath(page_elements.mass_interview['message'])
            if self.text_value == self.xl_message_m[0]:
                print('**-------->>> Interview Finished by interviewer')
                self.ui_interview_finish_button = 'Pass'
                self.ui_finished_interview = 'Pass'
                self.ui_next_candidate_screen_validate = 'Pass'

        except Exception as error:
            ui_logger.error(error)
