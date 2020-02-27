import xlwt
import styles
from datetime import date
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.applicant_actions import event_applicant_actions


class ApplicantActionsOutputFile(styles.FontColor, event_applicant_actions.ApplicantActions):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 27)))
        self.Actual_success_cases = []

        super(ApplicantActionsOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.admin_sc_col = 0
        self.admin_st_col = 1
        self.ea_sc_col = 2
        self.ea_st_col = 3

        index = 0
        excelheaders = ['Admin', 'Status', 'Event Actions', 'Status']
        for headers in excelheaders:
            if headers in ['Admin', 'Event Actions', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def admin_actions_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.admin_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.admin_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.admin_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.admin_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.admin_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.admin_sc_col, 'View applicant', self.style8)
            self.ws.write(8, self.admin_sc_col, 'Applicant advance search', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_ea)
                self.ws.write(2, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_ea)
                self.ws.write(3, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_ea)
                self.ws.write(4, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_ea)
                self.ws.write(5, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_ea)
                self.ws.write(6, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_applicant_action_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_event_applicant_action_ea)
                self.ws.write(7, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_advance_search_ea == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_advance_search_ea)
                self.ws.write(8, self.admin_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.admin_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['Applicant_action_output_report'])
        except Exception as error:
            api_logger.error(error)

    def event_applicant_actions_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.ea_sc_col, 'Change applicant status', self.style8)
            self.ws.write(3, self.ea_sc_col, 'Send SMS', self.style8)
            self.ws.write(4, self.ea_sc_col, 'Compose Mail', self.style8)
            self.ws.write(5, self.ea_sc_col, 'Tag Applicants', self.style8)
            self.ws.write(6, self.ea_sc_col, 'Untag Applicants', self.style8)
            self.ws.write(7, self.ea_sc_col, 'Send Registration Link', self.style8)
            self.ws.write(8, self.ea_sc_col, 'Send Admit card', self.style8)
            self.ws.write(9, self.ea_sc_col, 'View Registration Link', self.style8)
            self.ws.write(10, self.ea_sc_col, 'Manage task', self.style8)
            self.ws.write(11, self.ea_sc_col, 'View test status', self.style8)
            self.ws.write(12, self.ea_sc_col, 'Download resume', self.style8)
            self.ws.write(13, self.ea_sc_col, 'Single PDF', self.style8)
            self.ws.write(14, self.ea_sc_col, 'Generate docket', self.style8)
            self.ws.write(15, self.ea_sc_col, 'Compare Id card', self.style8)
            self.ws.write(16, self.ea_sc_col, 'Upload attachment', self.style8)
            self.ws.write(17, self.ea_sc_col, 'Change Business unit', self.style8)
            self.ws.write(18, self.ea_sc_col, 'View applicant json', self.style8)
            self.ws.write(19, self.ea_sc_col, 'Disable Registration link', self.style8)
            self.ws.write(20, self.ea_sc_col, 'Enable Registration link', self.style8)
            self.ws.write(21, self.ea_sc_col, 'Re Registration link', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status_action_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status_action_ae)
                self.ws.write(2, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_send_sms_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_send_sms_ae)
                self.ws.write(3, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_compose_mail_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_compose_mail_ae)
                self.ws.write(4, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_tag_applicant_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_tag_applicant_ae)
                self.ws.write(5, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_untag_applicant_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_untag_applicant_ae)
                self.ws.write(6, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_send_registration_link_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_send_registration_link_ae)
                self.ws.write(7, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_send_admit_card_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_send_admit_card_ae)
                self.ws.write(8, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_view_registration_link_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_view_registration_link_ae)
                self.ws.write(9, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_manage_task_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_manage_task_ae)
                self.ws.write(10, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_view_test_status_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_view_test_status_ae)
                self.ws.write(11, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_download_resume_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_download_resume_ae)
                self.ws.write(12, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_single_pdf_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_single_pdf_ae)
                self.ws.write(13, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(13, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_generate_docket_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_generate_docket_ae)
                self.ws.write(14, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(14, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_compare_id_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_compare_id_ae)
                self.ws.write(15, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(15, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_upload_attachment_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_upload_attachment_ae)
                self.ws.write(16, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(16, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_business_unit_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_change_business_unit_ae)
                self.ws.write(17, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(17, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_view_applicant_json_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_view_applicant_json_ae)
                self.ws.write(18, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(18, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_disable_registration_link_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_disable_registration_link_ae)
                self.ws.write(19, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(19, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_enable_registration_link_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_enable_registration_link_ae)
                self.ws.write(20, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(20, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_re_registration_link_ae == 'Pass':
                self.Actual_success_cases.append(self.ui_re_registration_link_ae)
                self.ws.write(21, self.ea_st_col, 'Pass', self.style7)
            else:
                self.ws.write(21, self.ea_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['Applicant_action_output_report'])
        except Exception as error:
            api_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)

            self.ws.write(0, 0, 'APPLICANT ACTIONS USECASES', self.style4)
            if self.Expected_success_cases == self.Actual_success_cases:
                self.ws.write(0, 1, 'Pass', self.style5)
            else:
                self.ws.write(0, 1, 'Fail', self.style6)

            self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
            self.ws.write(0, 3, 'Sprint_{}'.format(self.sprint_version), self.style5)
            self.ws.write(0, 4, 'SPRINT DATE', self.style4)
            self.ws.write(0, 5, self.date_now, self.style5)
            self.ws.write(0, 6, 'SERVER', self.style4)
            self.ws.write(0, 7, self.login_server, self.style5)
            self.ws.write(0, 8, 'Success Cases', self.style4)
            self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
            self.ws.write(0, 10, 'Failure Cases', self.style4)
            if failure_cases == 0:
                self.ws.write(0, 11, failure_cases, self.style5)
            else:
                self.ws.write(0, 11, failure_cases, self.style6)
            self.ws.write(0, 12, 'Success %', self.style4)
            self.ws.write(0, 13, percentage, self.style5)
            self.wb_Result.save(test_data_inputpath.output['Applicant_action_output_report'])

        except Exception as error:
            api_logger.error(error)
