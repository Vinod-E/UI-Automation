from logger_settings import ui_logger
from scripts.crpo.output import mass_interview_output


class MassInterviewFlow(mass_interview_output.MassInterviewOutputFile):
    def __init__(self):
        super(MassInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def slot_configuration(self):
        self.applicant_status()
        self.event_search()
        self.slot_config()
        self.candidate_login_page()

        self.candidate_status_output_report()

    def create_lobby_room(self):
        self.create_room()
        self.manage_candidate()
        self.tag_candidate_to_room()

        self.slot_configuration_output_report()
        self.room_output_report()

    def interviewer_login(self):
        self.int1_login()
        self.select_candidate()
        self.video_interview()

        self.interviewer_login_output_report()
        self.lobby_output_report()

    def mass_int_feedback(self):
        self.mass_feedback()
        self.candidate_feedback_status()

        self.mass_feedback_output_report()


Object = MassInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.slot_configuration()
        Object.create_lobby_room()
        Object.interviewer_login()
        Object.mass_int_feedback()

        Object.overall_status()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        ui_logger.error(flow_error)
