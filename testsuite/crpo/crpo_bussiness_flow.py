from logger_settings import ui_logger
from scripts.crpo.output import crpo_bussiness_output


class BusinessFlow(crpo_bussiness_output.CrpoOutputFile):
    def __init__(self):
        self.New_email_id = input("Email ID :: ")
        super(BusinessFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def job_creation(self):
        try:
            self.create_job_role()
            self.config_selection_process()
            self.tag_interview_panel()
            self.job_ec_task_configuration()
            self.config_feedback_form()
            self.job_automation_config()
            self.edit_job()
            self.tag_requirement()
            self.un_tag_requirement()

            self.job_output_report()

        except Exception as job_error:
            ui_logger.error(job_error)

    def requirement_creation(self):
        try:
            self.create_requirement()
            self.requirement_configuration_tab()

            self.requirement_output_report()

        except Exception as req_error:
            ui_logger.error(req_error)

    def assessment_creation(self):
        try:
            self.clone_assessment()

            self.assessment_output_report()

        except Exception as test_error:
            ui_logger.error(test_error)

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
            ui_logger.error(event_error)

    def embrace_module(self):
        try:
            self.embrace_app_to_submit_task()
            self.submit_task_verification()

            self.task_assign_output_report()

        except Exception as error:
            ui_logger.error(error)


Object = BusinessFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.job_creation()
        Object.requirement_creation()
        Object.assessment_creation()
        Object.event_creation()
        Object.embrace_module()

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
