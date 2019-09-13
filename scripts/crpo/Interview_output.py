import xlwt
import Live_interview
from datetime import date
import styles
import test_data_inputpath


class InterviewOutputFile(styles.FontColor, Live_interview.LiveInterview):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 52)))
        self.Actual_success_cases = []

        super(InterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.user_usecase_col = 0
        self.user_status_col = 1
        self.PF_usecase_col = 2
        self.PF_status_col = 3
        self.UF_usecase_col = 4
        self.UF_status_col = 5
        self.live_usecase_col = 6
        self.live_status_col = 7

        index = 0
        excelheaders = ['Users', 'Status', 'Provide Feedback', 'Status', 'Update Feedback', 'Status', 'Live Interview'
                        , 'Status']
        for headers in excelheaders:
            if headers in ['Users', 'Provide Feedback', 'Update Feedback', 'Live Interview', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def admin_output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  Job Use cases -------------------
        self.ws.write(2, self.user_usecase_col, 'Admin', self.style9)
        self.ws.write(3, self.user_usecase_col, 'Event advance search', self.style8)
        self.ws.write(4, self.user_usecase_col, 'Event floating action', self.style8)
        self.ws.write(5, self.user_usecase_col, 'View Event applicant', self.style8)
        self.ws.write(6, self.user_usecase_col, 'Event applicant search', self.style8)
        self.ws.write(7, self.user_usecase_col, 'Change applicant status', self.style8)
        self.ws.write(8, self.user_usecase_col, 'Schedule', self.style8)
        self.ws.write(9, self.user_usecase_col, 'Cancel Request Approved', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_search_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_search_o)
            self.ws.write(3, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_floating_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_floating_action_o)
            self.ws.write(4, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_applicant_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicant_action_o)
            self.ws.write(5, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_applicant_search_o == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_search_o)
            self.ws.write(6, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_change_applicant_status_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_change_applicant_status_action_o)
            self.ws.write(7, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_applicant_schedule_o == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_schedule_o)
            self.ws.write(8, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_approve_cancel_request_o == 'Pass':
            self.Actual_success_cases.append(self.ui_approve_cancel_request_o)
            self.ws.write(9, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def int1_output_report(self):
        # ------------  Requirement Use cases -------------------
        self.ws.write(10, self.user_usecase_col, 'Interviewer_1', self.style9)
        self.ws.write(11, self.user_usecase_col, 'Interviewer Login', self.style8)
        self.ws.write(12, self.user_usecase_col, 'Event getby Id', self.style8)
        self.ws.write(13, self.user_usecase_col, 'Event floating action', self.style8)
        self.ws.write(14, self.user_usecase_col, 'Event interviews', self.style8)
        self.ws.write(15, self.user_usecase_col, 'Reschedule action', self.style8)
        self.ws.write(16, self.user_usecase_col, 'Rescheduled', self.style8)
        self.ws.write(17, self.user_usecase_col, 'Cancel Interview', self.style8)

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_int1_login_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_o)
            self.ws.write(11, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_getby_id_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getby_id_o)
            self.ws.write(12, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_float_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_float_o)
            self.ws.write(13, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_interviews_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_interviews_o)
            self.ws.write(14, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(14, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_reschedule_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_reschedule_action_o)
            self.ws.write(15, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(15, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_rescheduled_o == 'Pass':
            self.Actual_success_cases.append(self.ui_rescheduled_o)
            self.ws.write(16, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(16, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_cancel_interview_o == 'Pass':
            self.Actual_success_cases.append(self.ui_cancel_interview_o)
            self.ws.write(17, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(17, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def int2_output_report(self):
        # ------------- Test Use cases -------------------
        self.ws.write(18, self.user_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(19, self.user_usecase_col, 'Interviewer Login', self.style8)
        self.ws.write(20, self.user_usecase_col, 'Event getby Id', self.style8)
        self.ws.write(21, self.user_usecase_col, 'Event floating action', self.style8)
        self.ws.write(22, self.user_usecase_col, 'Event interviews', self.style8)
        self.ws.write(23, self.user_usecase_col, 'Cancel Request action', self.style8)
        self.ws.write(24, self.user_usecase_col, 'Cancel Request Raise', self.style8)
        self.ws.write(25, self.user_usecase_col, 'Cancel Interview', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_int2_login_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_login_o)
            self.ws.write(19, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(19, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_getby_id__int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getby_id__int2_o)
            self.ws.write(20, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(20, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_float_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_float_int2_o)
            self.ws.write(21, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(21, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_interviews_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_interviews_int2_o)
            self.ws.write(22, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(22, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_cancel_interview_request_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_cancel_interview_request_action_o)
            self.ws.write(23, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(23, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_cancel_interview_request_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_cancel_interview_request_int2_o)
            self.ws.write(24, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(24, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_cancel_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_cancel_int2_o)
            self.ws.write(25, self.user_status_col, 'Pass', self.style7)
        else:
            self.ws.write(25, self.user_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def provide_feedback_output_report(self):
        # ------------- Test Use cases -------------------
        self.ws.write(2, self.PF_usecase_col, 'Interviewer_1', self.style9)
        self.ws.write(3, self.PF_usecase_col, 'Interviewer_1 Login', self.style8)
        self.ws.write(4, self.PF_usecase_col, 'Provide Feedback action', self.style8)
        self.ws.write(5, self.PF_usecase_col, 'Provide Feedback screen', self.style8)
        self.ws.write(6, self.PF_usecase_col, 'Int_1 Decision-MayBe', self.style8)
        self.ws.write(7, self.PF_usecase_col, 'Save Draft', self.style8)
        self.ws.write(8, self.PF_usecase_col, 'Partial submitted', self.style8)
        self.ws.write(9, self.PF_usecase_col, 'Partial bucket', self.style8)
        self.ws.write(10, self.PF_usecase_col, 'Feedback submitted from Partial bucket', self.style8)

        self.ws.write(11, self.PF_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(12, self.PF_usecase_col, 'Interviewer_2 Login', self.style8)
        self.ws.write(13, self.PF_usecase_col, 'Provide Feedback action', self.style8)
        self.ws.write(14, self.PF_usecase_col, 'Provide Feedback screen', self.style8)
        self.ws.write(15, self.PF_usecase_col, 'Int_2 Decision-MayBe', self.style8)
        self.ws.write(16, self.PF_usecase_col, 'Submit Feedback', self.style8)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_PF_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_PF_o)
            self.ws.write(3, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_feedback_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_feedback_action_o)
            self.ws.write(4, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_feedback_screen_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_feedback_screen_o)
            self.ws.write(5, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_decision_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_decision_o)
            self.ws.write(6, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_saveasdraft_o == 'Pass':
            self.Actual_success_cases.append(self.ui_saveasdraft_o)
            self.ws.write(7, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_partial_submit_o == 'Pass':
            self.Actual_success_cases.append(self.ui_partial_submit_o)
            self.ws.write(8, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_partial_submit_bucket_o == 'Pass':
            self.Actual_success_cases.append(self.ui_partial_submit_bucket_o)
            self.ws.write(9, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_from_partial_bucket_submit_feedback_o == 'Pass':
            self.Actual_success_cases.append(self.ui_from_partial_bucket_submit_feedback_o)
            self.ws.write(10, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_login_PF_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_login_PF_o)
            self.ws.write(12, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_feedback_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_feedback_action_o)
            self.ws.write(13, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_feedback_screen_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_feedback_screen_o)
            self.ws.write(14, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(14, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_decision_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_decision_o)
            self.ws.write(15, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(15, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_submit_feedback_o == 'Pass':
            self.Actual_success_cases.append(self.ui_submit_feedback_o)
            self.ws.write(16, self.PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(16, self.PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def update_feedback_output_report(self):
        # ------------- Update Feedback cases -------------------
        self.ws.write(2, self.UF_usecase_col, 'Admin', self.style9)
        self.ws.write(3, self.UF_usecase_col, 'All interviews', self.style8)
        self.ws.write(4, self.UF_usecase_col, 'Completed Feedback', self.style8)
        self.ws.write(5, self.UF_usecase_col, 'Unlock Feedback action', self.style8)
        self.ws.write(6, self.UF_usecase_col, 'Unlocked Feedback', self.style8)
        self.ws.write(7, self.UF_usecase_col, 'Interviewer_1', self.style9)
        self.ws.write(8, self.UF_usecase_col, 'Update decision', self.style8)
        self.ws.write(9, self.UF_usecase_col, 'Update Feedback', self.style8)
        self.ws.write(10, self.UF_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(11, self.UF_usecase_col, 'Update decision', self.style8)
        self.ws.write(12, self.UF_usecase_col, 'Update Feedback', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_all_interviews_bucket_o == 'Pass':
            self.Actual_success_cases.append(self.ui_all_interviews_bucket_o)
            self.ws.write(self.rowsize, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_completed_interview_bucket_o == 'Pass':
            self.Actual_success_cases.append(self.ui_completed_interview_bucket_o)
            self.ws.write(4, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_unlock_feedback_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_unlock_feedback_action_o)
            self.ws.write(5, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_unlock_feedback_o == 'Pass':
            self.Actual_success_cases.append(self.ui_unlock_feedback_o)
            self.ws.write(6, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_update_decision_int1_o == 'Pass':
            self.Actual_success_cases.append(self.ui_update_decision_int1_o)
            self.ws.write(8, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_update_feedback_int1_o == 'Pass':
            self.Actual_success_cases.append(self.ui_update_feedback_int1_o)
            self.ws.write(9, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_update_decision_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_update_decision_int2_o)
            self.ws.write(11, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_update_feedback_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_update_feedback_int2_o)
            self.ws.write(12, self.UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def live_interview_output_report(self):
        # ------------- Live interview cases -------------------
        self.ws.write(2, self.live_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(3, self.live_usecase_col, 'Event getByid', self.style8)
        self.ws.write(4, self.live_usecase_col, 'Live interview action', self.style8)
        self.ws.write(5, self.live_usecase_col, 'Interview stage', self.style8)
        self.ws.write(6, self.live_usecase_col, 'Advance search', self.style8)
        self.ws.write(7, self.live_usecase_col, 'Schedule', self.style8)
        self.ws.write(8, self.live_usecase_col, 'candidate schedule details', self.style8)
        self.ws.write(9, self.live_usecase_col, 'Provide feedback action', self.style8)
        self.ws.write(10, self.live_usecase_col, 'Interviewer decision - Shortlist', self.style8)
        self.ws.write(11, self.live_usecase_col, 'provide feedback screen', self.style8)
        self.ws.write(12, self.live_usecase_col, 'Submit feedback', self.style8)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_getby_id_l == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getby_id_l)
            self.ws.write(self.rowsize, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_action_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_action_l)
            self.ws.write(4, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_stage_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_stage_l)
            self.ws.write(5, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_advance_search_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_advance_search_l)
            self.ws.write(6, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_schedule_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_schedule_l)
            self.ws.write(7, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_candidate_details_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_candidate_details_l)
            self.ws.write(8, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_interview_PF_action_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_interview_PF_action_l)
            self.ws.write(9, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_decision_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_decision_l)
            self.ws.write(10, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_feedback_screen_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_feedback_screen_l)
            self.ws.write(11, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_live_submit_feedback_l == 'Pass':
            self.Actual_success_cases.append(self.ui_live_submit_feedback_l)
            self.ws.write(12, self.live_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.live_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def overall_status(self):
        self.ws.write(0, 0, 'Old Interview Flow', self.style4)
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
        self.ws.write(0, 8, 'No.of Use Cases', self.style4)
        self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])
