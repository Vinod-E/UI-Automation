import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class NewInterviewExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(NewInterviewExcelRead, self).__init__()

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['new_interview_file'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_n = []
        self.xl_stage_n = []
        self.xl_new_form = []
        self.xl_status_n = []
        self.xl_comment_n = []
        self.xl_int1 = []
        self.xl_int2 = []

        self.job_sprint_version_n = []

        # ------------- Iterate Excel sheet------------------------
        self.new_interview_excel_read()

    def new_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_n.append(rows[0])
            if rows[1]:
                self.xl_stage_n.append(str(rows[1]))
            if rows[2]:
                self.xl_new_form.append(str(rows[2]))
            if rows[3]:
                self.xl_status_n.append(str(rows[3]))
            if rows[4]:
                self.xl_comment_n.append(str(rows[4]))
            if rows[5]:
                self.xl_int1.append(str(rows[5]))
            if rows[6]:
                self.xl_int2.append(str(rows[6]))

            for j in self.xl_event_name_n:
                event_name = j
                self.job_sprint_version_n = event_name.format(self.sprint_version)
