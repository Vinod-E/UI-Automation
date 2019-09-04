import xlwt
import cancel_interview
from datetime import date
import styles
import test_data_inputpath


class InterviewOutputFile(styles.FontColor, cancel_interview.CancelAndRequest):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 18)))
        self.Actual_success_cases = []

        super(InterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 2
        self.size = self.rowsize
        self.admin_usecase_col = 0
        self.admin_status_col = 1
        self.int1_usecase_col = 2
        self.int1_status_col = 3
        self.int2_usecase_col = 4
        self.int2_status_col = 5

        index = 0
        excelheaders = ['Admin', 'Status', 'Interviewer 1', 'Status', 'Interviewer 2', 'Status']
        for headers in excelheaders:
            if headers in ['Admin', 'Status', 'Interviewer 1', 'Status', 'Interviewer 2', 'Status']:
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
        self.ws.write(2, self.admin_usecase_col, 'Event advance search', self.style8)
        self.ws.write(3, self.admin_usecase_col, 'Event floating action', self.style8)
        self.ws.write(4, self.admin_usecase_col, 'Event applicant action', self.style8)
        self.ws.write(5, self.admin_usecase_col, 'Event applicant search', self.style8)
        self.ws.write(6, self.admin_usecase_col, 'Schedule', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_search_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_search_o)
            self.ws.write(self.rowsize, self.admin_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.admin_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_floating_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_floating_action_o)
            self.ws.write(3, self.admin_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.admin_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_applicant_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicant_action_o)
            self.ws.write(4, self.admin_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.admin_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_applicant_search_o == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_search_o)
            self.ws.write(5, self.admin_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.admin_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_applicant_schedule_o == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_schedule_o)
            self.ws.write(6, self.admin_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.admin_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def int1_output_report(self):
        # ------------  Requirement Use cases -------------------
        self.ws.write(2, self.int1_usecase_col, 'Interviewer Login', self.style8)
        self.ws.write(3, self.int1_usecase_col, 'Event getby Id', self.style8)
        self.ws.write(4, self.int1_usecase_col, 'Event floating action', self.style8)
        self.ws.write(5, self.int1_usecase_col, 'Event interviews', self.style8)
        self.ws.write(6, self.int1_usecase_col, 'Reschedule action', self.style8)
        self.ws.write(7, self.int1_usecase_col, 'Rescheduled', self.style8)
        self.ws.write(8, self.int1_usecase_col, 'Cancel Interview', self.style8)

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_int1_login_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_o)
            self.ws.write(2, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_getby_id_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getby_id_o)
            self.ws.write(3, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_float_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_float_o)
            self.ws.write(4, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_interviews_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_interviews_o)
            self.ws.write(5, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_reschedule_action_o == 'Pass':
            self.Actual_success_cases.append(self.ui_reschedule_action_o)
            self.ws.write(6, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_rescheduled_o == 'Pass':
            self.Actual_success_cases.append(self.ui_rescheduled_o)
            self.ws.write(7, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_cancel_interview_o == 'Pass':
            self.Actual_success_cases.append(self.ui_cancel_interview_o)
            self.ws.write(8, self.int1_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.int1_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def int2_output_report(self):
        # ------------- Test Use cases -------------------
        self.ws.write(2, self.int2_usecase_col, 'Interviewer Login', self.style8)
        self.ws.write(3, self.int2_usecase_col, 'Event getby Id', self.style8)
        self.ws.write(4, self.int2_usecase_col, 'Event floating action', self.style8)
        self.ws.write(5, self.int2_usecase_col, 'Event interviews', self.style8)
        self.ws.write(6, self.int2_usecase_col, 'Cancel Request', self.style8)
        self.ws.write(7, self.int2_usecase_col, 'Cancel Interview', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_int2_login_o == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_login_o)
            self.ws.write(2, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_getby_id__int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getby_id__int2_o)
            self.ws.write(3, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_float_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_float_int2_o)
            self.ws.write(4, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_interviews_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_event_interviews_int2_o)
            self.ws.write(5, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_cancel_interview_request_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_cancel_interview_request_int2_o)
            self.ws.write(6, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_cancel_int2_o == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_cancel_int2_o)
            self.ws.write(7, self.int2_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.int2_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['interview_output_report'])

    def overall_status(self):
        self.ws.write(0, 0, 'Interview Flow USECASES', self.style4)
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
