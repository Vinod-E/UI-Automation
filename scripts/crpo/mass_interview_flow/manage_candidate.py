import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import create_room


class ManageCandidate(create_room.CreateRoom):
    def __init__(self):
        super(ManageCandidate, self).__init__()

        self.ui_configure_slot_tab_m = ''
        self.ui_stage_search_m = ''
        self.ui_slot_creation_m = ''
        self.ui_slot_data_filled_m = ''
        self.ui_assign_slot_m = ''
        self.ui_communicate_slot_m = ''
        self.ui_search_slot_applicant_m = ''
        self.ui_interview_lobby_action_m = ''
        self.ui_open_lobby_link_m = ''
        self.ui_candidate_id_enter_m = ''
        self.ui_enter_room_action_m = ''
        self.ui_entered_candidate_login_m = ''
        self.candidate_interview_status_m = ''

        self.ui_assign_room_action_m = ''
        self.ui_tag_room_m = ''
        self.candidate_interview_status_t_m = ''

    def manage_candidate(self):
        try:
            button_click.all_buttons(self, 'Manage Candidates')
            self.manage_candidate_validation(self.xl_to_be_Queued[0])

            # -------------------- output report values ----------------
            if self.candidate_interview_status == self.xl_to_be_Queued[0]:
                self.ui_configure_slot_tab_m = 'Pass'
                self.ui_stage_search_m = 'Pass'
                self.ui_slot_creation_m = 'Pass'
                self.ui_slot_data_filled_m = 'Pass'
                self.ui_assign_slot_m = 'Pass'
                self.ui_communicate_slot_m = 'Pass'
                self.ui_search_slot_applicant_m = 'Pass'
                self.ui_interview_lobby_action_m = 'Pass'
                self.ui_open_lobby_link_m = 'Pass'
                self.ui_candidate_id_enter_m = 'Pass'
                self.ui_enter_room_action_m = 'Pass'
            if self.candidate_interview_status == 'Interview Pending':
                self.ui_entered_candidate_login_m = 'Pass'
                self.ui_assign_room_action_m = 'Pass'
                self.ui_tag_room_m = 'Pass'
                self.candidate_interview_status_m = 'Pass'
                self.candidate_interview_status_t_m = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def tag_candidate_to_room(self):
        try:
            self.web_element_click_xpath(page_elements.title['tooltip'].format("'Assign Room'"))
            time.sleep(3)
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Room Name'), self.event_sprint_version_m)
            time.sleep(1.5)
            self.drop_down_selection()
            time.sleep(1)
            button_click.click_button(self, "'", 'assignCandidateToRoom', "'")
            time.sleep(0.5)
            button_click.all_buttons(self, 'OK')
            time.sleep(1)
            self.manage_candidate_validation(self.xl_interview_pending[0])

        except Exception as error:
            ui_logger.error(error)

    def manage_candidate_validation(self, candidate_interview_status):
        try:
            self.web_element_text_xpath(page_elements.mass_interview['Interview_Status'])
            self.candidate_interview_status = self.text_value

            if self.candidate_interview_status == candidate_interview_status:
                print('**-------->>> Candidate {} successfully'.format(candidate_interview_status))
        except Exception as error:
            ui_logger.error(error)
