import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.help_desk import reply_query


class HelpDeskOutput(styles.FontColor, reply_query.RaiseQuery):
    def __init__(self):
        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 33)))
        self.Actual_success_cases = []

        super(HelpDeskOutput, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.admin_headers_col = 0
        self.admin_status_col = 1
        self.can_header_col = 2
        self.can_status_col = 3
        self.default_headers_col = 4
        self.default_status_col = 5
        self.job_headers_col = 6
        self.job_status_col = 7
        self.event_headers_col = 8
        self.event_status_col = 9

        index = 0
        excelheaders = ['Admin', 'Status', 'Candidate_login', 'Status', 'Default Level', 'Status', 'Job Level',
                        'Status', 'Event Level', 'Status']
        for headers in excelheaders:
            if headers in ['Admin', 'Candidate_login', 'Default Level', 'Job Level', 'Event Level', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def admin_config_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.admin_headers_col, 'Requirement Tab', self.style8)
            self.ws.write(3, self.admin_headers_col, 'Advance search', self.style8)
            self.ws.write(4, self.admin_headers_col, 'Requirement details', self.style8)
            self.ws.write(5, self.admin_headers_col, 'Requirement Validation', self.style8)
            self.ws.write(6, self.admin_headers_col, 'Configuration tab', self.style8)
            self.ws.write(7, self.admin_headers_col, 'Query Configuration tab', self.style8)
            self.ws.write(8, self.admin_headers_col, 'Default Level Configuration', self.style8)
            self.ws.write(9, self.admin_headers_col, 'Job Level Configuration', self.style8)
            self.ws.write(10, self.admin_headers_col, 'Event Level Configuration', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_req_tab_he == 'Pass':
                self.Actual_success_cases.append(self.ui_req_tab_he)
                self.ws.write(2, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_req_advance_search_he == 'Pass':
                self.Actual_success_cases.append(self.ui_req_advance_search_he)
                self.ws.write(3, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_req_getbyid_he == 'Pass':
                self.Actual_success_cases.append(self.ui_req_getbyid_he)
                self.ws.write(4, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_requirement_validation_he == 'Pass':
                self.Actual_success_cases.append(self.ui_requirement_validation_he)
                self.ws.write(5, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_req_config_tab_he == 'Pass':
                self.Actual_success_cases.append(self.ui_req_config_tab_he)
                self.ws.write(6, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_configuration == 'Pass':
                self.Actual_success_cases.append(self.ui_query_configuration)
                self.ws.write(7, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_default_config == 'Pass':
                self.Actual_success_cases.append(self.ui_default_config)
                self.ws.write(8, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_config == 'Pass':
                self.Actual_success_cases.append(self.ui_job_config)
                self.ws.write(9, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.admin_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_config == 'Pass':
                self.Actual_success_cases.append(self.ui_event_config)
                self.ws.write(10, self.admin_status_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.admin_status_col, 'Fail', self.style3)

        except Exception as error:
            ui_logger.error(error)

    def candidate_raise_query_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.can_header_col, 'Candidate Login', self.style8)
            self.ws.write(3, self.can_header_col, 'Help desk tab', self.style8)
            self.ws.write(4, self.can_header_col, 'Query raise tab', self.style8)
            self.ws.write(5, self.can_header_col, 'Default Level Query', self.style8)
            self.ws.write(6, self.can_header_col, 'Job Level Query', self.style8)
            self.ws.write(7, self.can_header_col, 'Event Level Query', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_candidate_login_success == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_login_success)
                self.ws.write(2, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.can_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_help_desk_module == 'Pass':
                self.Actual_success_cases.append(self.ui_help_desk_module)
                self.ws.write(3, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.can_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_raise_query_module == 'Pass':
                self.Actual_success_cases.append(self.ui_raise_query_module)
                self.ws.write(4, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.can_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_default_raise_query == 'Pass':
                self.Actual_success_cases.append(self.ui_default_raise_query)
                self.ws.write(5, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.can_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_raise_query == 'Pass':
                self.Actual_success_cases.append(self.ui_job_raise_query)
                self.ws.write(6, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.can_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_event_raise_query == 'Pass':
                self.Actual_success_cases.append(self.ui_event_raise_query)
                self.ws.write(7, self.can_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.can_status_col, 'Fail', self.style3)

        except Exception as error:
            ui_logger.error(error)

    def default_level_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.default_headers_col, 'HelpDesk User Login', self.style8)
            self.ws.write(3, self.default_headers_col, 'Open Query', self.style8)
            self.ws.write(4, self.default_headers_col, 'Open Query Reply', self.style8)
            self.ws.write(5, self.default_headers_col, 'Inprogress Query', self.style8)
            self.ws.write(6, self.default_headers_col, 'Inprogress Query Reply', self.style8)
            self.ws.write(7, self.default_headers_col, 'Query Close', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_helpdesk_user1 == 'Pass':
                self.Actual_success_cases.append(self.ui_helpdesk_user1)
                self.ws.write(2, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.default_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_choosen_1 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_choosen_1)
                self.ws.write(3, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.default_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_reply_1 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_reply_1)
                self.ws.write(4, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.default_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_choosen_1 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_choosen_1)
                self.ws.write(5, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.default_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_reply_1 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_reply_1)
                self.ws.write(6, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.default_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_close_1 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_close_1)
                self.ws.write(7, self.default_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.default_status_col, 'Fail', self.style3)

        except Exception as error:
            ui_logger.error(error)

    def job_level_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.job_headers_col, 'HelpDesk User Login', self.style8)
            self.ws.write(3, self.job_headers_col, 'Open Query', self.style8)
            self.ws.write(4, self.job_headers_col, 'Open Query Reply', self.style8)
            self.ws.write(5, self.job_headers_col, 'Inprogress Query', self.style8)
            self.ws.write(6, self.job_headers_col, 'Inprogress Query Reply', self.style8)
            self.ws.write(7, self.job_headers_col, 'Query Close', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_helpdesk_user2 == 'Pass':
                self.Actual_success_cases.append(self.ui_helpdesk_user2)
                self.ws.write(2, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_choosen_2 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_choosen_2)
                self.ws.write(3, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_reply_2 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_reply_2)
                self.ws.write(4, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_choosen_2 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_choosen_2)
                self.ws.write(5, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_reply_2 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_reply_2)
                self.ws.write(6, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_close_2 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_close_2)
                self.ws.write(7, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.job_status_col, 'Fail', self.style3)

        except Exception as error:
            ui_logger.error(error)

    def event_level_output(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.event_headers_col, 'HelpDesk User Login', self.style8)
            self.ws.write(3, self.event_headers_col, 'Open Query', self.style8)
            self.ws.write(4, self.event_headers_col, 'Open Query Reply', self.style8)
            self.ws.write(5, self.event_headers_col, 'Inprogress Query', self.style8)
            self.ws.write(6, self.event_headers_col, 'Inprogress Query Reply', self.style8)
            self.ws.write(7, self.event_headers_col, 'Query Close', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            if self.ui_helpdesk_user3 == 'Pass':
                self.Actual_success_cases.append(self.ui_helpdesk_user3)
                self.ws.write(2, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_choosen_3 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_choosen_3)
                self.ws.write(3, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_reply_3 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_reply_3)
                self.ws.write(4, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_choosen_3 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_choosen_3)
                self.ws.write(5, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_inprogress_query_reply_3 == 'Pass':
                self.Actual_success_cases.append(self.ui_inprogress_query_reply_3)
                self.ws.write(6, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_query_close_3 == 'Pass':
                self.Actual_success_cases.append(self.ui_query_close_3)
                self.ws.write(7, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.event_status_col, 'Fail', self.style3)

        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'HELP DESK FLOW', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['help_desk_output_report'])

        except Exception as error:
            ui_logger.error(error)
