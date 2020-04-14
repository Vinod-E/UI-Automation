from logger_settings import ui_logger
from scripts.crpo.output import old_interview_flow_output


class OldInterviewFlow(old_interview_flow_output.OldInterviewOutputFile):
    def __init__(self):
        super(OldInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def schedule_re_schedule(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Schedule / Re-Schedule >>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.interview_schedule()
            self.schedule_admin_output_report(0, 1)

            self.interview_re_schedule()
            self.reschedule_output_report(2, 3)

        except Exception as error:
            ui_logger.error(error)

    def cancel_interviews(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<< Cancel / Cancellation Request >>>>>>>>>>>>>>>>>>>>>>')
            self.cancel_interview()
            self.cancel_output_report(4, 5)

            self.interview_schedule()
            self.schedule_admin_output_report(6, 7)

            self.cancel_interview_request()
            self.cancel_request_raise_output_report(8, 9)

            self.cancel_request_acceptance()
            self.cancel_request_accept_output_report(10, 11)

        except Exception as error:
            ui_logger.error(error)

    def provide_feedback_flow(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Draft / Partial / Feedback >>>>>>>>>>>>>>>>>>>>>>')
            self.interview_schedule()
            self.schedule_admin_output_report(12, 13)

            self.save_as_draft_old()
            self.save_draft_output_report(0, 1)

            self.partial_feedback()
            self.partial_feedback_output_report(2, 3)
            self.partial_to_full_feedback_output_report(4, 5)

            self.submitted_feedback()
            self.submit_feedback_output_report(6, 7)

        except Exception as error:
            ui_logger.error(error)

    def unlock_update_feedback(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< unlock / decision / Feedback >>>>>>>>>>>>>>>>>>>>>>')
            self.unlock_feedback_form()
            self.unlock_feedback_output_report(8, 9)

            self.decision_feedback_update()
            self.update_decision_output_report(10, 11)
            self.update_feedback_output_report(12, 13)

        except Exception as error:
            ui_logger.error(error)


Object = OldInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.schedule_re_schedule()
        Object.cancel_interviews()
        Object.provide_feedback_flow()
        Object.unlock_update_feedback()

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
