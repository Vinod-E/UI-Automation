import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import create_room


class ManageCandidate(create_room.CreateRoom):
    def __init__(self):
        super(ManageCandidate, self).__init__()

    def manage_candidate(self):
        try:
            button_click.all_buttons(self, 'Manage Candidates')
            self.manage_candidate_validation('To Be Queued')

        except Exception as error:
            ui_logger.error(error)

    def tag_candidate_to_room(self):
        try:
            self.web_element_click_xpath(page_elements.title['tooltip'].format("'Assign Room'"))
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Room Name'), self.event_sprint_version_m)
            self.drop_down_selection()
            button_click.button(self, 'Assign Room')
            time.sleep(0.5)
            button_click.all_buttons(self, 'OK')
            time.sleep(1)
            self.manage_candidate_validation('Interview Pending	')

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
