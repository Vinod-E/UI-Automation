import xlrd
import test_data_inputpath
from scripts.crpo.common import common_file


class QueryExcelReadHelpDesk(common_file.CommonFile):
    def __init__(self):
        super(QueryExcelReadHelpDesk, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['help_desk'])
        if self.login_server == 'betaams':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'ams':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'amsin':
            self.req_sheet1 = workbook.sheet_by_index(0)

        # --------------- Value initialization ----------------
        self.xl_requirement_name = []

        self.requirement_sprint_version = ''

        # ------------- Iterate Excel sheet------------------------
        self.requirement_excel_read_he()

    def requirement_excel_read_he(self):

        # --------------------------------------requirement details-----------------------------------------------------
        for i in range(1, self.req_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.req_sheet1.row_values(number)

            if rows[0]:
                self.xl_requirement_name.append(rows[0])

            for j in self.xl_requirement_name:
                requirement_name = j
                self.requirement_sprint_version = requirement_name.format(self.sprint_version)
