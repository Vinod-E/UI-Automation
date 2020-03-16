import xlrd
import datetime
import test_data_inputpath
import common_login


class FormExcelRead(common_login.CommonLogin):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(FormExcelRead, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_form'])
        if self.login_server == 'betaams':
            self.form_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.form_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.form_sheet1 = workbook.sheet_by_index(1)

        # --------------- Value initialization ----------------
        self.xl_candidate_name = []
        self.xl_date_time = []
        self.xl_college = []
        self.xl_gender = []
        self.xl_country = []
        self.xl_address = []
        self.xl_birth_date = []
        self.xl_current_time = []
        self.xl_python_tutorial = []
        self.xl_java_tutorial = []

        # ------------- Iterate Excel sheet------------------------
        self.event_excel_read()

    def event_excel_read(self):
        # --------------------------------------candidate details-------------------------------------------------------
        for i in range(1, self.form_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.form_sheet1.row_values(number)

            if rows[0]:
                self.xl_candidate_name.append(rows[0])
            if rows[1]:
                self.xl_date_time.append(rows[1])
            if rows[2]:
                self.xl_college.append(str(rows[2]))
            if rows[3]:
                self.xl_gender.append(str(rows[3]))
            if rows[4]:
                self.xl_country.append(str(rows[4]))
            if rows[5]:
                self.xl_address.append(str(rows[5]))
            if rows[6]:
                self.xl_birth_date.append(str(rows[6]))
            if rows[7]:
                self.xl_current_time.append(str(rows[7]))
            if rows[8]:
                self.xl_python_tutorial.append(str(rows[8]))
            if rows[9]:
                self.xl_java_tutorial.append(str(rows[9]))
