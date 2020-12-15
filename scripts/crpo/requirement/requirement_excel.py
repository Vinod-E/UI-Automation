import xlrd
import test_data_inputpath
from scripts.crpo.job import edit_job


class RequirementExcelRead(edit_job.EditJobRole):
    def __init__(self):
        super(RequirementExcelRead, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_requirement'])
        if self.login_server == 'betaams':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'ams' or self.login_server == 'indiaams':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'amsin':
            self.req_sheet1 = workbook.sheet_by_index(0)

        # --------------- Value initialization ----------------
        self.xl_requirement_name = []
        self.xl_job_name_in_req = []
        self.xl_hiring_track = []
        self.xl_college_type = []

        self.requirement_sprint_version = []
        self.job_sprint_version = []

        # ------------- Iterate Excel sheet------------------------
        self.requirement_excel_read()

    def requirement_excel_read(self):

        # --------------------------------------requirement details-----------------------------------------------------
        for i in range(1, self.req_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.req_sheet1.row_values(number)

            if rows[0]:
                self.xl_requirement_name.append(rows[0])
            if rows[1]:
                self.xl_job_name_in_req.append(rows[1])
            if rows[2]:
                self.xl_hiring_track.append(rows[2])
            if rows[3]:
                self.xl_college_type.append(rows[3])

            for k in self.xl_job_name_in_req:
                job_name = k
                self.job_sprint_version = job_name.format(self.sprint_version)
            for j in self.xl_requirement_name:
                requirement_name = j
                self.requirement_sprint_version = requirement_name.format(self.sprint_version)


# ob = RequirementExcelRead()
