import xlwt
import styles
from datetime import date
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import submit_feedback_int2


class NewInterviewOutputFile(styles.FontColor, submit_feedback_int2.SubmitFeedbackInt2):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 42)))
        self.Actual_success_cases = []

        super(NewInterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.settings_sc_col = 0
        self.settings_st_col = 1
        self.feed_sc_col = 2
        self.feed_st_col = 3
        self.sc_sc_col = 4
        self.sc_st_col = 5
        self.draft_sc = 6
        self.draft_st = 7
        self.s_int1_sc = 8
        self.s_int1_st = 9
        self.s_int2_sc = 10
        self.s_int2_st = 11

        index = 0
        excelheaders = ['Settings-Admin', 'Status', 'FeedbackForm-Admin', 'Status', 'Schedule-Admin', 'Status',
                        'SaveDraft-Int1', 'Status', 'SubmitFeedback-Int1', 'Status', 'SubmitFeedback-Int2', 'Status']
        for headers in excelheaders:
            if headers in ['Settings-Admin', 'Schedule-Admin', 'SaveDraft-Int1', 'SubmitFeedback-Int1',
                           'FeedbackForm-Admin', 'SubmitFeedback-Int2', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def settings_on_off_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.settings_sc_col, 'Common Settings', self.style8)
            self.ws.write(3, self.settings_sc_col, 'Settings', self.style8)
            self.ws.write(4, self.settings_sc_col, 'Interview Module', self.style8)
            self.ws.write(5, self.settings_sc_col, 'Enable-New_Form', self.style8)
            self.ws.write(6, self.settings_sc_col, 'Disable-New_Form', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_common_settings == 'Pass':
                self.Actual_success_cases.append(self.ui_common_settings)
                self.ws.write(2, self.settings_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.settings_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_settings == 'Pass':
                self.Actual_success_cases.append(self.ui_settings)
                self.ws.write(3, self.settings_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.settings_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.interview_module == 'Pass':
                self.Actual_success_cases.append(self.interview_module)
                self.ws.write(4, self.settings_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.settings_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_new_feedback_enable == 'Pass':
                self.Actual_success_cases.append(self.ui_new_feedback_enable)
                self.ws.write(5, self.settings_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.settings_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_new_feedback_disable == 'Pass':
                self.Actual_success_cases.append(self.ui_new_feedback_disable)
                self.ws.write(6, self.settings_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.settings_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def new_feedback_form_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.feed_sc_col, 'Job Tab', self.style8)
            self.ws.write(3, self.feed_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.feed_sc_col, 'Job details', self.style8)
            self.ws.write(5, self.feed_sc_col, 'Job validation', self.style8)
            self.ws.write(6, self.feed_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.feed_sc_col, 'Configure feedback action', self.style8)
            self.ws.write(8, self.feed_sc_col, 'Feedback form search', self.style8)
            self.ws.write(9, self.feed_sc_col, 'Feedback form validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_job_tab)
                self.ws.write(2, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_advance_search_n == 'Pass':
                self.Actual_success_cases.append(self.ui_job_advance_search_n)
                self.ws.write(3, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_getbyid_n == 'Pass':
                self.Actual_success_cases.append(self.ui_job_getbyid_n)
                self.ws.write(4, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_validation_n == 'Pass':
                self.Actual_success_cases.append(self.ui_job_validation_n)
                self.ws.write(5, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_n)
                self.ws.write(6, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_feedback_form_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_feedback_form_action_n)
                self.ws.write(7, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_feedback_form_search == 'Pass':
                self.Actual_success_cases.append(self.ui_feedback_form_search)
                self.ws.write(8, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_feedback_form_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_feedback_form_validation)
                self.ws.write(9, self.feed_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.feed_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def new_form_schedule_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.sc_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.sc_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.sc_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.sc_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.sc_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.sc_sc_col, 'View applicant', self.style8)
            self.ws.write(8, self.sc_sc_col, 'Applicant advance search', self.style8)
            self.ws.write(9, self.sc_sc_col, 'Change status action', self.style8)
            self.ws.write(10, self.sc_sc_col, 'Change applicant status', self.style8)
            self.ws.write(11, self.sc_sc_col, 'Candidate details screen', self.style8)
            self.ws.write(12, self.sc_sc_col, 'Applicant current status', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_n)
                self.ws.write(2, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_n == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_n)
                self.ws.write(3, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_details_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_n)
                self.ws.write(4, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_validation_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_n)
                self.ws.write(5, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_n)
                self.ws.write(6, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_applicant_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_applicant_action_n)
                self.ws.write(7, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_advance_search_n == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_advance_search_n)
                self.ws.write(8, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status_action_n)
                self.ws.write(9, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_change_applicant_status_n == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status_n)
                self.ws.write(10, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.sc_st_col, 'Fail', self.style3)
            # -----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_getby_n == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_getby_n)
                self.ws.write(11, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_applicant_current_status_n == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status_n)
                self.ws.write(12, self.sc_st_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.sc_st_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def new_save_draft_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.draft_sc, 'Event Tab', self.style8)
            self.ws.write(3, self.draft_sc, 'Advance search', self.style8)
            self.ws.write(4, self.draft_sc, 'Event details', self.style8)
            self.ws.write(5, self.draft_sc, 'Event Validation', self.style8)
            self.ws.write(6, self.draft_sc, 'Floating actions', self.style8)
            self.ws.write(7, self.draft_sc, 'View Event interviews', self.style8)
            self.ws.write(8, self.draft_sc, 'Provide Feedback action', self.style8)
            self.ws.write(9, self.draft_sc, 'Save draft', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_n)
                self.ws.write(2, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(2, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_n == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_n)
                self.ws.write(3, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(3, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_n)
                self.ws.write(4, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(4, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_n)
                self.ws.write(5, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(5, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_n)
                self.ws.write(6, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(6, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_n)
                self.ws.write(7, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(7, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_n)
                self.ws.write(8, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(8, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_save_draft_n == 'Pass':
                self.Actual_success_cases.append(self.ui_save_draft_n)
                self.ws.write(9, self.draft_st, 'Pass', self.style7)
            else:
                self.ws.write(9, self.draft_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def submit_feedback_one_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.s_int1_sc, 'Provide Feedback action', self.style8)
            self.ws.write(3, self.s_int1_sc, 'Submitted', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_n_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_n_int1)
                self.ws.write(2, self.s_int1_st, 'Pass', self.style7)
            else:
                self.ws.write(2, self.s_int1_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_feedback_new_int1 == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_feedback_new_int1)
                self.ws.write(3, self.s_int1_st, 'Pass', self.style7)
            else:
                self.ws.write(3, self.s_int1_st, 'SaveDraft Failed', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def submit_feedback_two_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.s_int2_sc, 'Event Tab', self.style8)
            self.ws.write(3, self.s_int2_sc, 'Advance search', self.style8)
            self.ws.write(4, self.s_int2_sc, 'Event details', self.style8)
            self.ws.write(5, self.s_int2_sc, 'Event Validation', self.style8)
            self.ws.write(6, self.s_int2_sc, 'Floating actions', self.style8)
            self.ws.write(7, self.s_int2_sc, 'View Event interviews', self.style8)
            self.ws.write(8, self.s_int2_sc, 'Provide Feedback action', self.style8)
            self.ws.write(9, self.s_int2_sc, 'Submitted', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_tab_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_tab_n)
                self.ws.write(2, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(2, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_advance_search_n == 'Pass':
                self.Actual_success_cases.append(self.ui_advance_search_n)
                self.ws.write(3, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(3, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_details_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_details_n)
                self.ws.write(4, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(4, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_validation_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_validation_n)
                self.ws.write(5, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(5, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_floating_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_floating_action_n)
                self.ws.write(6, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(6, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_interviews_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_event_interviews_action_n)
                self.ws.write(7, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(7, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_provide_feedback_action_n == 'Pass':
                self.Actual_success_cases.append(self.ui_provide_feedback_action_n)
                self.ws.write(8, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(8, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_save_draft_n == 'Pass':
                self.Actual_success_cases.append(self.ui_save_draft_n)
                self.ws.write(9, self.s_int2_st, 'Pass', self.style7)
            else:
                self.ws.write(9, self.s_int2_st, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])
        except Exception as error:
            api_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)

            self.ws.write(0, 0, 'NEW INTERVIEW FLOW USECASES', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['new_int_report'])

        except Exception as error:
            api_logger.error(error)
