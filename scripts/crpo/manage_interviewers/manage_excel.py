import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class ManageInterviewExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(ManageInterviewExcelRead, self).__init__()

        # ---------------------------------- file reader index ---------------------------------------------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['manage_interviewers'])
        if self.login_server == 'betaams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.feedback_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.feedback_sheet1 = workbook.sheet_by_index(1)

        # ----------------------------------- Value initialization -----------------------------------------------------
        self.xl_event_name_mi = []
        self.xl_skill1_mi = []
        self.xl_skill2_mi = []
        self.xl_user1_mi = []
        self.xl_user2_mi = []

        self.event_sprint_version_mi = ''
        self.skill1 = ''
        self.skill2 = ''

        # ------------- Iterate Excel sheet------------------------
        self.live_interview_excel_read()

    def live_interview_excel_read(self):

        # -------------------------------------- interview details -----------------------------------------------------
        for i in range(1, self.feedback_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.feedback_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name_mi.append(rows[0])
            if rows[1]:
                self.xl_skill1_mi.append(rows[1])
            if rows[2]:
                self.xl_skill2_mi.append(rows[2])
            if rows[3]:
                self.xl_user1_mi.append(rows[3])
            if rows[4]:
                self.xl_user2_mi.append(rows[4])

            for j in self.xl_event_name_mi:
                event_name = j
                self.event_sprint_version_mi = event_name.format(self.sprint_version)

            for k in self.xl_skill1_mi:
                self.skill1 = k

            for l in self.xl_skill2_mi:
                self.skill2 = l
