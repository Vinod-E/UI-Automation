import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.quick_interview_flow import interviewer_submit_feedback


class QuickInterviewOutputFile(styles.FontColor, interviewer_submit_feedback.InterviewFeedbackSubmit):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 31)))
        self.Actual_success_cases = []

        super(QuickInterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.event_sc_col = 0
        self.event_st_col = 1
        self.q_int1_sc_col = 2
        self.q_int1_st_col = 3
        self.q_int2_sc_col = 4
        self.q_int2_st_col = 5

        index = 0
        excelheaders = ['Schedule-Admin', 'Status', 'Interviewer_One', 'Status', 'Interviewer_Two', 'Status']
        for headers in excelheaders:
            if headers in ['Schedule-Admin', 'Interviewer_One', 'Interviewer_Two', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def quick_schedule_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.event_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.event_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.event_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.event_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.event_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.event_sc_col, 'View applicant', self.style8)
            self.ws.write(8, self.event_sc_col, 'Applicant advance search', self.style8)
            self.ws.write(9, self.event_sc_col, 'More Button action', self.style8)
            self.ws.write(10, self.event_sc_col, 'Quick Interview action', self.style8)
            self.ws.write(11, self.event_sc_col, 'Candidate details screen', self.style8)
            self.ws.write(12, self.event_sc_col, 'Applicant current status', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_q == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_q)
                self.ws.write(2, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_q == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_q)
                self.ws.write(3, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details_q == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_q)
                self.ws.write(4, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation_q == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_q)
                self.ws.write(5, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_q == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_q)
                self.ws.write(6, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_applicant_action_q == 'Pass':
                self.Actual_success_cases.append(self.ui_event_applicant_action_q)
                self.ws.write(7, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_advance_search_q == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_advance_search_q)
                self.ws.write(8, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_more_button_q == 'Pass':
                self.Actual_success_cases.append(self.ui_more_button_q)
                self.ws.write(9, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_quick_interview_action == 'Pass':
                self.Actual_success_cases.append(self.ui_quick_interview_action)
                self.ws.write(10, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.event_st_col, 'Fail', self.style3)
            # -----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_getby_q == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_getby_q)
                self.ws.write(11, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status_q == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status_q)
                self.ws.write(12, self.event_st_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.event_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['quick_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def quick_int1_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.q_int1_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.q_int1_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.q_int1_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.q_int1_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.q_int1_sc_col, 'Floating action', self.style8)
            self.ws.write(7, self.q_int1_sc_col, 'View Event interviews', self.style8)
            self.ws.write(8, self.q_int1_sc_col, 'Provide Feedback action', self.style8)
            self.ws.write(9, self.q_int1_sc_col, 'Submit feedback', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_q_int1)
                self.ws.write(2, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_q_int1)
                self.ws.write(3, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_q_int1)
                self.ws.write(4, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_q_int1)
                self.ws.write(5, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_q_int1)
                self.ws.write(6, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_q_int1)
                self.ws.write(7, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_q_int1)
                self.ws.write(8, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_feedback_q_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_q_int1)
                self.ws.write(9, self.q_int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.q_int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['quick_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def quick_int2_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.q_int2_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.q_int2_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.q_int2_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.q_int2_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.q_int2_sc_col, 'Floating action', self.style8)
            self.ws.write(7, self.q_int2_sc_col, 'View Event interviews', self.style8)
            self.ws.write(8, self.q_int2_sc_col, 'Provide Feedback action', self.style8)
            self.ws.write(9, self.q_int2_sc_col, 'Submit feedback', self.style8)
            self.ws.write(10, self.q_int2_sc_col, 'Completed Bucket', self.style8)
            self.ws.write(11, self.q_int2_sc_col, 'Applicant_details', self.style8)
            self.ws.write(12, self.q_int2_sc_col, 'Applicant Status', self.style8)
            self.ws.write(13, self.q_int2_sc_col, 'Submit validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_q_int2)
                self.ws.write(2, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_q_int2)
                self.ws.write(3, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_q_int2)
                self.ws.write(4, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_q_int2)
                self.ws.write(5, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_q_int2)
                self.ws.write(6, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_q_int2)
                self.ws.write(7, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_q_int2)
                self.ws.write(8, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_feedback_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_q_int2)
                self.ws.write(9, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_completed_bucket_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_completed_bucket_q_int2)
                self.ws.write(10, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_getby_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_getby_q_int2)
                self.ws.write(11, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status_q_int2)
                self.ws.write(12, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submitted_validation_q_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_submitted_validation_q_int2)
                self.ws.write(13, self.q_int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(13, self.q_int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['quick_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'QUICK INTERVIEW FLOW', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['quick_int_report'])

        except Exception as error:
            ui_logger.error(error)
