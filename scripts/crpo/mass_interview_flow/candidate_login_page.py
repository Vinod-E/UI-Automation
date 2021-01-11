import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import slot_configuration


class CandidatePage(slot_configuration.SlotManagement):
    def __init__(self):
        super(CandidatePage, self).__init__()
        self.ui_c_msg1 = ''
        self.ui_c_msg2 = ''
        self.ui_c_message_2 = ''
        self.ui_c_message_1 = ''
        self.ui_c_msg3 = ''
        self.ui_c_message_3 = ''
        self.ui_c_msg4 = ''
        self.ui_c_message_4 = ''

    def candidate_login_page(self, message):
        if message == 'msg1':
            message_ele = page_elements.mass_interview['candidate_msg1']
            text_value = 'Almost there! You are next in queue'
        elif message == 'msg2':
            message_ele = page_elements.mass_interview['candidate_msg2']
            text_value = 'Please wait to be queued'
        elif message == 'msg3':
            message_ele = page_elements.mass_interview['candidate_msg3']
            text_value = 'It’s your turn for the interview'
        elif message == 'msg4':
            message_ele = page_elements.mass_interview['candidate_msg1']
            text_value = 'Almost there! You are next in queue'
        try:
            self.driver.execute_script("window.open('');")
            # Switch to the new window
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(self.candidate_login_link)
            # self.driver.get('https://ams.hirepro.in/interviewLobby/#/crpoqa/interview/?candidate=961494&h=$2a$12$codc4vW7CMhUYEtjji/iZOUFwEQmEqLBpmTsksPa2Q3Z.cvQEwYk2&event=3812')
            time.sleep(3)
            # ------------------- Enter into Room -------------------------------
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Enter Candidate Id'), self.candidate_id_m)
            time.sleep(0.5)
            button_click.button(self, 'Enter the room')

            self.web_element_text_xpath(message_ele)
            if message == 'msg1':
                if self.text_value.strip() == text_value:
                    self.ui_c_msg1 = 'Pass'
                    self.ui_c_message_1 = self.text_value.strip()
                    print('**-------->>> Successfully logged into Candidate page')
            elif message == 'msg2':
                if self.text_value.strip() == text_value:
                    self.ui_c_msg2 = 'Pass'
                    self.ui_c_message_2 = self.text_value.strip()
                    print('**-------->>> Successfully logged into Candidate page')
            elif message == 'msg3':
                if self.text_value.strip() == text_value:
                    self.ui_c_msg3 = 'Pass'
                    self.ui_c_message_3 = self.text_value.strip()
                    print('**-------->>> Successfully logged into Candidate page')
            else:
                if self.text_value.strip() == text_value:
                    self.ui_c_msg4 = 'Pass'
                    self.ui_c_message_4 = 'Your Interview is finished'
                    print('**-------->>> Successfully logged into Candidate page')
            time.sleep(4)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as e:
            ui_logger.error(e)
