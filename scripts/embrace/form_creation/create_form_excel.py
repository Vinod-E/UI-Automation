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

        self.xl_candidate_name_label = []
        self.xl_date_time_label = []
        self.xl_college_label = []
        self.xl_gender_label = []
        self.xl_country_label = []
        self.xl_address_label = []
        self.xl_birth_date_label = []
        self.xl_current_time_label = []
        self.xl_python_tutorial_label = []
        self.xl_java_tutorial_label = []

        self.xl_group_one = []
        self.xl_group_two = []

        self.xl_college_dropdown = []
        self.xl_checkbox = []
        self.xl_radiobutton = []





        self.candidate_label = ''
        self.date_time_label = ''
        self.college_label = ''
        self.gender_label = ''
        self.country_label = ''
        self.address_label = ''
        self.birth_label = ''
        self.current_label = ''
        self.python_label = ''
        self.java_label = ''

        self.group_one = ''
        self.group_two = ''

        self.checkbox_one = ''
        self.checkbox_two = ''
        self.radiobutton_one = ''
        self.radiobutton_two = ''




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
            if rows[10]:
                self.xl_candidate_name_label.append(rows[10])
            if rows[11]:
                self.xl_date_time_label.append(rows[11])
            if rows[12]:
                self.xl_college_label.append(str(rows[12]))
            if rows[13]:
                self.xl_gender_label.append(str(rows[13]))
            if rows[14]:
                self.xl_country_label.append(str(rows[14]))
            if rows[15]:
                self.xl_address_label.append(str(rows[15]))
            if rows[16]:
                self.xl_birth_date_label.append(str(rows[16]))
            if rows[17]:
                self.xl_current_time_label.append(str(rows[17]))
            if rows[18]:
                self.xl_python_tutorial_label.append(str(rows[18]))
            if rows[19]:
                self.xl_java_tutorial_label.append(str(rows[19]))
            if rows[20]:
                self.xl_group_one.append(str(rows[20]))
            if rows[21]:
                self.xl_group_two.append(str(rows[21]))
            if rows[22]:
                self.xl_college_dropdown.append(str(rows[22]))
            if rows[23]:
                self.xl_checkbox.append(str(rows[23]))
            if rows[24]:
                self.xl_radiobutton.append(str(rows[24]))



        for a in self.xl_candidate_name_label:
            self.candidate_label = a

        for b in self.xl_date_time_label:
            self.date_time_label = b

        for c in self.xl_college_label:
            self.college_label = c

        for d in self.xl_gender_label:
            self.gender_label = d

        for e in self.xl_country_label:
            self.country_label = e

        for f in self.xl_address_label:
            self.address_label = f

        for g in self.xl_birth_date_label:
            self.birth_label = g

        for h in self.xl_current_time_label:
            self.current_label = h

        for x in self.xl_python_tutorial_label:
            self.python_label = x

        for y in self.xl_java_tutorial_label:
            self.java_label = y

        for z in self.xl_group_one:
            self.group_one = z

        for za in self.xl_group_two:
            self.group_two = za


