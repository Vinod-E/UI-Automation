from scripts.crpo import Candidate_actions
import styles
import test_data_inputpath
import xlwt
from datetime import date


class ApplicantActionOutput(styles.FontColor, Candidate_actions.CandidateActions):
    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 14)))
        self.Actual_success_cases = []

        super(ApplicantActionOutput, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 2
        self.size = self.rowsize
        self.Event_usecase_col = 0
        self.Event_status_col = 1
        self.Job_usecase_col = 2
        self.Job_status_col = 3
        self.Candidate_usecase_col = 4
        self.Candidate_status_col = 5

        index = 0
        excelheaders = ['Event Applicants', 'Status', 'Job Applicants', 'Status', 'Candidates Tab', 'Status']
        for headers in excelheaders:
            if headers in ['Event Applicants', 'Job Applicants', 'Candidates Tab', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def event_applicant_action_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  Event Use cases -------------------
        self.ws.write(2, self.Event_usecase_col, 'Event Tab', self.style8)
        self.ws.write(3, self.Event_usecase_col, 'Event Advance search', self.style8)
        self.ws.write(4, self.Event_usecase_col, 'Event Details', self.style8)
        self.ws.write(5, self.Event_usecase_col, 'Event Floating actions', self.style8)
        self.ws.write(6, self.Event_usecase_col, 'Event Applicants', self.style8)
        self.ws.write(7, self.Event_usecase_col, 'Event Advance Search', self.style8)
        self.ws.write(8, self.Event_usecase_col, 'Event Applicants Details', self.style8)
        self.ws.write(9, self.Event_usecase_col, 'Event Applicants Actions', self.style9)
        self.ws.write(10, self.Event_usecase_col, 'Change Applicant Status', self.style8)
        self.ws.write(11, self.Event_usecase_col, 'Compose Mail', self.style8)
        self.ws.write(12, self.Event_usecase_col, 'Send SMS', self.style8)
        self.ws.write(13, self.Event_usecase_col, 'Tag to Job/Test', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_tab == 'Pass':
            self.Actual_success_cases.append(self.ui_event_tab)
            self.ws.write(self.rowsize, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_event_advance_search)
            self.ws.write(3, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_get_by_id == 'Pass':
            self.Actual_success_cases.append(self.ui_event_get_by_id)
            self.ws.write(4, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_floating_actions == 'Pass':
            self.Actual_success_cases.append(self.ui_event_floating_actions)
            self.ws.write(5, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_applicants == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicants)
            self.ws.write(6, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_applicant_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_advance_search)
            self.ws.write(7, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_candidate_get_by_id == 'Pass':
            self.Actual_success_cases.append(self.ui_candidate_get_by_id)
            self.ws.write(8, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_candidate_status_changed == 'Pass':
            self.Actual_success_cases.append(self.ui_candidate_status_changed)
            self.ws.write(10, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_compose_mail == 'Pass':
            self.Actual_success_cases.append(self.ui_compose_mail)
            self.ws.write(11, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_send_sms == 'Pass':
            self.Actual_success_cases.append(self.ui_send_sms)
            self.ws.write(12, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_tag_to_job == 'Pass':
            self.Actual_success_cases.append(self.ui_tag_to_job)
            self.ws.write(13, self.Event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.Event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['Applicant_action_output_report'])

    def candidate_tab_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  candidate tab Use cases -------------------
        self.ws.write(2, self.Candidate_usecase_col, 'Candidate Tab', self.style8)
        self.ws.write(3, self.Candidate_usecase_col, 'Candidate Advance search', self.style8)
        self.ws.write(4, self.Candidate_usecase_col, 'Candidate Actions', self.style9)
        self.ws.write(5, self.Candidate_usecase_col, 'Candidate Tag To Event', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_candidate_tab == 'Pass':
            self.Actual_success_cases.append(self.ui_candidate_tab)
            self.ws.write(self.rowsize, self.Candidate_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.Candidate_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_candidate_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_candidate_advance_search)
            self.ws.write(3, self.Candidate_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.Candidate_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_tag_to_event == 'Pass':
            self.Actual_success_cases.append(self.ui_tag_to_event)
            self.ws.write(5, self.Candidate_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.Candidate_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['Applicant_action_output_report'])

    def overall_status(self):
        self.ws.write(0, 0, 'Applicant Actions', self.style4)
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
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['Applicant_action_output_report'])
