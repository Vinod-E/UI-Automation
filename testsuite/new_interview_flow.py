from logger_settings import api_logger
from scripts.crpo.output import new_interview_flow_output


class NewInterviewFlow(new_interview_flow_output.NewInterviewOutputFile):
    def __init__(self):
        super(NewInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def new_feedback_form_config(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Settings-On/Off, ConfigureFeedback >>>>>>>>>>>>>>>>>>>>>>>>')
            self.new_feedback_on()
            self.feedback_configuration()
            self.new_feedback_off()
        except Exception as error:
            api_logger.error(error)

    def schedule_with_new_form(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Schedule with new Feedback >>>>>>>>>>>>>>>>>>>>>>>>')
            self.new_interview_schedule()

        except Exception as error:
            api_logger.error(error)

    def provide_feedback_process(self):
        try:
            print('<<<<<<<<<<<<<<<<<<<<<<< Save draft and Submit feedback >>>>>>>>>>>>>>>>>>>>>>>>')
            self.save_draft_new()
            self.submit_feedback_int1()
            self.submit_feedback_int2()

        except Exception as error:
            api_logger.error(error)


Object = NewInterviewFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.new_feedback_form_config()
        Object.schedule_with_new_form()
        Object.provide_feedback_process()

        Object.overall_status()
        Object.browser_close()

    except Exception as flow_error:
        api_logger.error(flow_error)
else:
    try:
        Object.server_connection_error()
        Object.internet_not_available()
        Object.browser_close()

    except Exception as flow_error:
        api_logger.error(flow_error)
