import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class QuickInterviewExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(QuickInterviewExcelRead, self).__init__()

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['quick_interview_file'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_q = []
        self.xl_stage_q = []
        self.xl_interview_names = []
        self.xl_status_q = []
        self.xl_comment_q = []
        self.xl_int1 = []
        self.xl_int2 = []

        self.event_sprint_version_q = []

        # ------------- Iterate Excel sheet------------------------
        self.quick_interview_excel_read()

    def quick_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_q.append(rows[0])
            if rows[1]:
                self.xl_stage_q.append(str(rows[1]))
            if rows[2]:
                self.xl_interview_names.append(str(rows[2]))
            if rows[3]:
                self.xl_status_q.append(str(rows[3]))
            if rows[4]:
                self.xl_comment_q.append(str(rows[4]))
            if rows[5]:
                self.xl_int1.append(str(rows[5]))
            if rows[6]:
                self.xl_int2.append(str(rows[6]))

            for j in self.xl_event_name_q:
                event_name = j
                self.event_sprint_version_q = event_name.format(self.sprint_version)
