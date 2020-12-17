import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import slot_configuration


class CandidatePage(slot_configuration.SlotManagement):
    def __init__(self):
        super(CandidatePage, self).__init__()

    def candidate_login_page(self):
        try:

            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Candidate Id(s) (Eg: 1234, 2312,...)'),
                self.candidate_id_m)
            button_click.button(self, ' Search')
            self.web_element_click_xpath(page_elements.title['title'].format('View Interview Lobby Link'))
            time.sleep(0.5)
            button_click.all_buttons(self, 'OK')
            # input("Please fill the captcha and go ahead ::")
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            # button_click.button(self, 'Next')
            # print('**-------->>> Captcha verification completed manually successfully')

            # ------------------- Enter into Room -------------------------------
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Enter Candidate Id'), self.candidate_id_m)
            time.sleep(0.5)
            button_click.button(self, 'Enter the room')
            time.sleep(4)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as e:
            ui_logger.error(e)
