import xlwt
import New_Update_Feedback
from datetime import date
import styles
import test_data_inputpath


class InterviewOutputFile(styles.FontColor, New_Update_Feedback.NewUpdateFeedback):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 38)))
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

        # ------------  Configuration cases -------------------
        self.ws.write(2, self.config_usecase_col, 'Admin', self.style9)
        self.ws.write(3, self.config_usecase_col, 'Settings', self.style8)
        self.ws.write(4, self.config_usecase_col, 'Interview Module', self.style8)
        self.ws.write(5, self.config_usecase_col, 'Enable New Interview Feedback Form', self.style8)

        self.ws.write(6, self.config_usecase_col, 'Job Role Tab', self.style8)
        self.ws.write(7, self.config_usecase_col, 'Job Search', self.style8)
        self.ws.write(8, self.config_usecase_col, 'Job getbyid', self.style8)
        self.ws.write(9, self.config_usecase_col, 'floating action', self.style8)
        self.ws.write(10, self.config_usecase_col, 'Configure Feedback action', self.style8)
        self.ws.write(11, self.config_usecase_col, 'Interview Stage', self.style8)
        self.ws.write(12, self.config_usecase_col, 'Configured new feedback form', self.style8)
        self.ws.write(13, self.config_usecase_col, 'Disable New Interview Feedback Form', self.style8)
        self.ws.write(14, self.config_usecase_col, 'Event Tab', self.style8)
        self.ws.write(15, self.config_usecase_col, 'Event Search', self.style8)
        self.ws.write(16, self.config_usecase_col, 'Event GetbyId', self.style8)
        self.ws.write(17, self.config_usecase_col, 'Event Floating actions', self.style8)
        self.ws.write(18, self.config_usecase_col, 'Event applicants', self.style8)
        self.ws.write(19, self.config_usecase_col, 'Event applicants search', self.style8)
        self.ws.write(20, self.config_usecase_col, 'Change applicant status', self.style8)
        self.ws.write(21, self.config_usecase_col, 'Schedule', self.style8)

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
        if self.ui_event_tab_n == 'Pass':
            self.Actual_success_cases.append(self.ui_event_tab_n)
            self.ws.write(14, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(14, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_search_n == 'Pass':
            self.Actual_success_cases.append(self.ui_event_search_n)
            self.ws.write(15, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(15, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_getbyid_n == 'Pass':
            self.Actual_success_cases.append(self.ui_event_getbyid_n)
            self.ws.write(16, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(16, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_floating_action_n == 'Pass':
            self.Actual_success_cases.append(self.ui_event_floating_action_n)
            self.ws.write(17, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(17, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_event_applicant_action_n == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicant_action_n)
            self.ws.write(18, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(18, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_applicant_search_n == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_search_n)
            self.ws.write(19, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(19, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_change_applicant_status_action_n == 'Pass':
            self.Actual_success_cases.append(self.ui_change_applicant_status_action_n)
            self.ws.write(20, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(20, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_applicant_schedule_n == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_schedule_n)
            self.ws.write(21, self.config_status_col, 'Pass', self.style7)
        else:
            self.ws.write(21, self.config_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['New_interview_output_report'])

    def provide_feedback_output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  provide feedback cases -------------------
        self.ws.write(2, self.N_PF_usecase_col, 'Interviewer_1', self.style9)
        self.ws.write(3, self.N_PF_usecase_col, 'Interviewer_1 Login', self.style8)
        self.ws.write(4, self.N_PF_usecase_col, 'Event Tab', self.style8)
        self.ws.write(5, self.N_PF_usecase_col, 'Event Search', self.style8)
        self.ws.write(6, self.N_PF_usecase_col, 'Event Getbyid', self.style8)
        self.ws.write(7, self.N_PF_usecase_col, 'Event Floating actions', self.style8)
        self.ws.write(8, self.N_PF_usecase_col, 'Event Interviews', self.style8)
        self.ws.write(9, self.N_PF_usecase_col, 'Provide feedback action', self.style8)
        self.ws.write(10, self.N_PF_usecase_col, 'Provide feedback screen', self.style8)
        self.ws.write(11, self.N_PF_usecase_col, 'Save as Draft', self.style8)
        self.ws.write(12, self.N_PF_usecase_col, 'Auto decision - Rejected', self.style8)
        self.ws.write(13, self.N_PF_usecase_col, 'Interviewer_1 submit feedback', self.style8)
        self.ws.write(14, self.N_PF_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(15, self.N_PF_usecase_col, 'Interviewer_2 Login', self.style8)
        self.ws.write(16, self.N_PF_usecase_col, 'Provide feedback screen', self.style8)
        self.ws.write(17, self.N_PF_usecase_col, 'Manual decision - Maybe', self.style8)
        self.ws.write(18, self.N_PF_usecase_col, 'Interviewer_2 submit feedback', self.style8)

        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_PF_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_PF_n)
            self.ws.write(self.rowsize, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_ET_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_ET_n)
            self.ws.write(4, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_EAS_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_EAS_n)
            self.ws.write(5, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_EAS_getbyid_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_EAS_getbyid_n)
            self.ws.write(6, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_EFA_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_EFA_n)
            self.ws.write(7, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_login_EFA_EI_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_login_EFA_EI_n)
            self.ws.write(8, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_feedback_action_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_feedback_action_n)
            self.ws.write(9, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_feedback_screen_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_feedback_screen_n)
            self.ws.write(10, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_saveasdraft_n == 'Pass':
            self.Actual_success_cases.append(self.ui_saveasdraft_n)
            self.ws.write(11, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_auto_decision == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_auto_decision)
            self.ws.write(12, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int1_submit_feedback == 'Pass':
            self.Actual_success_cases.append(self.ui_int1_submit_feedback)
            self.ws.write(13, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_login_PF_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_login_PF_n)
            self.ws.write(15, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(15, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_feedback_screen_n == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_feedback_screen_n)
            self.ws.write(16, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(16, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_manual_decision == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_manual_decision)
            self.ws.write(17, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(17, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_submit_feedback == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_submit_feedback)
            self.ws.write(18, self.N_PF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(18, self.N_PF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['New_interview_output_report'])

    def new_update_feedback_output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  update feedback cases -------------------
        self.ws.write(2, self.N_UF_usecase_col, 'Interviewer_2', self.style9)
        self.ws.write(3, self.N_UF_usecase_col, 'Completed interviews Bucket', self.style8)
        self.ws.write(4, self.N_UF_usecase_col, 'Update feedback', self.style8)
        self.ws.write(5, self.N_UF_usecase_col, 'Manual update decision - Shortlist', self.style8)
        self.ws.write(6, self.N_UF_usecase_col, 'Interviewer_2 updated feedback', self.style8)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_completed_interviews == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_completed_interviews)
            self.ws.write(self.rowsize, self.N_UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.N_UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_update_feedback == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_update_feedback)
            self.ws.write(4, self.N_UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.N_UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_manual_update_decision == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_manual_update_decision)
            self.ws.write(5, self.N_UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.N_UF_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_int2_updated_feedback == 'Pass':
            self.Actual_success_cases.append(self.ui_int2_updated_feedback)
            self.ws.write(6, self.N_UF_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.N_UF_status_col, 'Fail', self.style3)
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
