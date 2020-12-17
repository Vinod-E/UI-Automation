import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import candidate_login_page


class CreateRoom(candidate_login_page.CandidatePage):
    def __init__(self):
        super(CreateRoom, self).__init__()
        self.room_info = ''
        self.candidate_interview_status = ''

        self.ui_create_room_action_m = ''
        self.ui_room_created_m = ''
        self.ui_active_room_action_m = ''
        self.ui_room_activate_m = ''
        self.ui_room_validation_m = ''

    def create_room(self):
        try:
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.actions_dropdown()
            self.floating_action('interview_lobby')
            self.driver.execute_script("window.scrollTo(0,-200);")
            button_click.button(self, 'Create Room')
            print('**-------->>> Enter into to interview lobby')

            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Room Name'), self.event_sprint_version_m)

            self.web_element_click_xpath(page_elements.title['title'].format('Select Interviewers'))
            self.web_element_send_keys_xpath(
                page_elements.title['title'].format('Type here to search'), self.xl_int1_name)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_click_xpath(page_elements.title['title'].format('Select Participants'))
            self.web_element_send_keys_xpath(
                page_elements.title['title'].format('Type here to search'), self.xl_int2_name)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')
            print('**-------->>> Details are filled to create ROOM')

            time.sleep(1)
            button_click.click_button(self, "'", 'createRoom', "'")
            print('**-------->>> ROOM created successfully')

            # ----------------------------- Activate Room ------------------------------------------
            self.web_element_click_xpath(page_elements.title['tooltip'].format("'Activate Room'"))
            button_click.all_buttons(self, 'OK')

            # ------ Validation check
            self.room_validation()

        except Exception as error:
            ui_logger.error(error)

    def room_validation(self):
        try:
            self.web_element_text_xpath(page_elements.mass_interview['room_name'])
            self.room_info = self.text_value

            if self.event_sprint_version_m in self.room_info.strip():
                print('**-------->>> Room created successfully')
                print('**-------->>> Room activated successfully')
                self.ui_create_room_action_m = 'Pass'
                self.ui_room_created_m = 'Pass'
                self.ui_active_room_action_m = 'Pass'
                self.ui_room_activate_m = 'Pass'
                self.ui_room_validation_m = 'Pass'

        except Exception as error:
            ui_logger.error(error)
