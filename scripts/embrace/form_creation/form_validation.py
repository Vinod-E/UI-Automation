from scripts.embrace.form_creation import form_creation


class FormValidations(form_creation.FormCreation):
    def __init__(self):
        super(FormValidations, self).__init__()

    def validation(self):
        try:
            if self.driver.find_element_by_name("candidate").get_attribute("type") == "text":
                print("Element is a text field")

            if self.driver.find_element_by_name("date").get_attribute("placeholder") == "Date":
                print("Element is a date time field")

            if self.driver.find_element_by_name("college").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a drop_down field")

            if self.driver.find_element_by_name("gender").get_attribute("type") == "radio":
                print("Element is a radio field")

            if self.driver.find_element_by_name("country").get_attribute("type") == "checkbox":
                print("Element is a checkbox field")

            if self.driver.find_element_by_name("address").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a textarea field")

            if self.driver.find_element_by_name("birth").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a birthdate field")

            if self.driver.find_element_by_name("current").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a current time field")

            if self.driver.find_element_by_name("python").get_attribute("type") == "text":
                print("Element is a video field")

            if self.driver.find_element_by_xpath('//*[@ng-href="https://www.tutorialspoint.com'
                                                 '/java/java_basic_syntax.htm"]').get_attribute('href') == 'https://www.tutorialspoint.com/java/java_basic_syntax.htm':

                print('Element is a link field')

        except Exception as e:
            print(e)
