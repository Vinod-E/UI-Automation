import time
from logger_settings import api_logger
from scripts.embrace.form_creation import form_creation


class FormValidations(form_creation.FormCreation):
    def __init__(self):
        super(FormValidations, self).__init__()

        self.ui_candidate_name = []
        self.ui_date_time = []
        self.ui_college = []
        self.ui_gender = []
        self.ui_country = []
        self.ui_address = []
        self.ui_birth_date = []
        self.ui_current_time = []
        self.ui_python_tutorial = []
        self.ui_java_tutorial = []

        self.ui_candidate_name_label = []
        self.ui_date_time_label = []
        self.ui_college_label = []
        self.ui_gender_label = []
        self.ui_country_label = []
        self.ui_address_label = []
        self.ui_birth_date_label = []
        self.ui_current_time_label = []
        self.ui_python_tutorial_label = []
        self.ui_java_tutorial_label = []

        self.label = ''

    def finding_element(self, label):
        try:
            ui_label = self.driver.find_elements_by_xpath('//*[@for="formname"]')
            ui_label_data = []
            for i in ui_label:
                ui_label_data.append(i.text)
            print(ui_label_data)

            for j in ui_label_data:
                if j == label:
                    self.label = True
                    break
        except Exception as error:
            api_logger.error(error)

    def label_validation(self):
        try:
            self.finding_element(self.candidate_label)
            if self.label:
                self.ui_candidate_name_label = 'Pass'
                print("Element is a text label")

            self.finding_element(self.date_time_label)
            if self.label:
                self.ui_date_time_label = 'Pass'
                print("Element is a date time label")

            self.finding_element(self.college_label)
            if self.label:
                self.ui_college_label = 'Pass'
                print("Element is a college label")

            self.finding_element(self.gender_label)
            if self.label:
                self.ui_gender_label = 'Pass'
                print("Element is a gender label")

            self.finding_element(self.country_label)
            if self.label:
                self.ui_country_label = 'Pass'
                print("Element is a country label")

            self.finding_element(self.address_label)
            if self.label:
                self.ui_address_label = 'Pass'
                print("Element is a address label")

            self.finding_element(self.birth_label)
            if self.label:
                self.ui_birth_date_label = 'Pass'
                print("Element is a birth date label")

            self.finding_element(self.current_label)
            if self.label:
                self.ui_current_time_label = 'Pass'
                print("Element is a current time label")

            self.finding_element(self.python_label)
            if self.label:
                self.ui_python_tutorial_label = 'Pass'
                print("Element is a python label")

            self.finding_element(self.java_label)
            if self.label:
                self.ui_java_tutorial_label = 'Pass'
                print("Element is a java tutorial label")

        except Exception as e:
            print(e)

    def field_validation(self):
        try:
            if self.driver.find_element_by_name("candidate").get_attribute("type") == "text":
                print("Element is a text field")
                if self.xl_candidate_name == ['Text_field']:
                    self.ui_candidate_name = 'Pass'

            if self.driver.find_element_by_name("date").get_attribute("placeholder") == "Date":
                print("Element is a date time field")
                if self.xl_date_time == ['Date_Time']:
                    self.ui_date_time = 'Pass'

            if self.driver.find_element_by_name("college").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a drop_down field")
                if self.xl_college == ['Dropdown_field']:
                    self.ui_college = 'Pass'

            if self.driver.find_element_by_name("gender").get_attribute("type") == "radio":
                print("Element is a radio field")
                if self.xl_gender == ['Radio_field']:
                    self.ui_gender = 'Pass'

            if self.driver.find_element_by_name("country").get_attribute("type") == "checkbox":
                print("Element is a checkbox field")
                if self.xl_country == ['Checkbox_Field']:
                    self.ui_country = 'Pass'

            if self.driver.find_element_by_name("address").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a textarea field")
                if self.xl_address == ['TextArea_Field']:
                    self.ui_address = 'Pass'

            if self.driver.find_element_by_name("birth").get_attribute("ng-model") == "formControl.Value":
                print("Element is a birthdate field")
                if self.xl_birth_date == ['Date_Field']:
                    self.ui_birth_date = 'Pass'

            if self.driver.find_element_by_name("current").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a current time field")
                if self.xl_current_time == ['Time_Field']:
                    self.ui_current_time = 'Pass'

            if self.driver.find_element_by_name("python").get_attribute("type") == "text":
                print("Element is a video field")
                if self.xl_python_tutorial == ['Video_Field']:
                    self.ui_python_tutorial = 'Pass'

            if self.driver.find_element_by_xpath('//*[@ng-href="https://www.tutorialspoint.com'
                                                 '/java/java_basic_syntax.htm"]').get_attribute(
                'href') == 'https://www.tutorialspoint.com/java/java_basic_syntax.htm':

                print('Element is a link field')
                if self.xl_java_tutorial == ['Link_Field']:
                    self.ui_java_tutorial = 'Pass'

        except Exception as e:
            print(e)
