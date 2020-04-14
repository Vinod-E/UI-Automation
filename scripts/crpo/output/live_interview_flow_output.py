import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.live_interview_flow import submit_feedback_live_int2


class LiveInterviewOutputFile(styles.FontColor, submit_feedback_live_int2.SubmitFeedback):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 33)))
        self.Actual_success_cases = []

        super(LiveInterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.live_sc_col = 0
        self.live_st_col = 1
        self.behalf_sc_col = 2
        self.behalf_st_col = 3
        self.int1_sc_col = 4
        self.int1_st_col = 5
        self.int2_sc_col = 6
        self.int2_st_col = 7

        index = 0
        excelheaders = ['LiveSchedule-Admin', 'Status', 'Behalf_Feedback-Admin', 'Status', 'SubmitFeedback-Int1',
                        'Status', 'SubmitFeedback-Int2', 'Status']
        for headers in excelheaders:
            if headers in ['LiveSchedule-Admin', 'Behalf_Feedback-Admin', 'SubmitFeedback-Int1',
                           'SubmitFeedback-Int2', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def live_schedule_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.live_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.live_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.live_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.live_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.live_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.live_sc_col, 'Live Interview action', self.style8)
            self.ws.write(8, self.live_sc_col, 'Live interview validation', self.style8)
            self.ws.write(9, self.live_sc_col, 'Live schedule', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_li == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_li)
                self.ws.write(2, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_li == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_li)
                self.ws.write(3, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_li == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_li)
                self.ws.write(4, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_li == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_li)
                self.ws.write(5, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_li == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_li)
                self.ws.write(6, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interviews_action_li == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interviews_action_li)
                self.ws.write(7, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interview_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interview_validation)
                self.ws.write(8, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_schedule == 'Pass':
                self.Actual_success_cases.append(self.ui_live_schedule)
                self.ws.write(9, self.live_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.live_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['live_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def behalf_of_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.behalf_sc_col, 'Provide feedback', self.style8)
            self.ws.write(3, self.behalf_sc_col, 'Behalf choose', self.style8)
            self.ws.write(4, self.behalf_sc_col, 'Submit feedback', self.style8)
            self.ws.write(5, self.behalf_sc_col, 'Submit validation', self.style8)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_button == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_button)
                self.ws.write(2, self.behalf_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.behalf_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_behalf_choose == 'Pass':
                self.Actual_success_cases.append(self.ui_behalf_choose)
                self.ws.write(3, self.behalf_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.behalf_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.live_provide_feedback_submitted == 'Pass':
                self.Actual_success_cases.append(self.live_provide_feedback_submitted)
                self.ws.write(4, self.behalf_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.behalf_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.live_submit_validation == 'Pass':
                self.Actual_success_cases.append(self.live_submit_validation)
                self.ws.write(5, self.behalf_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.behalf_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['live_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def submit_int1_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.int1_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.int1_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.int1_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.int1_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.int1_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.int1_sc_col, 'Live Interview action', self.style8)
            self.ws.write(8, self.int1_sc_col, 'Live interview validation', self.style8)
            self.ws.write(9, self.int1_sc_col, 'Live schedule', self.style8)
            self.ws.write(10, self.int1_sc_col, 'Provide feedback', self.style8)
            self.ws.write(11, self.int1_sc_col, 'Submit feedback', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_int1)
                self.ws.write(2, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_int1)
                self.ws.write(3, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_int1)
                self.ws.write(4, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_int1)
                self.ws.write(5, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_int1)
                self.ws.write(6, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interviews_action_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interviews_action_int1)
                self.ws.write(7, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interview_validation_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interview_validation_int1)
                self.ws.write(8, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_schedule_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_schedule_int1)
                self.ws.write(9, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_button_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_button_int1)
                self.ws.write(10, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_submitted_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_submitted_int1)
                self.ws.write(11, self.int1_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.int1_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['live_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def submit_int2_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.int2_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.int2_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.int2_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.int2_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.int2_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.int2_sc_col, 'Live Interview action', self.style8)
            self.ws.write(8, self.int2_sc_col, 'Live interview validation', self.style8)
            self.ws.write(9, self.int2_sc_col, 'Live schedule', self.style8)
            self.ws.write(10, self.int2_sc_col, 'Provide feedback', self.style8)
            self.ws.write(11, self.int2_sc_col, 'Submit feedback', self.style8)
            self.ws.write(12, self.int2_sc_col, 'Submit validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_int2)
                self.ws.write(2, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_int2)
                self.ws.write(3, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_int2)
                self.ws.write(4, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_int2)
                self.ws.write(5, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_int2)
                self.ws.write(6, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interviews_action_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interviews_action_int2)
                self.ws.write(7, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_interview_validation_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_interview_validation_int2)
                self.ws.write(8, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_live_schedule_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_live_schedule_int2)
                self.ws.write(9, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_button_int2 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_button_int2)
                self.ws.write(10, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.live_provide_feedback_submitted_int2 == 'Pass':
                self.Actual_success_cases.append(self.live_provide_feedback_submitted_int2)
                self.ws.write(11, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.live_submit_validation_int2 == 'Pass':
                self.Actual_success_cases.append(self.live_submit_validation_int2)
                self.ws.write(12, self.int2_st_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.int2_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['live_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'LIVE INTERVIEW FLOW', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['live_int_report'])

        except Exception as error:
            ui_logger.error(error)
