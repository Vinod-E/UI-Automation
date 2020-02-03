import datetime
from logger_settings import api_logger
from scripts.crpo.output import crpo_bussiness_output


class BusinessFlow(crpo_bussiness_output.CrpoOutputFile):
    def __init__(self):
        self.New_email_id = input("Email ID :: ")
        super(BusinessFlow, self).__init__()

    def job_creation(self):
        try:
            self.create_job_role()
            self.config_selection_process()
            self.job_ec_task_configuration()
            self.config_feedback_form()
            self.job_automation_config()
            self.tag_interview_panel()
            self.tag_requirement()
            self.un_tag_requirement()
            self.edit_job()

            self.job_output_report()

        except Exception as job_error:
            api_logger.error(job_error)

    def requirement_creation(self):
        try:
            self.create_requirement()
            self.requirement_configuration_tab()

            self.requirement_output_report()

        except Exception as req_error:
            api_logger.error(req_error)

    def assessment_creation(self):
        try:
            self.clone_assessment()

            self.assessment_output_report()

        except Exception as test_error:
            api_logger.error(test_error)

    def event_creation(self):
        try:
            self.create_event()
            self.event_test_task_configure()
            self.event_owner_configure()
            self.upload_candidates_to_event(self.New_email_id)
            self.event_applicants()
            self.event_change_applicant_status()
            self.manage_task_event()

            self.event_output_report()

        except Exception as event_error:
            api_logger.error(event_error)

    def embrace_module(self):
        try:
            self.embrace_app_to_submit_task()
            self.submit_task_verification()

            self.task_assign_output_report()

        except Exception as error:
            api_logger.error(error)


Object = BusinessFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.job_creation()
        print("Job Run completed at:: " + str(datetime.datetime.now()))

        Object.requirement_creation()
        print("Requirement Run completed at:: " + str(datetime.datetime.now()))

        Object.assessment_creation()
        print("Assessment Run completed at:: " + str(datetime.datetime.now()))

        Object.event_creation()
        print("Event Run completed at:: " + str(datetime.datetime.now()))

        Object.embrace_module()
        print("Embrace Run completed at:: " + str(datetime.datetime.now()))

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
