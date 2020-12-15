import xlrd
import test_data_inputpath
from scripts.crpo.requirement import requirement_config


class AssessmentExcelRead(requirement_config.RequirementConfig):
    def __init__(self):
        super(AssessmentExcelRead, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['clone_test'])
        if self.login_server == 'betaams':
            self.test_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams' or self.login_server == 'indiaams':
            self.test_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.test_sheet1 = workbook.sheet_by_index(1)

        # --------------- Value initialization ----------------
        self.xl_clone_test = []
        self.xl_new_test_name = []
        self.xl_old_test = ''

        self.assessment_sprint_version = []

        # ------------- Iterate Excel sheet------------------------
        self.assessment_excel_read()

    def assessment_excel_read(self):
        # --------------------------------------test details------------------------------------------------------------
        for i in range(1, self.test_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.test_sheet1.row_values(number)

            if rows[0]:
                self.xl_clone_test.append(rows[0])
            if rows[1]:
                self.xl_new_test_name.append(rows[1])

            for j in self.xl_new_test_name:
                job_name = j
                self.assessment_sprint_version = job_name.format(self.sprint_version)

            for k in self.xl_clone_test:
                self.xl_old_test = k


# ob = AssessmentExcelRead()
