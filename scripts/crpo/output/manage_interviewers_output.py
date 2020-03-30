import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.manage_interviewers import criteria_configuration


class ManageInterviewersOutput(styles.FontColor, criteria_configuration.CriteriaConfig):
    def __init__(self):
        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 33)))
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

        index = 0
        excelheaders = ['Admin', 'Status']
        for headers in excelheaders:
            if headers in ['Admin', 'Status']:
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

        except Exception as error:
            api_logger.error(error)

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
            api_logger.error(error)
