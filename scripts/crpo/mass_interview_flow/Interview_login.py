import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import manage_candidate


class InterviewLogin(manage_candidate.ManageCandidate):
    def __init__(self):
        super(InterviewLogin, self).__init__()

    def int1_login(self):
        try:
            time.sleep(0.5)
            self.crpo_logout()
            self.login('InterviewerTWO', self.xl_int1_name, self.xl_int1_pwd)
            # -------------------------------- Submit feedback Process -------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_m, 'Event')
            self.event_getby_name()
            self.event_validation('Interview lobby', self.event_sprint_version_m)
            self.actions_dropdown()
            self.floating_action('view_interview_panel')
            time.sleep(0.5)
        except Exception as error:
            ui_logger.error(error)


Object = InterviewLogin()
Object.crpo_login()
Object.event_search()
Object.slot_config()
Object.candidate_login_page()
Object.create_room()
Object.manage_candidate()
Object.tag_candidate_to_room()
Object.int1_login()
