import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import decision_feedback_updation


class OldInterviewOutputFile(styles.FontColor, decision_feedback_updation.DecisionFeedbackUpdate):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 108)))
        self.Actual_success_cases = []

        super(OldInterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
# ------------- Headers_set1
        index = 0
        excelheaders = ['Schedule-Admin', 'Status', 'Reschedule-Int1', 'Status', 'Cancel-Int1', 'Status',
                        'Schedule-Admin', 'Status', 'CancelRequest-Int2', 'Status', 'CancelRequestAccept-Admin',
                        'Status', 'Schedule-Admin', 'Status']
        for headers in excelheaders:
            if headers in ['Schedule-Admin', 'Reschedule-Int1', 'Cancel-Int1', 'CancelRequest-Int2',
                           'CancelRequestAccept-Admin', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
# ------------- Headers_set2
        index1 = 0
        excelheaders_1 = ['Draft-Int1', 'Status', 'Partial-Int1', 'Status', 'Partial_to_full-Int1', 'Status',
                          'Submitted-Int2', 'Status', 'Unlock-Admin', 'Status', 'Update_Decision-Int1',
                          'Status', 'Update_Feedback-Int1', 'Status']
        for headers in excelheaders_1:
            if headers in ['Draft-Int1', 'Partial-Int1', 'Partial_to_full-Int1', 'Submitted-Int2', 'Unlock-Admin',
                           'Update_Decision-Int1', 'Update_Feedback-Int1', 'Status']:
                self.ws.write(14, index1, headers, self.style0)
            else:
                self.ws.write(14, index1, headers, self.style1)
            index1 += 1
        print('Excel Headers are printed successfully')

    def schedule_admin_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, u_col, 'Event Tab', self.style8)
            self.ws.write(3, u_col, 'Advance search', self.style8)
            self.ws.write(4, u_col, 'Event details', self.style8)
            self.ws.write(5, u_col, 'Event Validation', self.style8)
            self.ws.write(6, u_col, 'Floating actions', self.style8)
            self.ws.write(7, u_col, 'View applicant', self.style8)
            self.ws.write(8, u_col, 'Applicant advance search', self.style8)
            self.ws.write(9, u_col, 'Change status action', self.style8)
            self.ws.write(10, u_col, 'Change applicant status', self.style8)
            self.ws.write(11, u_col, 'Candidate details screen', self.style8)
            self.ws.write(12, u_col, 'Applicant current status', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab)
                self.ws.write(2, s_col, 'Pass', self.style7)
            else:
                self.ws.write(2, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search)
                self.ws.write(3, s_col, 'Pass', self.style7)
            else:
                self.ws.write(3, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details)
                self.ws.write(4, s_col, 'Pass', self.style7)
            else:
                self.ws.write(4, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation)
                self.ws.write(5, s_col, 'Pass', self.style7)
            else:
                self.ws.write(5, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action)
                self.ws.write(6, s_col, 'Pass', self.style7)
            else:
                self.ws.write(6, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_applicant_action == 'Pass':
                self.Actual_success_cases.append(self.ui_event_applicant_action)
                self.ws.write(7, s_col, 'Pass', self.style7)
            else:
                self.ws.write(7, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_advance_search)
                self.ws.write(8, s_col, 'Pass', self.style7)
            else:
                self.ws.write(8, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status_action == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status_action)
                self.ws.write(9, s_col, 'Pass', self.style7)
            else:
                self.ws.write(9, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status)
                self.ws.write(10, s_col, 'Pass', self.style7)
            else:
                self.ws.write(10, s_col, 'Fail', self.style3)
            # -----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_getby == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_getby)
                self.ws.write(11, s_col, 'Pass', self.style7)
            else:
                self.ws.write(11, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status)
                self.ws.write(12, s_col, 'Pass', self.style7)
            else:
                self.ws.write(12, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def reschedule_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, u_col, 'Event Tab', self.style8)
            self.ws.write(3, u_col, 'Advance search', self.style8)
            self.ws.write(4, u_col, 'Event details', self.style8)
            self.ws.write(5, u_col, 'Event Validation', self.style8)
            self.ws.write(6, u_col, 'Floating actions', self.style8)
            self.ws.write(7, u_col, 'View Event interviews', self.style8)
            self.ws.write(8, u_col, 'Reschedule action', self.style8)
            self.ws.write(9, u_col, 'Reschedule', self.style8)
            self.ws.write(10, u_col, 'Candidate details screen', self.style8)
            self.ws.write(11, u_col, 'Applicant current status', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_r == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_r)
                self.ws.write(2, s_col, 'Pass', self.style7)
            else:
                self.ws.write(2, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_advance_search_r == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_r)
                self.ws.write(3, s_col, 'Pass', self.style7)
            else:
                self.ws.write(3, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details_r == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_r)
                self.ws.write(4, s_col, 'Pass', self.style7)
            else:
                self.ws.write(4, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation_r == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_r)
                self.ws.write(5, s_col, 'Pass', self.style7)
            else:
                self.ws.write(5, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_r == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_r)
                self.ws.write(6, s_col, 'Pass', self.style7)
            else:
                self.ws.write(6, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action)
                self.ws.write(7, s_col, 'Pass', self.style7)
            else:
                self.ws.write(7, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_grid_reschedule_action == 'Pass':
                self.Actual_success_cases.append(self.ui_grid_reschedule_action)
                self.ws.write(8, s_col, 'Pass', self.style7)
            else:
                self.ws.write(8, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_reschedule == 'Pass':
                self.Actual_success_cases.append(self.ui_reschedule)
                self.ws.write(9, s_col, 'Pass', self.style7)
            else:
                self.ws.write(9, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_getby_r == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_getby_r)
                self.ws.write(10, s_col, 'Pass', self.style7)
            else:
                self.ws.write(10, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status)
                self.ws.write(11, s_col, 'Pass', self.style7)
            else:
                self.ws.write(11, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def cancel_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, u_col, 'Cancel interview action', self.style8)
            self.ws.write(3, u_col, 'Cancel interview', self.style8)
            self.ws.write(4, u_col, 'Candidate details screen', self.style8)
            self.ws.write(5, u_col, 'Applicant current status', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_grid_cancel_action == 'Pass':
                self.Actual_success_cases.append(self.ui_grid_cancel_action)
                self.ws.write(2, s_col, 'Pass', self.style7)
            else:
                self.ws.write(2, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_cancel_interview == 'Pass':
                self.Actual_success_cases.append(self.ui_cancel_interview)
                self.ws.write(3, s_col, 'Pass', self.style7)
            else:
                self.ws.write(3, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_getby_c == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_getby_c)
                self.ws.write(4, s_col, 'Pass', self.style7)
            else:
                self.ws.write(4, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status)
                self.ws.write(5, s_col, 'Pass', self.style7)
            else:
                self.ws.write(5, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def cancel_request_raise_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, u_col, 'Event Tab', self.style8)
            self.ws.write(3, u_col, 'Advance search', self.style8)
            self.ws.write(4, u_col, 'Event details', self.style8)
            self.ws.write(5, u_col, 'Event Validation', self.style8)
            self.ws.write(6, u_col, 'Floating actions', self.style8)
            self.ws.write(7, u_col, 'View Event interviews', self.style8)
            self.ws.write(8, u_col, 'Cancel request action', self.style8)
            self.ws.write(9, u_col, 'Cancel request raise', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_cr)
                self.ws.write(2, s_col, 'Pass', self.style7)
            else:
                self.ws.write(2, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_cr)
                self.ws.write(3, s_col, 'Pass', self.style7)
            else:
                self.ws.write(3, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_cr)
                self.ws.write(4, s_col, 'Pass', self.style7)
            else:
                self.ws.write(4, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_cr)
                self.ws.write(5, s_col, 'Pass', self.style7)
            else:
                self.ws.write(5, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_cr)
                self.ws.write(6, s_col, 'Pass', self.style7)
            else:
                self.ws.write(6, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_cr == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_cr)
                self.ws.write(7, s_col, 'Pass', self.style7)
            else:
                self.ws.write(7, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_cancel_request_action == 'Pass':
                self.Actual_success_cases.append(self.ui_cancel_request_action)
                self.ws.write(8, s_col, 'Pass', self.style7)
            else:
                self.ws.write(8, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_cancel_request_raise == 'Pass':
                self.Actual_success_cases.append(self.ui_cancel_request_raise)
                self.ws.write(9, s_col, 'Pass', self.style7)
            else:
                self.ws.write(9, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def cancel_request_accept_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, u_col, 'Event Tab', self.style8)
            self.ws.write(3, u_col, 'Advance search', self.style8)
            self.ws.write(4, u_col, 'Event details', self.style8)
            self.ws.write(5, u_col, 'Event Validation', self.style8)
            self.ws.write(6, u_col, 'Tracking Tab', self.style8)
            self.ws.write(7, u_col, 'Cancel request tab', self.style8)
            self.ws.write(8, u_col, 'Request validation', self.style8)
            self.ws.write(9, u_col, 'Approve', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_cr_a == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_cr_a)
                self.ws.write(2, s_col, 'Pass', self.style7)
            else:
                self.ws.write(2, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_cr_a == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_cr_a)
                self.ws.write(3, s_col, 'Pass', self.style7)
            else:
                self.ws.write(3, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_cr_a == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_cr_a)
                self.ws.write(4, s_col, 'Pass', self.style7)
            else:
                self.ws.write(4, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_cr_a == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_cr_a)
                self.ws.write(5, s_col, 'Pass', self.style7)
            else:
                self.ws.write(5, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_tracking_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_tracking_tab)
                self.ws.write(6, s_col, 'Pass', self.style7)
            else:
                self.ws.write(6, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_cancel_request_sub_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_cancel_request_sub_tab)
                self.ws.write(7, s_col, 'Pass', self.style7)
            else:
                self.ws.write(7, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_request_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_request_validation)
                self.ws.write(8, s_col, 'Pass', self.style7)
            else:
                self.ws.write(8, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_approve == 'Pass':
                self.Actual_success_cases.append(self.ui_approve)
                self.ws.write(9, s_col, 'Pass', self.style7)
            else:
                self.ws.write(9, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def save_draft_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Event Tab', self.style8)
            self.ws.write(16, u_col, 'Advance search', self.style8)
            self.ws.write(17, u_col, 'Event details', self.style8)
            self.ws.write(18, u_col, 'Event Validation', self.style8)
            self.ws.write(19, u_col, 'Floating action', self.style8)
            self.ws.write(20, u_col, 'View Event interviews', self.style8)
            self.ws.write(21, u_col, 'Provide Feedback action', self.style8)
            self.ws.write(22, u_col, 'Save draft', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_d == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_d)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_d == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_d)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_d == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_d)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_d == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_d)
                self.ws.write(18, s_col, 'Pass', self.style7)
            else:
                self.ws.write(18, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_d == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_d)
                self.ws.write(19, s_col, 'Pass', self.style7)
            else:
                self.ws.write(19, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_d == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_d)
                self.ws.write(20, s_col, 'Pass', self.style7)
            else:
                self.ws.write(20, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_d == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_d)
                self.ws.write(21, s_col, 'Pass', self.style7)
            else:
                self.ws.write(21, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_save_draft == 'Pass':
                self.Actual_success_cases.append(self.ui_save_draft)
                self.ws.write(22, s_col, 'Pass', self.style7)
            else:
                self.ws.write(22, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def partial_feedback_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Provide Feedback action', self.style8)
            self.ws.write(16, u_col, 'Partial submission', self.style8)
            self.ws.write(17, u_col, 'Draft validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_p == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_p)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_partial_submission == 'Pass':
                self.Actual_success_cases.append(self.ui_partial_submission)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_draft_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_draft_validation)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def partial_to_full_feedback_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Partial Bucket', self.style8)
            self.ws.write(16, u_col, 'Provide Feedback action', self.style8)
            self.ws.write(17, u_col, 'Submit Feedback', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_partial_bucket == 'Pass':
                self.Actual_success_cases.append(self.ui_partial_bucket)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_p_f == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_p_f)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_feedback_p_f == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_p_f)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def submit_feedback_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Event Tab', self.style8)
            self.ws.write(16, u_col, 'Advance search', self.style8)
            self.ws.write(17, u_col, 'Event details', self.style8)
            self.ws.write(18, u_col, 'Event Validation', self.style8)
            self.ws.write(19, u_col, 'Floating actions', self.style8)
            self.ws.write(20, u_col, 'View Event interviews', self.style8)
            self.ws.write(21, u_col, 'Provide feedback action', self.style8)
            self.ws.write(22, u_col, 'Submit feedback', self.style8)
            self.ws.write(23, u_col, 'Completed bucket', self.style8)
            self.ws.write(24, u_col, 'Candidate details', self.style8)
            self.ws.write(25, u_col, 'Current status', self.style8)
            self.ws.write(26, u_col, 'Submit validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_su == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_su)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_advance_search_su == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_su)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details_su == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_su)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation_su == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_su)
                self.ws.write(18, s_col, 'Pass', self.style7)
            else:
                self.ws.write(18, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_su == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_su)
                self.ws.write(19, s_col, 'Pass', self.style7)
            else:
                self.ws.write(19, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_su == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_su)
                self.ws.write(20, s_col, 'Pass', self.style7)
            else:
                self.ws.write(20, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_su == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_su)
                self.ws.write(21, s_col, 'Pass', self.style7)
            else:
                self.ws.write(21, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_feedback_su == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_su)
                self.ws.write(22, s_col, 'Pass', self.style7)
            else:
                self.ws.write(22, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_completed_bucket_su == 'Pass':
                self.Actual_success_cases.append(self.ui_completed_bucket_su)
                self.ws.write(23, s_col, 'Pass', self.style7)
            else:
                self.ws.write(23, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_getby == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_getby)
                self.ws.write(24, s_col, 'Pass', self.style7)
            else:
                self.ws.write(24, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status_su == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status_su)
                self.ws.write(25, s_col, 'Pass', self.style7)
            else:
                self.ws.write(25, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submitted_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_submitted_validation)
                self.ws.write(26, s_col, 'Pass', self.style7)
            else:
                self.ws.write(26, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def unlock_feedback_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Event Tab', self.style8)
            self.ws.write(16, u_col, 'Advance search', self.style8)
            self.ws.write(17, u_col, 'Event details', self.style8)
            self.ws.write(18, u_col, 'Event Validation', self.style8)
            self.ws.write(19, u_col, 'Floating actions', self.style8)
            self.ws.write(20, u_col, 'View Event interviews', self.style8)
            self.ws.write(21, u_col, 'All interviews bucket', self.style8)
            self.ws.write(22, u_col, 'Completed bucket', self.style8)
            self.ws.write(23, u_col, 'Unlock feedback action', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_un == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_un)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_advance_search_un == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_un)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details_un == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_un)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation_un == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_un)
                self.ws.write(18, s_col, 'Pass', self.style7)
            else:
                self.ws.write(18, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_un == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_un)
                self.ws.write(19, s_col, 'Pass', self.style7)
            else:
                self.ws.write(19, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_un == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_un)
                self.ws.write(20, s_col, 'Pass', self.style7)
            else:
                self.ws.write(20, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_all_interviews_bucket_un == 'Pass':
                self.Actual_success_cases.append(self.ui_all_interviews_bucket_un)
                self.ws.write(21, s_col, 'Pass', self.style7)
            else:
                self.ws.write(21, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_all_completed_bucket_un == 'Pass':
                self.Actual_success_cases.append(self.ui_all_completed_bucket_un)
                self.ws.write(22, s_col, 'Pass', self.style7)
            else:
                self.ws.write(22, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_unlock_feedback_action == 'Pass':
                self.Actual_success_cases.append(self.ui_unlock_feedback_action)
                self.ws.write(23, s_col, 'Pass', self.style7)
            else:
                self.ws.write(23, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def update_decision_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Completed Interviews', self.style8)
            self.ws.write(16, u_col, 'Provide feedback action', self.style8)
            self.ws.write(17, u_col, 'Submitted feedback', self.style8)
            self.ws.write(18, u_col, 'Update decision', self.style8)
            self.ws.write(19, u_col, 'Update decision validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_completed_interviews_bucket_ud == 'Pass':
                self.Actual_success_cases.append(self.ui_completed_interviews_bucket_ud)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_provide_feedback_action_ud == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_ud)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_submit_feedback_ud == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_ud)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_update_decision == 'Pass':
                self.Actual_success_cases.append(self.ui_update_decision)
                self.ws.write(18, s_col, 'Pass', self.style7)
            else:
                self.ws.write(18, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_decision_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_decision_validation)
                self.ws.write(19, s_col, 'Pass', self.style7)
            else:
                self.ws.write(19, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def update_feedback_output_report(self, u_col, s_col):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(15, u_col, 'Completed Interviews', self.style8)
            self.ws.write(16, u_col, 'Provide feedback action', self.style8)
            self.ws.write(17, u_col, 'Submitted feedback', self.style8)
            self.ws.write(18, u_col, 'Update feedback', self.style8)
            self.ws.write(19, u_col, 'Update feedback validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_completed_interviews_bucket_uf == 'Pass':
                self.Actual_success_cases.append(self.ui_completed_interviews_bucket_uf)
                self.ws.write(15, s_col, 'Pass', self.style7)
            else:
                self.ws.write(15, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_provide_feedback_action_uf == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_uf)
                self.ws.write(16, s_col, 'Pass', self.style7)
            else:
                self.ws.write(16, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_submit_feedback_uf == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_uf)
                self.ws.write(17, s_col, 'Pass', self.style7)
            else:
                self.ws.write(17, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_update_feedback == 'Pass':
                self.Actual_success_cases.append(self.ui_update_feedback)
                self.ws.write(18, s_col, 'Pass', self.style7)
            else:
                self.ws.write(18, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_feedback_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_feedback_validation)
                self.ws.write(19, s_col, 'Pass', self.style7)
            else:
                self.ws.write(19, s_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'OLD INTERVIEW FLOW', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['old_int_report'])

        except Exception as error:
            ui_logger.error(error)
