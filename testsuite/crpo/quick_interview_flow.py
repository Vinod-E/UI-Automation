from logger_settings import ui_logger
from scripts.crpo.output import quick_interview_output


class QuickFlow(quick_interview_output.QuickInterviewOutputFile):
    def __init__(self):
        super(QuickFlow, self).__init__()
        # ------------- Login session ------------------------
        self.crpo_login()

    def quick_interview_schedule(self):
        self.event_search()
        self.quick_schedule_output_report()

    def submit_quick_interview(self):
        self.submitted_feedback_int1()
        self.submitted_feedback_int2()

        self.quick_int1_output()
        self.quick_int2_output()


Object = QuickFlow()
if Object.status_of_login.strip() == 'administrator':
    try:
        Object.quick_interview_schedule()
        Object.submit_quick_interview()

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
