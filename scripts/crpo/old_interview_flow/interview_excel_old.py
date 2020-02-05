import xlrd
import test_data_inputpath
from scripts.crpo.common import common_file


class OldInterviewExcelRead(common_file.CommonFile):
    def __init__(self):
        super(OldInterviewExcelRead, self).__init__()

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['old_interview_file'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_o = []
        self.xl_change_applicant_stage_o = []
        self.xl_change_applicant_status_o = []
        self.xl_change_status_comment_o = []
        self.xl_username_int1_o = []
        self.xl_password_int1_o = []
        self.xl_username_int2_o = []
        self.xl_password_int2_o = []
        self.xl_cancel_reschedule_comment_o = []
        self.xl_cancel_request_reason_o = []
        self.xl_cancel_request_comment_o = []
        self.xl_update_feedback_comment_o = []

        self.event_sprint_version_o = []

        # ------------- Iterate Excel sheet------------------------
        self.old_interview_excel_read()

    def old_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_o.append(rows[0])
            if rows[1]:
                self.xl_change_applicant_stage_o.append(str(rows[1]))
            if rows[2]:
                self.xl_change_applicant_status_o.append(str(rows[2]))
            if rows[3]:
                self.xl_change_status_comment_o.append(str(rows[3]))
            if rows[4]:
                self.xl_username_int1_o.append(str(rows[4]))
            if rows[5]:
                self.xl_password_int1_o.append(str(rows[5]))
            if rows[6]:
                self.xl_username_int2_o.append(str(rows[6]))
            if rows[7]:
                self.xl_password_int2_o.append(str(rows[7]))
            if rows[8]:
                self.xl_cancel_reschedule_comment_o.append(str(rows[8]))
            if rows[9]:
                self.xl_cancel_request_reason_o.append(str(rows[9]))
            if rows[10]:
                self.xl_cancel_request_comment_o.append(str(rows[10]))
            if rows[11]:
                self.xl_update_feedback_comment_o.append((str(rows[11])))

            for j in self.xl_event_name_o:
                event_name = j
                self.event_sprint_version_o = event_name.format(self.sprint_version)
