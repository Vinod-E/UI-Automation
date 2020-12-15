from scripts.embrace.form_creation import form_validation
from logger_settings import ui_logger

class CatalogValidations(form_validation.FormValidations):
    def __init__(self):
        super(CatalogValidations, self).__init__()
        self.college_dropdown_check = ''
        self.ui_college_dropdown = ''
        self.ui_college_dropdown_two = ''
        self.ui_college_dropdown_three = ''
        self.ui_college_dropdown_four = ''
        self.list_of_college_name = ''


    def college_catalogs(self):
        try:
            ui_college_catalog = self.driver.find_elements_by_name('college')[0]
            self.list_of_college_name = ui_college_catalog.text.split('\n')
            print(self.list_of_college_name)
            self.list_of_college_names = ', '.join(self.list_of_college_name)
            print(self.list_of_college_names)
            self.ui_college_dropdown = 'Pass'

            # for i in self.list_of_college_name:
            #     if i == college:
            #         print('college is {}'.format(college))
            #         self.college_dropdown_check = 'True'
            #         break

        except Exception as error:
            ui_logger.error(error)

    def college_catalog_validations(self):
        try:
            self.college_catalogs(self.college_one)
            if self.college_dropdown_check == 'True':
                self.ui_college_dropdown_one = 'Pass'
            self.college_catalogs(self.college_two)
            if self.college_dropdown_check == 'True':
                self.ui_college_dropdown_two = 'Pass'
            self.college_catalogs(self.college_three)
            if self.college_dropdown_check == 'True':
                self.ui_college_dropdown_three = 'Pass'
            self.college_catalogs(self.college_four)
            if self.college_dropdown_check == 'True':
                self.ui_college_dropdown_four = 'Pass'

        except Exception as error:
            api_logger.error(error)

