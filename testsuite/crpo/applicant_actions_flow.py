from logger_settings import ui_logger
from scripts.crpo.output import applicant_actions_output


class ApplicantActionFlow(applicant_actions_output.ApplicantActionsOutputFile):
    def __init__(self):
        super(ApplicantActionFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def event_applicant_actions(self):
        try:
            self.event_tab_search()
            self.admin_actions_output_report()

            self.event_change_applicant_status()
            self.compose_mail()
            self.send_sms()
            self.tag_applicants_to_job_test()
            self.untag_applicant()
            self.registration_link()
            self.admit_card()
            self.view_registration_link()
            self.manage_task()
            self.view_test_status()
            self.download_resume()
            self.generate_single_pdf()
            self.generate_docket()
            self.compare_id_card()
            self.upload_attachment()
            self.change_business_unit()
            self.applicant_json()
            self.disable_registration_link()
            self.enable_registration_link()

            self.fill_registration()
            self.re_registration_link()

            self.event_applicant_actions_output_report()

        except Exception as error:
            ui_logger.error(error)

    def job_applicant_actions(self):
        try:
            self.job_tab_search()
            self.admin_actions_output_report_job()

            self.job_change_applicant_status()
            self.job_compose_mail()
            self.job_untag_applicant()
            self.job_copy_registration_link()
            self.job_manage_task()
            self.job_view_test_status()
            self.job_generate_single_pdf()
            self.email_mobile_verification_link()
            self.job_admit_card()

            self.job_applicant_actions_output_report()
        except Exception as error:
            ui_logger.error(error)


Object = ApplicantActionFlow()
if Object.status_of_login.strip() == 'administrator':

    try:
        Object.event_applicant_actions()
        Object.job_applicant_actions()

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
