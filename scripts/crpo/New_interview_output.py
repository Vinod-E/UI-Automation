import xlwt
import configure_new_feedback
from datetime import date
import styles
import test_data_inputpath


class InterviewOutputFile(styles.FontColor, configure_new_feedback.NewFeedBackForm):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 11)))
        self.Actual_success_cases = []

        super(InterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.config_usecase_col = 0
        self.config_status_col = 1
        self.N_PF_usecase_col = 2
        self.N_PF_status_col = 3
        self.N_UF_usecase_col = 4
        self.N_UF_status_col = 5

        index = 0
        excelheaders = ['Configuration', 'Status', 'Provide Feedback', 'Status', 'Update Feedback', 'Status']
        for headers in excelheaders:
            if headers in ['Configuration', 'Provide Feedback', 'Update Feedback', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def configuration_output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  Job Use cases -------------------
        self.ws.write(2, self.config_usecase_col, 'Admin', self.style9)
        self.ws.write(3, self.config_usecase_col, 'Settings', self.style8)
        self.ws.write(4, self.config_usecase_col, 'Interview Module', self.style8)
        self.ws.write(5, self.config_usecase_col, 'Enable New Interview Feedback Form', self.style8)

        self.ws.write(6, self.config_usecase_col, 'Job Role', self.style8)
        self.ws.write(7, self.config_usecase_col, 'Job Search', self.style8)
        self.ws.write(8, self.config_usecase_col, 'Job getbyid', self.style8)
        self.ws.write(9, self.config_usecase_col, 'floating action', self.style8)
        self.ws.write(10, self.config_usecase_col, 'Configure Feedback action', self.style8)
        self.ws.write(11, self.config_usecase_col, 'Interview Stage', self.style8)
        self.ws.write(12, self.config_usecase_col, 'Configured new feedback form', self.style8)

        self.ws.write(13, self.config_usecase_col, 'Disable New Interview Feedback Form', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_settings_icon == 'Pass':
            self.Actual_success_cases.append(self.ui_settings_icon)
            self.ws.write(3, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_module == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_module)
            self.ws.write(4, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_new_interview_feedback_form_on == 'Pass':
            self.Actual_success_cases.append(self.ui_new_interview_feedback_form_on)
            self.ws.write(5, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_jobrole_tab == 'Pass':
            self.Actual_success_cases.append(self.ui_jobrole_tab)
            self.ws.write(6, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_job_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_job_advance_search)
            self.ws.write(7, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_job_getbyid == 'Pass':
            self.Actual_success_cases.append(self.ui_job_getbyid)
            self.ws.write(8, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_Floating_actions == 'Pass':
            self.Actual_success_cases.append(self.ui_Floating_actions)
            self.ws.write(9, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_getbyid_menu_feedback_form == 'Pass':
            self.Actual_success_cases.append(self.ui_getbyid_menu_feedback_form)
            self.ws.write(10, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_stage == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_stage)
            self.ws.write(11, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_new_form_configured == 'Pass':
            self.Actual_success_cases.append(self.ui_new_form_configured)
            self.ws.write(12, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_new_interview_feedback_form_off == 'Pass':
            self.Actual_success_cases.append(self.ui_new_interview_feedback_form_off)
            self.ws.write(13, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['New_interview_output_report'])

    def overall_status(self):
        self.ws.write(0, 0, 'New Interview Flow', self.style4)
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
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['New_interview_output_report'])
