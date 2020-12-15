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

        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_screening_rule'])
        if self.login_server == 'betaams':
            self.form_sheet2 = workbook.sheet_by_index(1)
        if self.login_server == 'ams':
            self.form_sheet2 = workbook.sheet_by_index(1)
        if self.login_server == 'amsin':
            self.form_sheet2 = workbook.sheet_by_index(0)

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
        self.xl_attachment = []

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
        self.xl_resume_label = []

        self.xl_group_one = []
        self.xl_group_two = []

        self.xl_college_dropdown = []
        self.xl_checkbox = []
        self.xl_radiobutton = []

        #screening rule excel headers
        self.xl_Title = []
        self.xl_CandidateNameRule = []
        self.xl_CandidateName = []
        self.xl_College = []
        self.xl_Gender = []
        self.xl_Country = []
        self.xl_AddressRule = []
        self.xl_Address = []
        self.xl_CollegeId = []
        self.xl_Title2 = []
        self.xl_CandidateNameRule2 = []
        self.xl_CandidateName2 = []
        self.xl_College2 = []
        self.xl_Gender2 = []
        self.xl_Country2 = []
        self.xl_AddressRule2 = []
        self.xl_Address2 = []
        self.xl_CollegeId2 = []

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
        self.resume_label = ''


        self.group_one = ''
        self.group_two = ''

        self.checkbox_one = ''
        self.checkbox_two = ''
        self.radiobutton_one = ''
        self.radiobutton_two = ''
        self.attachment = ''

        # ------------- Iterate Excel sheet------------------------
        self.event_excel_read()
        self.event_excel_read1()

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
            if rows[25]:
                self.xl_attachment.append(str(rows[25]))
            if rows[26]:
                self.xl_resume_label.append(str(rows[26]))

    def event_excel_read1(self):
        # --------------------------------------candidate details-------------------------------------------------------
        for i in range(1, self.form_sheet2.nrows):
            number = i
            rows = self.form_sheet2.row_values(number)
            if not rows[0]:
                self.xl_Title.append(None)
            else:
                self.xl_Title.append(rows[0])

            if not rows[1]:
                self.xl_CandidateName.append(None)
            else:
                self.xl_CandidateName.append(rows[1])

            if not rows[2]:
                self.xl_CandidateNameRule.append(None)
            else:
                self.xl_CandidateNameRule.append(rows[2])

            if not rows[3]:
                self.xl_College.append(None)
            else:
                self.xl_College.append(rows[3])

            if not rows[4]:
                self.xl_Gender.append(None)
            else:
                self.xl_Gender.append(rows[4])

            if not rows[5]:
                self.xl_Country.append(None)
            else:
                self.xl_Country.append(rows[5])

            if not rows[6]:
                self.xl_Address.append(None)
            else:
                self.xl_Address.append(rows[6])

            if not rows[7]:
                self.xl_AddressRule.append(None)
            else:
                self.xl_AddressRule.append(rows[7])

            if not rows[8]:
                self.xl_CollegeId.append(None)
            else:
                self.xl_CollegeId.append(int(rows[8]))

            if not rows[9]:
                self.xl_Title2.append(None)
            else:
                self.xl_Title2.append(rows[9])

            if not rows[10]:
                self.xl_CandidateName2.append(None)
            else:
                self.xl_CandidateName2.append(rows[10])

            if not rows[11]:
                self.xl_CandidateNameRule2.append(None)
            else:
                self.xl_CandidateNameRule2.append(rows[11])

            if not rows[12]:
                self.xl_College2.append(None)
            else:
                self.xl_College2.append(rows[12])

            if not rows[13]:
                self.xl_Gender2.append(None)
            else:
                self.xl_Gender2.append(rows[13])

            if not rows[14]:
                self.xl_Country2.append(None)
            else:
                self.xl_Country2.append(rows[14])

            if not rows[15]:
                self.xl_Address2.append(None)
            else:
                self.xl_Address2.append(rows[15])

            if not rows[16]:
                self.xl_AddressRule2.append(None)
            else:
                self.xl_AddressRule2.append(rows[16])

            if not rows[17]:
                self.xl_CollegeId2.append(None)
            else:
                self.xl_CollegeId2.append(int(rows[17]))



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

        for zb in self.xl_attachment:
            self.attachment = zb

        for zb in self.xl_resume_label:
            self.resume_label = zb


