import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.manage_interviewers import em_acceptance


class ManageInterviewersOutput(styles.FontColor, em_acceptance.EmAcceptance):
    def __init__(self):
        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 45)))
        self.Actual_success_cases = []

        super(ManageInterviewersOutput, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.admin_headers_col = 0
        self.admin_status_col = 1
        self.invite_int_col = 2
        self.invite_int_status_col = 3
        self.manage_int_col = 4
        self.manage_int_status_col = 5
        self.acceptance_int1_col = 6
        self.acceptance_int1_status_col = 7
        self.acceptance_int2_col = 8
        self.acceptance_int2_status_col = 9
        self.em_col = 10
        self.em_status_col = 11

        index = 0
        excelheaders = ['Admin', 'Status', 'Invite Interviewers', 'Status', 'Manage Interviewers', 'Status',
                        'Acceptance_Int1', 'Status', 'Acceptance_Int2', 'Status', 'EventManager', 'Status']
        for headers in excelheaders:
            if headers in ['Admin', 'Invite Interviewers', 'Manage Interviewers', 'Acceptance_Int1',
                           'Acceptance_Int2', 'EventManager', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def admin_config_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.admin_headers_col, 'Event Tab', self.style8)
            self.ws.write(3, self.admin_headers_col, 'Advance search', self.style8)
            self.ws.write(4, self.admin_headers_col, 'Event details', self.style8)
            self.ws.write(5, self.admin_headers_col, 'Event Validation', self.style8)
            self.ws.write(6, self.admin_headers_col, 'Floating actions', self.style8)
            self.ws.write(7, self.admin_headers_col, 'Manage Interviewers Action', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_mi)
                self.ws.write(2, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_mi)
                self.ws.write(3, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_mi)
                self.ws.write(4, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_mi)
                self.ws.write(5, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_mi)
                self.ws.write(6, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_manage_interviews_action_mi == 'Pass':
                self.Actual_success_cases.append(self.ui_manage_interviews_action_mi)
                self.ws.write(7, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])

        except Exception as error:
            ui_logger.error(error)

    def invite_int_config_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.invite_int_col, 'Skill1 Config', self.style8)
            self.ws.write(3, self.invite_int_col, 'Skill2 Config', self.style8)
            self.ws.write(4, self.invite_int_col, 'Nomination ON/OFF', self.style8)
            self.ws.write(5, self.invite_int_col, 'Mail to Interviewers', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.skill1_configured == 'Pass':
                self.Actual_success_cases.append(self.skill1_configured)
                self.ws.write(2, self.invite_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.invite_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.skill2_configured == 'Pass':
                self.Actual_success_cases.append(self.skill2_configured)
                self.ws.write(3, self.invite_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.invite_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.nomination_on_off == 'Pass':
                self.Actual_success_cases.append(self.nomination_on_off)
                self.ws.write(4, self.invite_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.invite_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.send_mail_to_interviewers == 'Pass':
                self.Actual_success_cases.append(self.send_mail_to_interviewers)
                self.ws.write(5, self.invite_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.invite_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])

        except Exception as error:
            ui_logger.error(error)

    def manage_interviewers_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.manage_int_col, 'Panel_Search_skill1', self.style8)
            self.ws.write(3, self.manage_int_col, 'Skill1-Pending', self.style8)
            self.ws.write(4, self.manage_int_col, 'Panel_Search_skill1', self.style8)
            self.ws.write(5, self.manage_int_col, 'Skill2-Pending', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.panel_skill11_search == 'Pass':
                self.Actual_success_cases.append(self.panel_skill11_search)
                self.ws.write(2, self.manage_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.manage_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.skill1_interviewer_status == 'Pass':
                self.Actual_success_cases.append(self.skill1_interviewer_status)
                self.ws.write(3, self.manage_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.manage_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.panel_skill12_search == 'Pass':
                self.Actual_success_cases.append(self.panel_skill12_search)
                self.ws.write(4, self.manage_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.manage_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.skill2_interviewer_status == 'Pass':
                self.Actual_success_cases.append(self.skill2_interviewer_status)
                self.ws.write(5, self.manage_int_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.manage_int_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])

        except Exception as error:
            ui_logger.error(error)

    def acceptance_int1_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.acceptance_int1_col, 'Event Tab', self.style8)
            self.ws.write(3, self.acceptance_int1_col, 'Advance search', self.style8)
            self.ws.write(4, self.acceptance_int1_col, 'Event details', self.style8)
            self.ws.write(5, self.acceptance_int1_col, 'Event Validation', self.style8)
            self.ws.write(6, self.acceptance_int1_col, 'Nomination Tab', self.style8)
            self.ws.write(7, self.acceptance_int1_col, 'Request Validation', self.style8)
            self.ws.write(8, self.acceptance_int1_col, 'Skill Validation', self.style8)
            self.ws.write(9, self.acceptance_int1_col, 'Accept Request', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_mi_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_mi_int1)
                self.ws.write(2, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_mi_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_mi_int1)
                self.ws.write(3, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_mi_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_mi_int1)
                self.ws.write(4, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_mi_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_mi_int1)
                self.ws.write(5, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_nomination_tab_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_nomination_tab_int1)
                self.ws.write(6, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_request_validation_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_request_validation_int1)
                self.ws.write(7, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_skill_request_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_skill_request_int1)
                self.ws.write(8, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_request_accepted_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_request_accepted_int1)
                self.ws.write(9, self.acceptance_int1_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.acceptance_int1_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])

        except Exception as error:
            ui_logger.error(error)

    def acceptance_int2_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.acceptance_int2_col, 'Event Tab', self.style8)
            self.ws.write(3, self.acceptance_int2_col, 'Advance search', self.style8)
            self.ws.write(4, self.acceptance_int2_col, 'Event details', self.style8)
            self.ws.write(5, self.acceptance_int2_col, 'Event Validation', self.style8)
            self.ws.write(6, self.acceptance_int2_col, 'Nomination Tab', self.style8)
            self.ws.write(7, self.acceptance_int2_col, 'Request Validation', self.style8)
            self.ws.write(8, self.acceptance_int2_col, 'Skill Validation', self.style8)
            self.ws.write(9, self.acceptance_int2_col, 'Accept Request', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_mi_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_mi_int2)
                self.ws.write(2, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_mi_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_mi_int2)
                self.ws.write(3, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_mi_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_mi_int2)
                self.ws.write(4, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_mi_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_mi_int2)
                self.ws.write(5, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_nomination_tab_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_nomination_tab_int2)
                self.ws.write(6, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_request_validation_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_request_validation_int2)
                self.ws.write(7, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_skill_request_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_skill_request_int2)
                self.ws.write(8, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_request_accepted_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_request_accepted_int2)
                self.ws.write(9, self.acceptance_int2_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.acceptance_int2_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])
        except Exception as error:
            ui_logger.error(error)

    def event_manager_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.em_col, 'Event Tab', self.style8)
            self.ws.write(3, self.em_col, 'Advance search', self.style8)
            self.ws.write(4, self.em_col, 'Event details', self.style8)
            self.ws.write(5, self.em_col, 'Event Validation', self.style8)
            self.ws.write(6, self.em_col, 'Floating actions', self.style8)
            self.ws.write(7, self.em_col, 'Manage Interviewers Action', self.style8)
            self.ws.write(8, self.em_col, 'Panel_Search_skill1', self.style8)
            self.ws.write(9, self.em_col, 'Skill1-Accepted', self.style8)
            self.ws.write(10, self.em_col, 'Panel_Search_skill1', self.style8)
            self.ws.write(11, self.em_col, 'Skill2-Accepted', self.style8)
            self.ws.write(12, self.em_col, 'Clear search', self.style8)
            self.ws.write(13, self.em_col, 'Approve Action', self.style8)
            self.ws.write(14, self.em_col, 'Approved', self.style8)
            self.ws.write(15, self.em_col, 'Approved_Request_Validate', self.style8)
            self.ws.write(16, self.em_col, 'SYNC Interviewers', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_em == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_em)
                self.ws.write(2, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_em == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_em)
                self.ws.write(3, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_em == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_em)
                self.ws.write(4, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_em == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_em)
                self.ws.write(5, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_em == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_em)
                self.ws.write(6, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_manage_interviews_action_em == 'Pass':
                self.Actual_success_cases.append(self.ui_manage_interviews_action_em)
                self.ws.write(7, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_panel_skill11_search == 'Pass':
                self.Actual_success_cases.append(self.ui_panel_skill11_search)
                self.ws.write(8, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_skill1_interviewer_status == 'Pass':
                self.Actual_success_cases.append(self.ui_skill1_interviewer_status)
                self.ws.write(9, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_panel_skill12_search == 'Pass':
                self.Actual_success_cases.append(self.ui_panel_skill12_search)
                self.ws.write(10, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_skill2_interviewer_status == 'Pass':
                self.Actual_success_cases.append(self.ui_skill2_interviewer_status)
                self.ws.write(11, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_clear_search == 'Pass':
                self.Actual_success_cases.append(self.ui_clear_search)
                self.ws.write(12, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_approve_action == 'Pass':
                self.Actual_success_cases.append(self.ui_approve_action)
                self.ws.write(13, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(13, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_approved == 'Pass':
                self.Actual_success_cases.append(self.ui_approved)
                self.ws.write(14, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(14, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_em_request_validated == 'Pass':
                self.Actual_success_cases.append(self.ui_em_request_validated)
                self.ws.write(15, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(15, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_sync_interviewers == 'Pass':
                self.Actual_success_cases.append(self.ui_sync_interviewers)
                self.ws.write(16, self.em_status_col, 'Pass', self.style7)
            else:
                self.ws.write(16, self.em_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'MANAGE INTERVIEWS FLOW', self.style4)
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
            self.ws.write(0, 14, 'Time Taken (min)', self.style4)
            self.ws.write(0, 15, minutes, self.style5)
            self.wb_Result.save(test_data_inputpath.output['manage_interviewers_output_report'])

        except Exception as error:
            ui_logger.error(error)
