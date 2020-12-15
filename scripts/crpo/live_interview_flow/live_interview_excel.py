import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class LiveInterviewExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(LiveInterviewExcelRead, self).__init__()

        self.is_behalf_int = 1
        self.stage1_l = ''
        self.stage2_l = ''

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['live_interview_file'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_l = []
        self.xl_stage1_l = []
        self.xl_stage2_l = []
        self.xl_comment_l = []
        self.xl_int1_l = []
        self.xl_int2_l = []
        self.xl_int1_name = []
        self.xl_int2_name = []

        self.event_sprint_version_l = []

        # ------------- Iterate Excel sheet------------------------
        self.live_interview_excel_read()

    def live_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_l.append(rows[0])
            if rows[1]:
                self.xl_stage1_l.append(str(rows[1]))
            if rows[2]:
                self.xl_stage2_l.append(str(rows[2]))
            if rows[3]:
                self.xl_comment_l.append(str(rows[3]))
            if rows[4]:
                self.xl_int1_l.append(str(rows[4]))
            if rows[5]:
                self.xl_int2_l.append(str(rows[5]))
            if rows[6]:
                self.xl_int1_name.append(str(rows[6]))
            if rows[7]:
                self.xl_int2_name.append(str(rows[7]))

            for j in self.xl_event_name_l:
                event_name = j
                self.event_sprint_version_l = event_name.format(self.sprint_version)

            for k in self.xl_stage1_l:
                stage1 = k
                self.stage1_l = stage1

            for m in self.xl_stage2_l:
                stage2 = m
                self.stage2_l = stage2
