import xlrd
import datetime
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.common import common_file


class QueryExcelReadHelpDesk(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
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
        self.xl_category_1 = []
        self.xl_user_1 = []
        self.xl_sla_1 = []
        self.xl_login_1 = []
        self.xl_category_2 = []
        self.xl_user_2 = []
        self.xl_sla_2 = []
        self.xl_login_2 = []
        self.xl_category_3 = []
        self.xl_user_3 = []
        self.xl_sla_3 = []
        self.xl_login_3 = []

        self.requirement_sprint_version = ''

        # ------------- Iterate Excel sheet------------------------
        self.requirement_excel_read_he()

    def requirement_excel_read_he(self):
        try:
            # --------------------------------------requirement details-------------------------------------------------
            for i in range(1, self.req_sheet1.nrows):
                number = i  # Counting number of rows
                rows = self.req_sheet1.row_values(number)

                if rows[0]:
                    self.xl_requirement_name.append(rows[0])
                if rows[1]:
                    self.xl_category_1.append(rows[1])
                if rows[2]:
                    self.xl_user_1.append(rows[2])
                if rows[3]:
                    self.xl_sla_1.append(str(int(rows[3])))
                if rows[4]:
                    self.xl_login_1.append(rows[4])
                if rows[5]:
                    self.xl_category_2.append(rows[5])
                if rows[6]:
                    self.xl_user_2.append(rows[6])
                if rows[7]:
                    self.xl_sla_2.append(str(int(rows[7])))
                if rows[8]:
                    self.xl_login_2.append(rows[8])
                if rows[9]:
                    self.xl_category_3.append(rows[9])
                if rows[10]:
                    self.xl_user_3.append(rows[10])
                if rows[11]:
                    self.xl_sla_3.append(str(int(rows[11])))
                if rows[12]:
                    self.xl_login_3.append(rows[12])

                for j in self.xl_requirement_name:
                    requirement_name = j
                    self.requirement_sprint_version = requirement_name.format(self.sprint_version)

        except Exception as error:
            api_logger.error(error)
