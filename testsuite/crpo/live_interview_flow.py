from logger_settings import ui_logger
from scripts.crpo.output import live_interview_flow_output


class LiveInterviewFlow(live_interview_flow_output.LiveInterviewOutputFile):
    def __init__(self):
        super(LiveInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def live_schedule_interview(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Live interview schedule >>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.live_schedule()
            self.live_schedule_output_report()

        except Exception as error:
            ui_logger.error(error)

    def schedule_behalf_of(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Behalf of submission feedback >>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.behalf_of_submission()
            self.behalf_of_output_report()

        except Exception as error:
            ui_logger.error(error)

    def submit_feedback_live(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Submit feedback by interviewers >>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.submit_feedback_live_int1()
            self.submit_int1_output_report()

            self.submit_feedback_live_int2()
            self.submit_int2_output_report()

        except Exception as error:
            ui_logger.error(error)


Object = LiveInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.live_schedule_interview()
        Object.schedule_behalf_of()
        Object.submit_feedback_live()

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
