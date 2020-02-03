import xlwt
import styles
from datetime import date
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.event import embrace_app


class CrpoOutputFile(styles.FontColor, embrace_app.EmbraceApp):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 74)))
        self.Actual_success_cases = []

        super(CrpoOutputFile, self).__init__()

        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))

        self.rowsize = 2
        self.size = self.rowsize

        self.job_usecase_col = 0
        self.job_status_col = 1
        self.req_usecase_col = 2
        self.req_status_col = 3
        self.test_usecase_col = 4
        self.test_status_col = 5
        self.event_usecase_col = 6
        self.event_status_col = 7
        self.task_usecase_col = 8
        self.task_status_col = 9

        index = 0
        excelheaders = ['Job UseCases', 'Status', 'Requirement Usecases', 'Status', 'Test', 'Status', 'Event UseCases',
                        'Status', 'Task UseCases', 'Status', ]
        for headers in excelheaders:
            if headers in ['Job UseCases', 'Event UseCases', 'Task UseCases', 'Requirement Usecases', 'Test', 'Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def job_output_report(self):
        try:
            # ------------------------- Writing Output Data to Job Use cases -------------------------------------------
            self.ws.write(2, self.job_usecase_col, 'Job creation', self.style8)
            self.ws.write(3, self.job_usecase_col, 'Job Validation', self.style8)
            self.ws.write(4, self.job_usecase_col, 'Floating actions', self.style8)
            self.ws.write(5, self.job_usecase_col, 'Selection Process action', self.style8)
            self.ws.write(6, self.job_usecase_col, 'Selection Process tagged', self.style8)
            self.ws.write(7, self.job_usecase_col, 'Configure Tab', self.style8)
            self.ws.write(8, self.job_usecase_col, 'EC Config', self.style8)
            self.ws.write(9, self.job_usecase_col, 'Task Config', self.style8)
            self.ws.write(10, self.job_usecase_col, 'FeedbackForm actions', self.style8)
            self.ws.write(11, self.job_usecase_col, 'Automation Tab', self.style8)
            self.ws.write(12, self.job_usecase_col, 'FeedbackForm stage1', self.style8)
            self.ws.write(13, self.job_usecase_col, 'FeedbackForm stage2', self.style8)
            self.ws.write(14, self.job_usecase_col, 'FeedbackForm stage3', self.style8)
            self.ws.write(15, self.job_usecase_col, 'Job Hopping/Automation', self.style8)
            self.ws.write(16, self.job_usecase_col, 'Tag interviewers action', self.style8)
            self.ws.write(17, self.job_usecase_col, 'Tagged interviewers', self.style8)
            self.ws.write(18, self.job_usecase_col, 'TagRequirement action', self.style8)
            self.ws.write(19, self.job_usecase_col, 'Tag to Requirement', self.style8)
            self.ws.write(20, self.job_usecase_col, 'UntagRequirement action', self.style8)
            self.ws.write(21, self.job_usecase_col, 'Untag from Requirement', self.style8)
            self.ws.write(22, self.job_usecase_col, 'Owners Tab', self.style8)
            self.ws.write(23, self.job_usecase_col, 'Edit action', self.style8)
            self.ws.write(24, self.job_usecase_col, 'Updated Job', self.style8)
            self.ws.write(25, self.job_usecase_col, 'Advance search', self.style8)
            self.ws.write(26, self.job_usecase_col, 'Job getbyid', self.style8)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_job_created == 'Pass':
                self.Actual_success_cases.append(self.ui_job_created)
                self.ws.write(self.rowsize, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(self.rowsize, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_job_validation)
                self.ws.write(3, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_floating_action == 'Pass':
                self.Actual_success_cases.append(self.ui_job_floating_action)
                self.ws.write(4, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_selection_process_action == 'Pass':
                self.Actual_success_cases.append(self.ui_selection_process_action)
                self.ws.write(5, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.selection_process_created == 'Pass':
                self.Actual_success_cases.append(self.selection_process_created)
                self.ws.write(6, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_configure_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_job_configure_tab)
                self.ws.write(7, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_ec_configure == 'Pass':
                self.Actual_success_cases.append(self.ui_ec_configure)
                self.ws.write(8, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_task_configure == 'Pass':
                self.Actual_success_cases.append(self.ui_task_configure)
                self.ws.write(9, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_feedback_form_action == 'Pass':
                self.Actual_success_cases.append(self.ui_feedback_form_action)
                self.ws.write(10, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_automation_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_job_automation_tab)
                self.ws.write(11, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_interview_stage1 == 'Pass':
                self.Actual_success_cases.append(self.ui_interview_stage1)
                self.ws.write(12, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_interview_stage2 == 'Pass':
                self.Actual_success_cases.append(self.ui_interview_stage2)
                self.ws.write(13, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(13, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_interview_stage3 == 'Pass':
                self.Actual_success_cases.append(self.ui_interview_stage3)
                self.ws.write(14, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(14, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_hopping_config == 'Pass':
                self.Actual_success_cases.append(self.ui_hopping_config)
                self.ws.write(15, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(15, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_interview_panel_action == 'Pass':
                self.Actual_success_cases.append(self.ui_interview_panel_action)
                self.ws.write(16, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(16, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_tag_interviews == 'Pass':
                self.Actual_success_cases.append(self.ui_tag_interviews)
                self.ws.write(17, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(17, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_tag_requirement_action == 'Pass':
                self.Actual_success_cases.append(self.ui_tag_requirement_action)
                self.ws.write(18, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(18, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_tag_requirement == 'Pass':
                self.Actual_success_cases.append(self.ui_tag_requirement)
                self.ws.write(19, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(19, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_un_tag_requirement_action == 'Pass':
                self.Actual_success_cases.append(self.ui_un_tag_requirement_action)
                self.ws.write(20, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(20, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_un_tag_requirement == 'Pass':
                self.Actual_success_cases.append(self.ui_un_tag_requirement)
                self.ws.write(21, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(21, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_owners_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_job_owners_tab)
                self.ws.write(22, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(22, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_edit_action == 'Pass':
                self.Actual_success_cases.append(self.ui_job_edit_action)
                self.ws.write(23, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(23, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_update_job == 'Pass':
                self.Actual_success_cases.append(self.ui_update_job)
                self.ws.write(24, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(24, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_job_advance_search)
                self.ws.write(25, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(25, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_job_getbyid == 'Pass':
                self.Actual_success_cases.append(self.ui_job_getbyid)
                self.ws.write(26, self.job_status_col, 'Pass', self.style7)
            else:
                self.ws.write(26, self.job_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)

    def requirement_output_report(self):
        try:
            # ------------  Requirement Use cases -------------------
            self.ws.write(2, self.req_usecase_col, 'Requirement creation', self.style8)
            self.ws.write(3, self.req_usecase_col, 'Requirement validation', self.style8)
            self.ws.write(4, self.req_usecase_col, 'Configure Tab', self.style8)
            self.ws.write(5, self.req_usecase_col, 'Duplicity Tab', self.style8)
            self.ws.write(6, self.req_usecase_col, 'Duplicity On', self.style8)
            self.ws.write(7, self.req_usecase_col, 'Advance search', self.style8)
            self.ws.write(8, self.req_usecase_col, 'Requirement getbyid', self.style8)

            # ----------------------------------------------------------------------------------------------------------

            if self.ui_create_requirement == 'Pass':
                self.Actual_success_cases.append(self.ui_create_requirement)
                self.ws.write(2, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_requirement_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_requirement_validation)
                self.ws.write(3, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_req_config_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_req_config_tab)
                self.ws.write(4, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_req_duplicity_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_req_duplicity_tab)
                self.ws.write(5, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_req_duplicity == 'Pass':
                self.Actual_success_cases.append(self.ui_req_duplicity)
                self.ws.write(6, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_req_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_req_advance_search)
                self.ws.write(7, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_req_getbyid == 'Pass':
                self.Actual_success_cases.append(self.ui_req_getbyid)
                self.ws.write(8, self.req_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.req_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)

    def assessment_output_report(self):
        try:
            # ------------- Test Use cases -------------------
            self.ws.write(2, self.test_usecase_col, 'Test advance search', self.style8)
            self.ws.write(3, self.test_usecase_col, 'Grid_verification_old', self.style8)
            self.ws.write(4, self.test_usecase_col, 'Getby_verification_old', self.style8)
            self.ws.write(5, self.test_usecase_col, 'Clone action', self.style8)
            self.ws.write(6, self.test_usecase_col, 'Cloned assessment', self.style8)
            self.ws.write(7, self.test_usecase_col, 'Grid_verification_new', self.style8)
            self.ws.write(8, self.test_usecase_col, 'Getby_verification_new', self.style8)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_test_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_test_advance_search)
                self.ws.write(2, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_old_test_grid_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_old_test_grid_validation)
                self.ws.write(3, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_old_test_getby_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_old_test_getby_validation)
                self.ws.write(4, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_clone_action == 'Pass':
                self.Actual_success_cases.append(self.ui_clone_action)
                self.ws.write(5, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_assessment_clone == 'Pass':
                self.Actual_success_cases.append(self.ui_assessment_clone)
                self.ws.write(6, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_new_test_grid_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_new_test_grid_validation)
                self.ws.write(7, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_new_test_getby_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_new_test_getby_validation)
                self.ws.write(8, self.test_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.test_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)

    def event_output_report(self):
        try:
            # ------------- Event Use cases -------------------
            self.ws.write(2, self.event_usecase_col, 'Event creation', self.style8)
            self.ws.write(3, self.event_usecase_col, 'Event validation', self.style8)
            self.ws.write(4, self.event_usecase_col, 'Config Tab', self.style8)
            self.ws.write(5, self.event_usecase_col, 'Task config', self.style8)
            self.ws.write(6, self.event_usecase_col, 'Task validation', self.style8)
            self.ws.write(7, self.event_usecase_col, 'Test config', self.style8)
            self.ws.write(8, self.event_usecase_col, 'Test validation', self.style8)
            self.ws.write(9, self.event_usecase_col, 'Owners Tab', self.style8)
            self.ws.write(10, self.event_usecase_col, 'Owners Edit', self.style8)
            self.ws.write(11, self.event_usecase_col, 'Owners config', self.style8)
            self.ws.write(12, self.event_usecase_col, 'Floating actions', self.style8)
            self.ws.write(13, self.event_usecase_col, 'Upload candidate action', self.style8)
            self.ws.write(14, self.event_usecase_col, 'Upload candidates', self.style8)
            self.ws.write(15, self.event_usecase_col, 'Advance search', self.style8)
            self.ws.write(16, self.event_usecase_col, 'View candidate action', self.style8)
            self.ws.write(17, self.event_usecase_col, 'Applicant Advance search', self.style8)
            self.ws.write(18, self.event_usecase_col, 'Applicant getby', self.style8)
            self.ws.write(19, self.event_usecase_col, 'Candidate page validation', self.style8)
            self.ws.write(20, self.event_usecase_col, 'Change applicant status action', self.style8)
            self.ws.write(21, self.event_usecase_col, 'Applicant movement', self.style8)
            self.ws.write(22, self.event_usecase_col, 'Current status validation', self.style8)
            self.ws.write(23, self.event_usecase_col, 'Candidate floating action', self.style8)
            self.ws.write(24, self.event_usecase_col, 'Manage Task action', self.style8)
            self.ws.write(25, self.event_usecase_col, 'Candidate task validation', self.style8)

            # ----------------------------------------------------------------------------------------------------------

            if self.ui_create_event == 'Pass':
                self.Actual_success_cases.append(self.ui_create_event)
                self.ws.write(2, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.event_validation_check == 'Pass':
                self.Actual_success_cases.append(self.event_validation_check)
                self.ws.write(3, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_config_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_event_config_tab)
                self.ws.write(4, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_task_config == 'Pass':
                self.Actual_success_cases.append(self.ui_event_task_config)
                self.ws.write(5, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.task_validation == 'Pass':
                self.Actual_success_cases.append(self.task_validation)
                self.ws.write(6, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_test_config == 'Pass':
                self.Actual_success_cases.append(self.ui_event_test_config)
                self.ws.write(7, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.test_validation == 'Pass':
                self.Actual_success_cases.append(self.test_validation)
                self.ws.write(8, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_owners_tab == 'Pass':
                self.Actual_success_cases.append(self.ui_event_owners_tab)
                self.ws.write(9, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_owner_edit_action == 'Pass':
                self.Actual_success_cases.append(self.ui_owner_edit_action)
                self.ws.write(10, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_owner_config == 'Pass':
                self.Actual_success_cases.append(self.ui_event_owner_config)
                self.ws.write(11, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_floating_action == 'Pass':
                self.Actual_success_cases.append(self.ui_event_floating_action)
                self.ws.write(12, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_upload_candidate_action == 'Pass':
                self.Actual_success_cases.append(self.ui_event_upload_candidate_action)
                self.ws.write(13, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(13, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_upload_candidate == 'Pass':
                self.Actual_success_cases.append(self.ui_event_upload_candidate)
                self.ws.write(14, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(14, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_event_advance_search)
                self.ws.write(15, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(15, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_event_applicants_action == 'Pass':
                self.Actual_success_cases.append(self.ui_event_applicants_action)
                self.ws.write(16, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(16, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_applicant_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_advance_search)
                self.ws.write(17, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(17, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_applicant_getby == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_getby)
                self.ws.write(18, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(18, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_candidate_details_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_details_validation)
                self.ws.write(19, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(19, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_change_applicant_status_action == 'Pass':
                self.Actual_success_cases.append(self.ui_change_applicant_status_action)
                self.ws.write(20, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(20, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_applicant_current_status == 'Pass':
                self.Actual_success_cases.append(self.ui_applicant_current_status)
                self.ws.write(21, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(21, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_current_status_validation == 'Pass':
                self.Actual_success_cases.append(self.ui_current_status_validation)
                self.ws.write(22, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(22, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_candidate_floating_action == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_floating_action)
                self.ws.write(23, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(23, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_candidate_manage_task_action == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_manage_task_action)
                self.ws.write(24, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(24, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_task_candidate_name == 'Pass':
                self.Actual_success_cases.append(self.ui_task_candidate_name)
                self.ws.write(25, self.event_status_col, 'Pass', self.style7)
            else:
                self.ws.write(25, self.event_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)

    def task_assign_output_report(self):
        try:
            # ------------- Event Use cases -------------------
            self.ws.write(2, self.task_usecase_col, 'More Modules action', self.style8)
            self.ws.write(3, self.task_usecase_col, 'Embrace Module', self.style8)
            self.ws.write(4, self.task_usecase_col, 'Advance search', self.style8)
            self.ws.write(5, self.task_usecase_col, 'Behalf of submission', self.style8)
            self.ws.write(6, self.task_usecase_col, 'Call back activity', self.style8)
            self.ws.write(7, self.task_usecase_col, 'Activity assignment', self.style8)
            self.ws.write(8, self.task_usecase_col, 'Total Task Count', self.style8)
            self.ws.write(9, self.task_usecase_col, 'Approved Task Count', self.style8)
            self.ws.write(10, self.task_usecase_col, 'Pending Task Count', self.style8)
            self.ws.write(11, self.task_usecase_col, 'Submitted Task Count', self.style8)
            self.ws.write(12, self.task_usecase_col, 'rejected Task Count', self.style8)
            # ----------------------------------------------------------------------------------------------------------

            if self.ui_more_tabs == 'Pass':
                self.Actual_success_cases.append(self.ui_more_tabs)
                self.ws.write(2, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(2, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_embrace_module == 'Pass':
                self.Actual_success_cases.append(self.ui_embrace_module)
                self.ws.write(3, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(3, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_embrace_advance_search == 'Pass':
                self.Actual_success_cases.append(self.ui_embrace_advance_search)
                self.ws.write(4, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(4, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submit_behalf == 'Pass':
                self.Actual_success_cases.append(self.ui_submit_behalf)
                self.ws.write(5, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(5, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_call_back_activity == 'Pass':
                self.Actual_success_cases.append(self.ui_call_back_activity)
                self.ws.write(6, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(6, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_a2_assignment == 'Pass':
                self.Actual_success_cases.append(self.ui_a2_assignment)
                self.ws.write(7, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(7, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_total_tasks == 'Pass':
                self.Actual_success_cases.append(self.ui_total_tasks)
                self.ws.write(8, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(8, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_approved_tasks == 'Pass':
                self.Actual_success_cases.append(self.ui_approved_tasks)
                self.ws.write(9, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(9, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_pending_tasks == 'Pass':
                self.Actual_success_cases.append(self.ui_pending_tasks)
                self.ws.write(10, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(10, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_submitted_tasks == 'Pass':
                self.Actual_success_cases.append(self.ui_submitted_tasks)
                self.ws.write(11, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(11, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_rejected_tasks == 'Pass':
                self.Actual_success_cases.append(self.ui_rejected_tasks)
                self.ws.write(12, self.task_status_col, 'Pass', self.style7)
            else:
                self.ws.write(12, self.task_status_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100/len(self.Expected_success_cases)

            self.ws.write(0, 0, 'CRPO USECASES', self.style4)
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
            self.wb_Result.save(test_data_inputpath.output['output_report'])

        except Exception as error:
            api_logger.error(error)
