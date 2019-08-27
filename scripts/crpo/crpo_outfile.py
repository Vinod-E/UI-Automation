import xlwt
import create_event
from datetime import date
import styles
import test_data_inputpath


class CrpoOutputFile(styles.FontColor, create_event.CreateEvent):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 40)))
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
        excelheaders = ['Job UseCases', 'Job Status', 'Requirement Usecases', 'Requirement Status', 'Test UseCases',
                        'Test Status', 'Event UseCases', 'Event Status', 'Task Assignment', 'Task Assignment Status']
        for headers in excelheaders:
            if headers in ['Job UseCases', 'Job Status', 'Requirement Usecases', 'Requirement Status', 'Test UseCases',
                           'Test Status', 'Event UseCases', 'Event Status', 'Task Assignment',
                           'Task Assignment Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def job_output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  Job Use cases -------------------
        self.ws.write(2, self.job_usecase_col, 'Job creation', self.style8)
        self.ws.write(3, self.job_usecase_col, 'Job advance search', self.style8)
        self.ws.write(4, self.job_usecase_col, 'Job selection Process', self.style8)
        self.ws.write(5, self.job_usecase_col, 'Feedback_Form stage1', self.style8)
        self.ws.write(6, self.job_usecase_col, 'Feedback_Form stage2', self.style8)
        self.ws.write(7, self.job_usecase_col, 'Feedback_Form stage3', self.style8)
        self.ws.write(8, self.job_usecase_col, 'Tag interviewers', self.style8)
        self.ws.write(9, self.job_usecase_col, 'Eligibility criteria configuration', self.style8)
        self.ws.write(10, self.job_usecase_col, 'Task configuration', self.style8)
        self.ws.write(11, self.job_usecase_col, 'Job Hopping/Automation', self.style8)
        self.ws.write(12, self.job_usecase_col, 'Edit Job Role', self.style8)
        self.ws.write(13, self.job_usecase_col, 'Tag to Requirement', self.style8)
        self.ws.write(14, self.job_usecase_col, 'Untag from Requirement', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_job_created == 'Pass':
            self.Actual_success_cases.append(self.ui_job_created)
            self.ws.write(self.rowsize, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_job_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_job_advance_search)
            self.ws.write(3, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_selection_process == 'Pass':
            self.Actual_success_cases.append(self.ui_selection_process)
            self.ws.write(4, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_interview_stage1 == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_stage1)
            self.ws.write(5, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_interview_stage2 == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_stage2)
            self.ws.write(6, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_interview_stage3 == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_stage3)
            self.ws.write(7, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_tag_interviews == 'Pass':
            self.Actual_success_cases.append(self.ui_tag_interviews)
            self.ws.write(8, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_ec_configure == 'Pass':
            self.Actual_success_cases.append(self.ui_ec_configure)
            self.ws.write(9, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_task_configure == 'Pass':
            self.Actual_success_cases.append(self.ui_task_configure)
            self.ws.write(10, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_hopping_config == 'Pass':
            self.Actual_success_cases.append(self.ui_hopping_config)
            self.ws.write(11, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_update_job == 'Pass':
            self.Actual_success_cases.append(self.ui_update_job)
            self.ws.write(12, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_tag_requirement == 'Pass':
            self.Actual_success_cases.append(self.ui_tag_requirement)
            self.ws.write(13, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_un_tag_requirement == 'Pass':
            self.Actual_success_cases.append(self.ui_un_tag_requirement)
            self.ws.write(14, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(14, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['output_report'])

    def requirement_output_report(self):
        # ------------  Requirement Use cases -------------------
        self.ws.write(2, self.req_usecase_col, 'Requirement creation', self.style8)
        self.ws.write(3, self.req_usecase_col, 'Requirement advance search', self.style8)
        self.ws.write(4, self.req_usecase_col, 'Requirement getbyid', self.style8)
        self.ws.write(5, self.req_usecase_col, 'Requirement config tab', self.style8)
        self.ws.write(6, self.req_usecase_col, 'Requirement Duplicity', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_create_requirement == 'Pass':
            self.Actual_success_cases.append(self.ui_create_requirement)
            self.ws.write(2, self.req_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.req_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_req_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_req_advance_search)
            self.ws.write(3, self.req_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.req_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_req_getbyid == 'Pass':
            self.Actual_success_cases.append(self.ui_req_getbyid)
            self.ws.write(4, self.req_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.req_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_req_config_tab == 'Pass':
            self.Actual_success_cases.append(self.ui_req_config_tab)
            self.ws.write(5, self.req_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.req_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_req_duplicity == 'Pass':
            self.Actual_success_cases.append(self.ui_req_duplicity)
            self.ws.write(6, self.req_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.req_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['output_report'])

    def test_output_report(self):
        # ------------- Test Use cases -------------------
        self.ws.write(2, self.test_usecase_col, 'Test advance search', self.style8)
        self.ws.write(3, self.test_usecase_col, 'Test Clone Creation', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_test_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_test_advance_search)
            self.ws.write(2, self.test_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.test_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_test_clone == 'Pass':
            self.Actual_success_cases.append(self.ui_test_clone)
            self.ws.write(3, self.test_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.test_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['output_report'])

    def event_output_report(self):
        # ------------- Event Use cases -------------------
        self.ws.write(2, self.event_usecase_col, 'Event creation', self.style8)
        self.ws.write(3, self.event_usecase_col, 'Event task config', self.style8)
        self.ws.write(4, self.event_usecase_col, 'Event test config', self.style8)
        self.ws.write(5, self.event_usecase_col, 'Event owners config', self.style8)
        self.ws.write(6, self.event_usecase_col, 'Event upload Candidates', self.style8)
        self.ws.write(7, self.event_usecase_col, 'Event View Candidates', self.style8)
        self.ws.write(8, self.event_usecase_col, 'Event Advance search', self.style8)
        self.ws.write(9, self.event_usecase_col, 'Applicants Advance search', self.style8)
        self.ws.write(10, self.event_usecase_col, 'Applicant get_by_Id', self.style8)
        self.ws.write(11, self.event_usecase_col, 'EC with positive status', self.style8)
        self.ws.write(12, self.event_usecase_col, 'Tag to test', self.style8)
        self.ws.write(13, self.event_usecase_col, 'Change applicant status', self.style8)

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_create_event == 'Pass':
            self.Actual_success_cases.append(self.ui_create_event)
            self.ws.write(2, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_task_config == 'Pass':
            self.Actual_success_cases.append(self.ui_event_task_config)
            self.ws.write(3, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_test_config == 'Pass':
            self.Actual_success_cases.append(self.ui_event_test_config)
            self.ws.write(4, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_owner_config == 'Pass':
            self.Actual_success_cases.append(self.ui_event_owner_config)
            self.ws.write(5, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_upload_candidate == 'Pass':
            self.Actual_success_cases.append(self.ui_event_upload_candidate)
            self.ws.write(6, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_applicants == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicants)
            self.ws.write(7, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_event_advance_search)
            self.ws.write(8, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_applicant_search == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicant_search)
            self.ws.write(9, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_event_applicant_getby == 'Pass':
            self.Actual_success_cases.append(self.ui_event_applicant_getby)
            self.ws.write(10, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_ec_eligible == 'Pass':
            self.Actual_success_cases.append(self.ui_ec_eligible)
            self.ws.write(11, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_tag_to_test == 'Pass':
            self.Actual_success_cases.append(self.ui_tag_to_test)
            self.ws.write(12, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_applicant_current_status == 'Pass':
            self.Actual_success_cases.append(self.ui_applicant_current_status)
            self.ws.write(13, self.event_status_col, 'Pass', self.style7)
        else:
            self.ws.write(13, self.event_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['output_report'])

    def task_assign_output_report(self):
        # ------------- Event Use cases -------------------
        self.ws.write(2, self.task_usecase_col, 'Task Assignment', self.style8)
        self.ws.write(3, self.task_usecase_col, 'Assignment Status', self.style8)
        self.ws.write(4, self.task_usecase_col, 'Activity Call Back', self.style8)
        self.ws.write(5, self.task_usecase_col, 'Total Task Count', self.style8)
        self.ws.write(6, self.task_usecase_col, 'Submitted Task Count', self.style8)
        self.ws.write(7, self.task_usecase_col, 'Approved Task Count', self.style8)
        self.ws.write(8, self.task_usecase_col, 'Pending Task Count', self.style8)
        self.ws.write(9, self.task_usecase_col, 'rejected Task Count', self.style8)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_task_candidate_name == 'Pass':
            self.Actual_success_cases.append(self.ui_task_candidate_name)
            self.ws.write(2, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_a2_assignment == 'Pass':
            self.Actual_success_cases.append(self.ui_a2_assignment)
            self.ws.write(3, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_call_back_status == 'Pass':
            self.Actual_success_cases.append(self.ui_call_back_status)
            self.ws.write(4, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_total_tasks == 'Pass':
            self.Actual_success_cases.append(self.ui_total_tasks)
            self.ws.write(5, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_submitted_tasks == 'Pass':
            self.Actual_success_cases.append(self.ui_submitted_tasks)
            self.ws.write(6, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_approved_tasks == 'Pass':
            self.Actual_success_cases.append(self.ui_approved_tasks)
            self.ws.write(7, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(7, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_pending_tasks == 'Pass':
            self.Actual_success_cases.append(self.ui_pending_tasks)
            self.ws.write(8, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(8, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_rejected_tasks == 'Pass':
            self.Actual_success_cases.append(self.ui_rejected_tasks)
            self.ws.write(9, self.task_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.task_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

    def overall_status(self):
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
        self.wb_Result.save(test_data_inputpath.crpo_test_data_file['output_report'])
