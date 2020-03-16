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

    def validation(self):
        try:
            if self.driver.find_element_by_name("candidate").get_attribute("type") == "text":
                print("Element is a text field")
                self.ui_candidate_name = 'Pass'

            if self.driver.find_element_by_name("date").get_attribute("placeholder") == "Date":
                print("Element is a date time field")
                self.ui_date_time = 'Pass'

            if self.driver.find_element_by_name("college").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a drop_down field")
                self.ui_college = 'Pass'

            if self.driver.find_element_by_name("gender").get_attribute("type") == "radio":
                print("Element is a radio field")
                self.ui_gender = 'Pass'

            if self.driver.find_element_by_name("country").get_attribute("type") == "checkbox":
                print("Element is a checkbox field")
                self.ui_country = 'Pass'

            if self.driver.find_element_by_name("address").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a textarea field")
                self.ui_address = 'Pass'

            if self.driver.find_element_by_name("birth").get_attribute("ng-model") == "formControl.Value":
                print("Element is a birthdate field")
                self.ui_birth_date = 'Pass'

            if self.driver.find_element_by_name("current").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a current time field")
                self.ui_current_time = 'Pass'

            if self.driver.find_element_by_name("python").get_attribute("type") == "text":
                print("Element is a video field")
                self.ui_python_tutorial = 'Pass'

            if self.driver.find_element_by_xpath('//*[@ng-href="https://www.tutorialspoint.com'
                                                 '/java/java_basic_syntax.htm"]').get_attribute('href') == 'https://www.tutorialspoint.com/java/java_basic_syntax.htm':

                print('Element is a link field')
                self.ui_java_tutorial = 'Pass'

        except Exception as e:
            print(e)
