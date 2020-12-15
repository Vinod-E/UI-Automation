import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class MassExcelRead(common_file.CommonFile):
    def __init__(self):
        super(MassExcelRead, self).__init__()

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['mass_interview_file'])
        if self.login_server == 'betaams':
            self.mass_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.mass_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.mass_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_m = []
        self.xl_stage_m = []
        self.xl_size_m = []
        self.xl_status_m = []
        self.xl_comment_m = []
        self.xl_int1_name = []
        self.xl_int1_pwd = []

        self.event_sprint_version_m = []

        # ------------- Iterate Excel sheet------------------------
        self.mass_interview_excel_read()

    def mass_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.mass_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.mass_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_m.append(rows[0])
            if rows[1]:
                self.xl_size_m.append(int(rows[1]))
            if rows[2]:
                self.xl_stage_m.append(rows[2])
            if rows[3]:
                self.xl_status_m.append(rows[3])
            if rows[4]:
                self.xl_comment_m.append(rows[4])
            if rows[5]:
                self.xl_int1_name.append(rows[5])
            if rows[6]:
                self.xl_int1_pwd.append(rows[6])

            for j in self.xl_event_name_m:
                event_name = j
                self.event_sprint_version_m = event_name.format(self.sprint_version)
