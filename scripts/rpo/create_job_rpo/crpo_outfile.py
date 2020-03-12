from datetime import date

import xlwt
from selenium.common import exceptions
import create_offer
import styles
import test_data_inputpath


class CrpoOutputFile(styles.FontColor, create_offer.CreateOffer):

    def __init__(self):

        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 22)))
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
        self.interview_usecase_col = 2
        self.interview_status_col = 3
        self.offer_usecase_col = 4
        self.offer_status_col = 5
        self.vendor_usecase_col = 6
        self.vendor_status_col = 7

        # self.req_status_col = 3
        # self.test_usecase_col = 4
        # self.test_status_col = 5
        # self.event_usecase_col = 6
        # self.event_status_col = 7

        index = 0
        excelheaders = ['Job UseCases', 'Job Status', 'Interview UseCases', ' Interview Status', 'Offer UseCase',
                        'Offer Status', 'Vendor UseCase', 'Vendor Status']
        # excelheaders = ['Job UseCases', 'Job Status', 'Requirement Usecases', 'Requirement Status', 'Test UseCases',
        #                 'Test Status', 'Event UseCases', 'Event Status']
        for headers in excelheaders:
            if headers in ['Job UseCases', 'Job Status', 'Interview UseCases', ' Interview Status', 'Offer UseCase',
                           'Offer Status', 'Vendor UseCase', 'Vendor Status']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1
        print('Excel Headers are printed successfully')

    def output_report(self):
        # --------------------
        # Writing Output Data
        # --------------------

        # ------------  Job Use cases -------------------
        self.ws.write(2, self.job_usecase_col, 'Job Creation', self.style8)
        self.ws.write(3, self.job_usecase_col, 'Job Approved', self.style8)
        self.ws.write(4, self.job_usecase_col, 'Job Advance Search', self.style8)
        self.ws.write(5, self.job_usecase_col, 'Job Posting to Vendor ', self.style8)
        self.ws.write(6, self.job_usecase_col, 'Job Posting to Referal ', self.style8)
        self.ws.write(7, self.job_usecase_col, 'Feedback Form Configure', self.style8)
        self.ws.write(8, self.job_usecase_col, 'Tag interviewers', self.style8)
        self.ws.write(9, self.job_usecase_col, 'Extract Resume', self.style8)
        self.ws.write(10, self.job_usecase_col, 'Candidate Create And Tag To Job', self.style8)
        self.ws.write(11, self.job_usecase_col, 'Edit Job Role', self.style8)
        # self.ws.write(10, self.job_usecase_col, 'Applicant Status Change', self.style8)

        # self.ws.write(10, self.job_usecase_col, 'Provide Interview Feedback', self.style8)
        self.ws.write(12, self.job_usecase_col, 'Status Change to Offer Pending', self.style8)

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_job_created == 'Pass':
            self.Actual_success_cases.append(self.ui_job_created)
            self.ws.write(self.rowsize, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(self.rowsize, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_job_approved == 'Pass':
            self.Actual_success_cases.append(self.ui_job_approved)
            self.ws.write(3, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_job_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_job_advance_search)
            self.ws.write(4, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

        if self.ui_job_posting_to_vendor == 'Pass':
            self.Actual_success_cases.append(self.ui_job_posting_to_vendor)
            self.ws.write(5, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_job_posting_to_referal == 'Pass':
            self.Actual_success_cases.append(self.ui_job_posting_to_referal)
            self.ws.write(6, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(6, self.job_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_stage1 == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_stage1)
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

        if self.ui_extract_resume == 'Pass':
            self.Actual_success_cases.append(self.ui_extract_resume)
            self.ws.write(9, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(9, self.job_status_col, 'Fail', self.style3)

        # Canidate Tag
        if self.ui_create_candidate == 'Pass':
            self.Actual_success_cases.append(self.ui_create_candidate)
            self.ws.write(10, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(10, self.job_status_col, 'Fail', self.style3)

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_update_job == 'Pass':
            self.Actual_success_cases.append(self.ui_update_job)
            self.ws.write(11, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(11, self.job_status_col, 'Fail', self.style3)
        # self.wb_Result.save(test_data_inputpath.test_data_file['output_report'])

        # --------------------------------------------------------------------------------------------------------------

        if self.ui_status_change_to_offer_pending == 'Pass':
            self.Actual_success_cases.append(self.ui_status_change_to_offer_pending)
            self.ws.write(12, self.job_status_col, 'Pass', self.style7)
        else:
            self.ws.write(12, self.job_status_col, 'Fail', self.style3)

            # ----------------Interview Use Case----------------------------------------------------------------------------
        self.ws.write(2, self.interview_usecase_col, 'Interviewer Login ', self.style8)
        self.ws.write(3, self.interview_usecase_col, 'Applicant Interview Schedule ', self.style8)
        self.ws.write(4, self.interview_usecase_col, 'Provide Interview Feedback', self.style8)
        self.ws.write(5, self.interview_usecase_col, 'Interview Advance Search', self.style8)

        # write(row,col,value)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_interview_login == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_login)
            self.ws.write(2, self.interview_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.interview_status_col, 'Fail', self.style3)

        if self.ui_status_change == 'Pass':
            self.Actual_success_cases.append(self.ui_status_change)
            self.ws.write(3, self.interview_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.interview_status_col, 'Fail', self.style3)

        if self.ui_interview_feedback == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_feedback)
            self.ws.write(4, self.interview_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.interview_status_col, 'Fail', self.style3)

        if self.ui_interview_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_interview_advance_search)
            self.ws.write(5, self.interview_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.interview_status_col, 'Fail', self.style3)

        # ------------  Offer Use cases -------------------
        self.ws.write(2, self.offer_usecase_col, 'Offer Creation', self.style8)
        self.ws.write(3, self.offer_usecase_col, 'Offer Approved', self.style8)
        self.ws.write(4, self.offer_usecase_col, 'Offer Advance Search', self.style8)
        # self.ws.write()
        # write(row,col,value)
        # --------------------------------------------------------------------------------------------------------------
        if self.ui_create_offer == 'Pass':
            self.Actual_success_cases.append(self.ui_create_offer)
            self.ws.write(2, self.offer_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.offer_status_col, 'Fail', self.style3)

        if self.ui_offer_approved == 'Pass':
            self.Actual_success_cases.append(self.ui_offer_approved)
            self.ws.write(3, self.offer_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.offer_status_col, 'Fail', self.style3)

        if self.ui_offer_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_offer_advance_search)
            self.ws.write(4, self.offer_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.offer_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------
        self.ws.write(2, self.vendor_usecase_col, 'Vendor Login  ', self.style8)
        self.ws.write(3, self.vendor_usecase_col, 'Vendor Search', self.style8)
        self.ws.write(4, self.vendor_usecase_col, 'Extract Resume', self.style8)
        self.ws.write(5, self.vendor_usecase_col, 'Source Candidate and Tag to Job', self.style8)

        if self.ui_vendor_login == 'Pass':
            self.Actual_success_cases.append(self.ui_vendor_login)
            self.ws.write(2, self.vendor_status_col, 'Pass', self.style7)
        else:
            self.ws.write(2, self.vendor_status_col, 'Fail', self.style3)
        # -------------------------------------------------------------------------------------------

        if self.ui_vendor_advance_search == 'Pass':
            self.Actual_success_cases.append(self.ui_vendor_advance_search)
            self.ws.write(3, self.vendor_status_col, 'Pass', self.style7)
        else:
            self.ws.write(3, self.vendor_status_col, 'Fail', self.style3)
        # -----------------------------------------------------------------------------------------------
        if self.ui_vendor_extract_resume == 'Pass':
            self.Actual_success_cases.append(self.ui_vendor_extract_resume)
            self.ws.write(4, self.vendor_status_col, 'Pass', self.style7)
        else:
            self.ws.write(4, self.vendor_status_col, 'Fail', self.style3)
        # ------------------------------------------------------------------------------------------------------
        if self.ui_source_candidate == 'Pass':
            self.Actual_success_cases.append(self.ui_source_candidate)
            self.ws.write(5, self.vendor_status_col, 'Pass', self.style7)
        else:
            self.ws.write(5, self.vendor_status_col, 'Fail', self.style3)
        # --------------------------------------------------------------------------------------------------------------

    def overall_status(self):
        self.ws.write(0, 0, 'RPO USECASES', self.style4)
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
        self.wb_Result.save(test_data_inputpath.test_data_file['output_report'])

    def createJob(self):
        try:
            self.job_excel_read()
            self.create_job_role()
            self.job_advance_search()
            self.feedback_form()
            self.tag_interview_panel()
            self.job_posting()
            self.edit_job()
            self.tag_candidate()
            self.status_change()
            self.interviewModule()
            self.post_status_change()
            self.sourcedCandidate()
        except exceptions.NoSuchElementException as createJob:
            print(createJob)

    def login(self):
        try:
            self.excel_read()
            self.crpo_login()
        except exceptions.NoSuchElementException as crpologin:
            print crpologin

    def offer(self):
        try:
            self.offer_excel_read()
            self.offer_creation()
        except exceptions.NoSuchElementException as create_offer:
            print create_offer

#
# desc = CrpoOutputFile()
# desc.login()
# desc.createJob()
# desc.offer()
# desc.output_report()
# desc.overall_status()
