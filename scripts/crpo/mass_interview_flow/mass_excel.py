import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class MassExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
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
        self.xl_int1_user = []
        self.xl_int1_pwd = []
        self.xl_int2_name = []
        self.xl_int2_user = []
        self.xl_int2_pwd = []
        self.xl_to_be_Queued = []
        self.xl_interview_pending = []
        self.xl_awaited = []
        self.xl_shortlist_m = []
        self.xl_message_m = []

        self.event_sprint_version_m = ''
        self.interviewer_1_name = ''

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
                self.xl_int1_user.append(rows[6])
            if rows[7]:
                self.xl_int1_pwd.append(rows[7])
            if rows[8]:
                self.xl_int2_name.append(rows[8])
            if rows[9]:
                self.xl_int2_user.append(rows[9])
            if rows[10]:
                self.xl_int2_pwd.append(rows[10])
            if rows[11]:
                self.xl_to_be_Queued.append(rows[11])
            if rows[12]:
                self.xl_interview_pending.append(rows[12])
            if rows[13]:
                self.xl_awaited.append(rows[13])
            if rows[14]:
                self.xl_shortlist_m.append(rows[14])
            if rows[15]:
                self.xl_message_m.append(rows[15])

            for j in self.xl_event_name_m:
                event_name = j
                self.event_sprint_version_m = event_name.format(self.sprint_version)

            for k in self.xl_int1_name:
                self.interviewer_1_name = k
