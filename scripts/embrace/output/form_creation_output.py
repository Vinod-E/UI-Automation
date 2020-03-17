import xlwt
import styles
import datetime
from datetime import date
import test_data_inputpath
from logger_settings import api_logger
from scripts.embrace.form_creation import form_validation


class FormOutputReport(styles.FontColor, form_validation.FormValidations):
    def __init__(self):
        self.date_now = str(date.today())
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 20)))
        self.Actual_success_cases = []

        super(FormOutputReport, self).__init__()
        # -------------------------------------
        # Excel sheet write for Output results
        # -------------------------------------
        self.wb_Result = xlwt.Workbook()
        self.ws = self.wb_Result.add_sheet('UI_Automation_{}'.format(self.sprint_version))
        self.rowsize = 3
        self.size = self.rowsize
        self.label_col = 0
        self.label_validation_col = 1
        self.form_field_col = 2
        self.form_field_validate_col = 3

        index = 0
        excelheaders = ['Label', 'Label Validation', 'Field', 'Field Validation']
        for headers in excelheaders:
            if headers in ['Field', 'Field Validation', 'Label', 'Label Validation']:
                self.ws.write(1, index, headers, self.style0)
            else:
                self.ws.write(1, index, headers, self.style1)
            index += 1

    def create_form_label_output(self):
        try:
            # ------------------------------ Writing Input Data -------------------------------------------------------
            self.ws.write(2, self.label_col, self.xl_candidate_name_label, self.style8)
            self.ws.write(3, self.label_col, self.xl_date_time_label, self.style8)
            self.ws.write(4, self.label_col, self.xl_college_label, self.style8)
            self.ws.write(5, self.label_col, self.xl_gender_label, self.style8)
            self.ws.write(6, self.label_col, self.xl_country_label, self.style8)
            self.ws.write(7, self.label_col, self.xl_address_label, self.style8)
            self.ws.write(8, self.label_col, self.xl_birth_date_label, self.style8)
            self.ws.write(9, self.label_col, self.xl_current_time_label, self.style8)
            self.ws.write(10, self.label_col, self.xl_python_tutorial_label, self.style8)
            self.ws.write(11, self.label_col, self.xl_java_tutorial_label, self.style8)

            # ------------------------------ Writing Output Data -------------------------------------------------------
            if self.ui_candidate_name_label == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_name_label)
                self.ws.write(2, self.label_validation_col, self.candidate_label, self.style7)
            else:
                self.ws.write(2, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_date_time_label == 'Pass':
                self.Actual_success_cases.append(self.ui_date_time_label)
                self.ws.write(3, self.label_validation_col, self.date_time_label, self.style7)
            else:
                self.ws.write(3, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_college_label == 'Pass':
                self.Actual_success_cases.append(self.ui_college_label)
                self.ws.write(4, self.label_validation_col, self.college_label, self.style7)
            else:
                self.ws.write(4, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_gender_label == 'Pass':
                self.Actual_success_cases.append(self.ui_gender_label)
                self.ws.write(5, self.label_validation_col, self.gender_label, self.style7)
            else:
                self.ws.write(5, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_country_label == 'Pass':
                self.Actual_success_cases.append(self.ui_country_label)
                self.ws.write(6, self.label_validation_col, self.country_label, self.style7)
            else:
                self.ws.write(6, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_address_label == 'Pass':
                self.Actual_success_cases.append(self.ui_address_label)
                self.ws.write(7, self.label_validation_col, self.address_label, self.style7)
            else:
                self.ws.write(7, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_birth_date_label == 'Pass':
                self.Actual_success_cases.append(self.ui_birth_date_label)
                self.ws.write(8, self.label_validation_col, self.birth_label, self.style7)
            else:
                self.ws.write(8, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_current_time_label == 'Pass':
                self.Actual_success_cases.append(self.ui_current_time_label)
                self.ws.write(9, self.label_validation_col, self.current_label, self.style7)
            else:
                self.ws.write(9, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_python_tutorial_label == 'Pass':
                self.Actual_success_cases.append(self.ui_python_tutorial_label)
                self.ws.write(10, self.label_validation_col, self.python_label, self.style7)
            else:
                self.ws.write(10, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_java_tutorial_label == 'Pass':
                self.Actual_success_cases.append(self.ui_java_tutorial_label)
                self.ws.write(11, self.label_validation_col, self.java_label, self.style7)
            else:
                self.ws.write(11, self.label_validation_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

        except Exception as error:
            api_logger.error(error)

    def create_form_field_output(self):
        try:
            # ------------------------------ Writing Input Data -------------------------------------------------------
            self.ws.write(2, self.form_field_col, self.xl_candidate_name, self.style8)
            self.ws.write(3, self.form_field_col, self.xl_date_time, self.style8)
            self.ws.write(4, self.form_field_col, self.xl_college, self.style8)
            self.ws.write(5, self.form_field_col, self.xl_gender, self.style8)
            self.ws.write(6, self.form_field_col, self.xl_country, self.style8)
            self.ws.write(7, self.form_field_col, self.xl_address, self.style8)
            self.ws.write(8, self.form_field_col, self.xl_birth_date, self.style8)
            self.ws.write(9, self.form_field_col, self.xl_current_time, self.style8)
            self.ws.write(10, self.form_field_col, self.xl_python_tutorial, self.style8)
            self.ws.write(11, self.form_field_col, self.xl_java_tutorial, self.style8)

            # ------------------------------ Writing Output Data -------------------------------------------------------
            if self.ui_candidate_name == 'Pass':
                self.Actual_success_cases.append(self.ui_candidate_name)
                self.ws.write(2, self.form_field_validate_col, 'Text_field', self.style7)
            else:
                self.ws.write(2, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_date_time == 'Pass':
                self.Actual_success_cases.append(self.ui_date_time)
                self.ws.write(3, self.form_field_validate_col, 'Date_Time', self.style7)
            else:
                self.ws.write(3, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_college == 'Pass':
                self.Actual_success_cases.append(self.ui_college)
                self.ws.write(4, self.form_field_validate_col, 'Dropdown_field', self.style7)
            else:
                self.ws.write(4, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_gender == 'Pass':
                self.Actual_success_cases.append(self.ui_gender)
                self.ws.write(5, self.form_field_validate_col, 'Radio_field', self.style7)
            else:
                self.ws.write(5, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_country == 'Pass':
                self.Actual_success_cases.append(self.ui_country)
                self.ws.write(6, self.form_field_validate_col, 'Checkbox_Field', self.style7)
            else:
                self.ws.write(6, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_address == 'Pass':
                self.Actual_success_cases.append(self.ui_address)
                self.ws.write(7, self.form_field_validate_col, 'TextArea_Field', self.style7)
            else:
                self.ws.write(7, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_birth_date == 'Pass':
                self.Actual_success_cases.append(self.ui_birth_date)
                self.ws.write(8, self.form_field_validate_col, 'Date_Field', self.style7)
            else:
                self.ws.write(8, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_current_time == 'Pass':
                self.Actual_success_cases.append(self.ui_current_time)
                self.ws.write(9, self.form_field_validate_col, 'Time_Field', self.style7)
            else:
                self.ws.write(9, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_python_tutorial == 'Pass':
                self.Actual_success_cases.append(self.ui_python_tutorial)
                self.ws.write(10, self.form_field_validate_col, 'Video_Field', self.style7)
            else:
                self.ws.write(10, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------
            if self.ui_java_tutorial == 'Pass':
                self.Actual_success_cases.append(self.ui_java_tutorial)
                self.ws.write(11, self.form_field_validate_col, 'Link_Field', self.style7)
            else:
                self.ws.write(11, self.form_field_validate_col, 'Fail', self.style3)
            # ----------------------------------------------------------------------------------------------------------

        except Exception as error:
            api_logger.error(error)

    def overall_status(self):
        try:
            failure_cases = len(self.Expected_success_cases) - len(self.Actual_success_cases)
            percentage = len(self.Actual_success_cases) * 100 / len(self.Expected_success_cases)
            end_date_time = datetime.datetime.now()
            time_taken = end_date_time - self.start_date_time
            minutes = time_taken.total_seconds() / 60

            self.ws.write(0, 0, 'CREATE FORM', self.style4)
            if self.Expected_success_cases == self.Actual_success_cases:
                self.ws.write(0, 1, 'Pass', self.style5)
            else:
                self.ws.write(0, 1, 'Fail', self.style6)

            self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
            self.ws.write(0, 3, 'Sprint_{}'.format(self.sprint_version), self.style5)
            self.ws.write(0, 4, 'SPRINT DATE', self.style4)
            self.ws.write(0, 5, self.date_now, self.style5)
            self.ws.write(0, 6, 'SERVER', self.style4)
            self.ws.write(0, 7, self.login_server, self.style5)
            self.ws.write(0, 8, 'Success Cases', self.style4)
            self.ws.write(0, 9, len(self.Actual_success_cases), self.style5)
            self.ws.write(0, 10, 'Failure Cases', self.style4)
            if failure_cases == 0:
                self.ws.write(0, 11, failure_cases, self.style5)
            else:
                self.ws.write(0, 11, failure_cases, self.style6)
            self.ws.write(0, 12, 'Success %', self.style4)
            self.ws.write(0, 13, percentage, self.style5)
            self.ws.write(0, 14, 'Time Taken (min)', self.style4)
            self.ws.write(0, 15, minutes, self.style5)
            self.wb_Result.save(test_data_inputpath.output['form_creation_output_report'])

        except Exception as error:
            api_logger.error(error)
