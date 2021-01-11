import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.mass_interview_flow import provide_mass_feedback


class MassInterviewOutputFile(styles.FontColor, provide_mass_feedback.MassFeedback):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 88)))
        self.Actual_success_cases = []

        super(MassInterviewOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 3
        self.size = self.rowsize
        self.c_sc_col = 0
        self.c_st_col = 1
        self.aa_sc_col = 2
        self.aa_st_col = 3
        self.sc_sc_col = 4
        self.sc_st_col = 5
        self.rc_sc_col = 6
        self.rc_st_col = 7
        self.au_sc_col = 8
        self.au_st_col = 9
        self.cl_sc = 10
        self.cl_st = 11
        self.int_sc_col = 0
        self.int_st_col = 1
        self.l_sc_col = 2
        self.l_st_col = 3
        self.p_sc_col = 4
        self.p_st_col = 5
        self.s2_sc_col = 6
        self.s2_st_col = 7
# ------------- Headers_set_1
        index = 0
        excelheaders = ['Candidate status (Recruiter)', 'Status', 'RoomAutoAssignConfig (Recruiter)', 'Status',
                        'Slot configuration (Recruiter)', 'Status', 'Room Creation (Recruiter)', 'Status',
                        'Tag/Untag Room (Recruiter)', 'Status', 'Candidate_login', 'Status']
        for headers in excelheaders:
            if headers in ['Candidate status (Recruiter)', 'Slot configuration (Recruiter)',
                           'RoomAutoAssignConfig (Recruiter)', 'Room Creation (Recruiter)',
                           'Tag/Untag Room (Recruiter)', 'Candidate_login', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
# ------------- Headers_set_2
        index = 0
        excelheaders = ['Interviewer_1', 'Status', 'STAGE1 Lobby (Interviewer)', 'Status',
                        'Provide Feedback (Interviewer)', 'Status', 'STAGE2 Lobby (Interviewer)',
                        'Status']
        for headers in excelheaders:
            if headers in ['Interviewer_1', 'STAGE1 Lobby (Interviewer)', 'Provide Feedback (Interviewer)',
                           'STAGE2 Lobby (Interviewer)', 'Status']:
                self.ws.write(18, index, headers, self.style0)
            else:
                self.ws.write(18, index, headers, self.style1)
            index += 1

    def candidate_status_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.c_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.c_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.c_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.c_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.c_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.c_sc_col, 'View Event Applicants', self.style8)
            self.ws.write(8, self.c_sc_col, 'Applicant Grid', self.style8)
            self.ws.write(9, self.c_sc_col, 'Applicant Advance Search', self.style8)
            self.ws.write(10, self.c_sc_col, 'Applicant Search Result', self.style8)
            self.ws.write(11, self.c_sc_col, 'Change Applicant status', self.style8)
            self.ws.write(12, self.c_sc_col, 'Applicant GetById', self.style8)
            self.ws.write(13, self.c_sc_col, 'Applicant Status Validate', self.style8)
            self.ws.write(14, self.c_sc_col, 'Candidate ID Copied', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(2, self.ui_event_tab_m, self.c_st_col)
            self.__common_result_pass(3, self.ui_advance_search_m, self.c_st_col)
            self.__common_result_pass(4, self.ui_event_details_m, self.c_st_col)
            self.__common_result_pass(5, self.ui_event_validation_m, self.c_st_col)
            self.__common_result_pass(6, self.ui_floating_action_m, self.c_st_col)
            self.__common_result_pass(7, self.ui_event_applicant_action_m, self.c_st_col)
            self.__common_result_pass(8, self.ui_event_applicant_grid_m, self.c_st_col)
            self.__common_result_pass(9, self.ui_applicant_search_action_m, self.c_st_col)
            self.__common_result_pass(10, self.ui_applicant_name_search_m, self.c_st_col)
            self.__common_result_pass(11, self.ui_change_applicant_status_action_m, self.c_st_col)
            self.__common_result_pass(12, self.ui_candidate_getby_m, self.c_st_col)
            self.__common_result_pass(13, self.ui_applicant_current_status_m, self.c_st_col)
            self.__common_result_pass(14, self.ui_candidate_id_copied_m, self.c_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def slot_configuration_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.sc_sc_col, 'Event Tab', self.style8)
            self.ws.write(3, self.sc_sc_col, 'Advance search', self.style8)
            self.ws.write(4, self.sc_sc_col, 'Event details', self.style8)
            self.ws.write(5, self.sc_sc_col, 'Event Validation', self.style8)
            self.ws.write(6, self.sc_sc_col, 'Floating actions', self.style8)
            self.ws.write(7, self.sc_sc_col, 'Slot Configure', self.style8)
            self.ws.write(8, self.sc_sc_col, 'Configure slot tab', self.style8)
            self.ws.write(9, self.sc_sc_col, 'Stage Search', self.style8)
            self.ws.write(10, self.sc_sc_col, 'Slot Creation', self.style8)
            self.ws.write(11, self.sc_sc_col, 'Slot Date&Time Filled', self.style8)
            self.ws.write(12, self.sc_sc_col, 'Assign Slot', self.style8)
            self.ws.write(13, self.sc_sc_col, 'Communicate Slot', self.style8)
            self.ws.write(14, self.sc_sc_col, 'Search Slot Candidate', self.style8)
            self.ws.write(15, self.sc_sc_col, 'View Candidate link action', self.style8)
            self.ws.write(16, self.sc_sc_col, 'Candidate login link copied', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(2, self.ui_event_tab_m_1, self.sc_st_col)
            self.__common_result_pass(3, self.ui_advance_search_m_1, self.sc_st_col)
            self.__common_result_pass(4, self.ui_event_details_m_1, self.sc_st_col)
            self.__common_result_pass(5, self.ui_event_validation_m_1, self.sc_st_col)
            self.__common_result_pass(6, self.ui_floating_action_m_1, self.sc_st_col)
            self.__common_result_pass(7, self.ui_slot_config_action_m, self.sc_st_col)
            self.__common_result_pass(8, self.ui_configure_slot_tab_m, self.sc_st_col)
            self.__common_result_pass(9, self.ui_stage_search_m, self.sc_st_col)
            self.__common_result_pass(10, self.ui_slot_creation_m, self.sc_st_col)
            self.__common_result_pass(11, self.ui_slot_data_filled_m, self.sc_st_col)
            self.__common_result_pass(12, self.ui_assign_slot_m, self.sc_st_col)
            self.__common_result_pass(13, self.ui_communicate_slot_m, self.sc_st_col)
            self.__common_result_pass(14, self.ui_search_slot_applicant_m, self.sc_st_col)
            self.__common_result_pass(15, self.ui_interview_lobby_action_m, self.sc_st_col)
            self.__common_result_pass(16, self.ui_candidate_login_link_copied, self.sc_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def auto_assign_room_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.aa_sc_col, 'Configuration Tab', self.style8)
            self.ws.write(3, self.aa_sc_col, 'Auto Assign ON/OFF', self.style8)
            self.ws.write(4, self.aa_sc_col, 'Chat Config', self.style8)
            self.ws.write(5, self.aa_sc_col, 'Select User', self.style8)
            self.ws.write(6, self.aa_sc_col, 'Save Config', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(2, self.ui_event_config_tab, self.aa_st_col)
            self.__common_result_pass(3, self.ui_auto_assign_on, self.aa_st_col)
            self.__common_result_pass(4, self.ui_chat_config, self.aa_st_col)
            self.__common_result_pass(5, self.ui_select_user, self.aa_st_col)
            self.__common_result_pass(6, self.ui_save_config, self.aa_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def candidate_login_report(self):
        try:
            self.ws.write(2, self.cl_sc, 'Open candidate link', self.style8)
            self.ws.write(3, self.cl_sc, 'Candidate Id to Entry', self.style8)
            self.ws.write(4, self.cl_sc, 'Enter button', self.style8)
            self.ws.write(5, self.cl_sc, 'Candidate Lobby Entry', self.style8)
            self.ws.write(6, self.cl_sc, self.ui_c_message_1, self.style8)
            self.ws.write(7, self.cl_sc, 'Interview status - To Be Queued', self.style8)
            self.ws.write(8, self.cl_sc, self.ui_c_message_2, self.style8)
            self.ws.write(9, self.cl_sc, 'Interview status - Interview Pending', self.style8)
            self.ws.write(10, self.cl_sc, self.ui_c_message_3, self.style8)
            self.ws.write(11, self.cl_sc, 'Interview status - Invited to Interview', self.style8)
            self.ws.write(12, self.cl_sc, self.ui_c_message_4, self.style8)
            self.ws.write(13, self.cl_sc, 'Interview status - Interview Completed', self.style8)
            # ----------------------------------------------------------------------------------------------------------

            self.__common_result_pass(2, self.ui_open_lobby_link_m, self.cl_st)
            self.__common_result_pass(3, self.ui_candidate_id_enter_m, self.cl_st)
            self.__common_result_pass(4, self.ui_enter_room_action_m, self.cl_st)
            self.__common_result_pass(5, self.ui_entered_candidate_login_m, self.cl_st)
            self.__common_result_pass(6, self.ui_c_msg1, self.cl_st)
            self.__common_result_pass(7, self.candidate_interview_status_m, self.cl_st)
            self.__common_result_pass(8, self.ui_c_msg2, self.cl_st)
            self.__common_result_pass(9, self.candidate_interview_status_m, self.cl_st)
            self.__common_result_pass(10, self.ui_c_msg3, self.cl_st)
            self.__common_result_pass(11, self.ui_select_candidate_m, self.cl_st)
            self.__common_result_pass(12, self.ui_c_msg4, self.cl_st)
            self.__common_result_pass(13, self.ui_interview_finish_button, self.cl_st)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def room_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(2, self.rc_sc_col, 'Create Room button', self.style8)
            self.ws.write(3, self.rc_sc_col, 'Room Creation', self.style8)
            self.ws.write(4, self.rc_sc_col, 'Room Activate Action', self.style8)
            self.ws.write(5, self.rc_sc_col, 'Room Activate', self.style8)
            self.ws.write(6, self.rc_sc_col, 'Validate Created Room', self.style8)
            self.ws.write(7, self.rc_sc_col, 'Auto Room action ON', self.style8)
            self.ws.write(8, self.rc_sc_col, 'Interview status - Interview Pending', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(2, self.ui_create_room_action_m, self.rc_st_col)
            self.__common_result_pass(3, self.ui_room_created_m, self.rc_st_col)
            self.__common_result_pass(4, self.ui_active_room_action_m, self.rc_st_col)
            self.__common_result_pass(5, self.ui_room_activate_m, self.rc_st_col)
            self.__common_result_pass(6, self.ui_room_validation_m, self.rc_st_col)
            self.__common_result_pass(7, self.ui_auto_enable, self.rc_st_col)
            self.__common_result_pass(8, self.candidate_interview_status_t_m, self.rc_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def assigned_unassigned_room_report(self):
        try:
            self.ws.write(2, self.au_sc_col, 'Validation Auto Tagged', self.style8)
            self.ws.write(3, self.au_sc_col, 'Un Assign Room Action', self.style8)
            self.ws.write(4, self.au_sc_col, 'Un Assign form Room', self.style8)
            self.ws.write(5, self.au_sc_col, 'Un Assign form Room', self.style8)
            self.ws.write(6, self.au_sc_col, 'Assign Room Action', self.style8)
            self.ws.write(7, self.au_sc_col, 'Assign Room to Candidate', self.style8)
            self.ws.write(8, self.au_sc_col, 'Interview status - Interview Pending', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(2, self.ui_tagged_room, self.au_st_col)
            self.__common_result_pass(3, self.ui_unassigned_room, self.au_st_col)
            self.__common_result_pass(4, self.ui_unassigned_room_action, self.au_st_col)
            self.__common_result_pass(5, self.ui_validation_check_unassigned, self.au_st_col)
            self.__common_result_pass(6, self.ui_assign_room_action_m, self.au_st_col)
            self.__common_result_pass(7, self.ui_tag_room_m, self.au_st_col)
            self.__common_result_pass(8, self.candidate_interview_status_t_m, self.au_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])
        except Exception as error:
            ui_logger.error(error)

    def interviewer_login_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(19, self.int_sc_col, 'Interview Login', self.style8)
            self.ws.write(20, self.int_sc_col, 'Event Tab', self.style8)
            self.ws.write(21, self.int_sc_col, 'Advance search', self.style8)
            self.ws.write(22, self.int_sc_col, 'Event details', self.style8)
            self.ws.write(23, self.int_sc_col, 'Event Validation', self.style8)
            self.ws.write(24, self.int_sc_col, 'Floating actions', self.style8)
            self.ws.write(25, self.int_sc_col, 'View Interview Panel', self.style8)
            self.ws.write(26, self.int_sc_col, 'Validate Lobby screen', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(19, self.ui_int1_login_m, self.int_st_col)
            self.__common_result_pass(20, self.ui_event_tab_m_2, self.int_st_col)
            self.__common_result_pass(21, self.ui_advance_search_m_2, self.int_st_col)
            self.__common_result_pass(22, self.ui_event_details_m_2, self.int_st_col)
            self.__common_result_pass(23, self.ui_event_validation_m_3, self.int_st_col)
            self.__common_result_pass(24, self.ui_floating_action_m_4, self.int_st_col)
            self.__common_result_pass(25, self.ui_view_interview_panel_action_m, self.int_st_col)
            self.__common_result_pass(26, self.int1_panel_validation_m, self.int_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def lobby_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(19, self.l_sc_col, 'Next candidate', self.style8)
            self.ws.write(20, self.l_sc_col, 'Validate Candidate', self.style8)
            self.ws.write(21, self.l_sc_col, 'Invite Candidate to Video call', self.style8)
            self.ws.write(22, self.l_sc_col, 'Candidate Video link Opened', self.style8)
            self.ws.write(23, self.l_sc_col, 'Validate VideoProctor Page', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(19, self.ui_select_candidate_action_m, self.l_st_col)
            self.__common_result_pass(20, self.ui_select_candidate_m, self.l_st_col)
            self.__common_result_pass(21, self.ui_invite_candidate_action, self.l_st_col)
            self.__common_result_pass(22, self.ui_invited_candidate_to_VC, self.l_st_col)
            self.__common_result_pass(23, self.ui_validate_video_proctor_page, self.l_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def mass_feedback_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(19, self.p_sc_col, 'Provide Feedback Button', self.style8)
            self.ws.write(20, self.p_sc_col, 'Feedback screen validation', self.style8)
            self.ws.write(21, self.p_sc_col, 'Decision select', self.style8)
            self.ws.write(22, self.p_sc_col, 'Submit Feedback', self.style8)
            self.ws.write(23, self.p_sc_col, 'View Profile Button', self.style8)
            self.ws.write(24, self.p_sc_col, 'Profile Screen Validate', self.style8)
            self.ws.write(25, self.p_sc_col, 'Candidate status', self.style8)
            self.ws.write(26, self.p_sc_col, 'Interview Finished Button', self.style8)
            self.ws.write(27, self.p_sc_col, 'Finished Interview', self.style8)
            self.ws.write(28, self.p_sc_col, 'Validate Next candidate select', self.style8)

            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(19, self.ui_provide_feedback_action_m, self.p_st_col)
            self.__common_result_pass(20, self.ui_p_f_screen_validate, self.p_st_col)
            self.__common_result_pass(21, self.ui_decision_select, self.p_st_col)
            self.__common_result_pass(22, self.ui_p_f_submit_button, self.p_st_col)
            self.__common_result_pass(23, self.ui_p_f_submitted, self.p_st_col)
            self.__common_result_pass(24, self.ui_view_profile_action, self.p_st_col)
            self.__common_result_pass(25, self.ui_profile_screen_validate, self.p_st_col)
            self.__common_result_pass(26, self.ui_interview_finish_button, self.p_st_col)
            self.__common_result_pass(27, self.ui_finished_interview, self.p_st_col)
            self.__common_result_pass(28, self.ui_next_candidate_screen_validate, self.p_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def stage_2_output_report(self):
        try:
            # ------------------------------ Writing Output Data -------------------------------------------------------
            self.ws.write(19, self.s2_sc_col, 'Next candidate', self.style8)
            self.ws.write(20, self.s2_sc_col, 'Validate Candidate', self.style8)
            self.ws.write(21, self.s2_sc_col, 'Invite Candidate to Video call', self.style8)
            self.ws.write(22, self.s2_sc_col, 'Provide Feedback Button', self.style8)
            self.ws.write(23, self.s2_sc_col, 'Finished Interview', self.style8)
            self.ws.write(24, self.s2_sc_col, 'Validate Next candidate select', self.style8)
            # ----------------------------------------------------------------------------------------------------------
            self.__common_result_pass(19, self.ui_select_candidate_action_m, self.s2_st_col)
            self.__common_result_pass(20, self.ui_select_candidate_m, self.s2_st_col)
            self.__common_result_pass(21, self.ui_invite_candidate_action, self.s2_st_col)
            self.__common_result_pass(22, self.ui_provide_feedback_action_m, self.s2_st_col)
            self.__common_result_pass(23, self.ui_finished_interview, self.s2_st_col)
            self.__common_result_pass(24, self.ui_next_candidate_screen_validate, self.s2_st_col)

            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)

    def __common_result_pass(self, row, result_key, column):
        try:
            if result_key == 'Pass':
                self.Actual_success_cases.append(result_key)
                self.ws.write(row, column, 'Pass', self.style7)
            else:
                self.ws.write(row, column, 'Fail', self.style3)
        except Exception as error:
            ui_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100 / len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'MASS INTERVIEW FLOW', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['mass_int_report'])

        except Exception as error:
            ui_logger.error(error)
