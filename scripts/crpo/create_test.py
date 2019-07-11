import crpo_login
import time
import xlrd
from selenium.common import exceptions
import test_data_inputpath
import page_elements
from datetime import datetime
import create_requirement


class CreateTest(create_requirement.CreateRequirement):
    def __init__(self):
        super(CreateTest, self).__init__()
        now = datetime.now()
        self.xl_test_from_date = now.strftime("%d/%m/%Y")
        self.xl_test_to_date = now.strftime("%d/%m/%Y")

        self.xl_clone_test = []
        self.xl_new_test_name = []
        self.grid_test_name = ""
        self.loop_v = ''
        self.test_name_sprint_version = []

        self.ui_test_advance_search = []
        self.ui_test_clone = []

        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['clone_test'])
        if self.login_server == 'beta':
            self.test_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.test_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.test_sheet1 = workbook.sheet_by_index(1)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def test_excel_read(self):
        # --------------------------------------test details------------------------------------------------------------
        for i in range(1, self.test_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.test_sheet1.row_values(number)

            if rows[0]:
                self.xl_clone_test.append(rows[0])
            if rows[1]:
                self.xl_new_test_name.append(rows[1])

            for j in self.xl_new_test_name:
                job_name = j
                self.test_name_sprint_version = job_name.format(self.sprint_version)

    def test_advance_search(self):
        try:
            self.driver.implicitly_wait(5)
            test_tab = self.driver.find_element_by_xpath(page_elements.test['assessment_tab'])
            test_tab.click()
            time.sleep(5)
            search = self.driver.find_element_by_xpath(page_elements.test['assess_advance_search'])
            search.click()
            name = self.driver.find_element_by_name(page_elements.test['assessment_name'])
            name.send_keys(self.xl_clone_test)
            time.sleep(2)
            button = self.driver.find_element_by_xpath(page_elements.test['assess_search_button'])
            button.click()
            time.sleep(5)
            print('--------------- Advance search is working --------------------')
            self.ui_test_advance_search = 'Pass'

            # ------------------------------ validating the test name --------------------------------------------------
            try:
                for i in self.xl_clone_test:
                    self.loop_v = i
                    test_name = self.driver.find_element_by_xpath(
                        page_elements.test['grid_test_name'].format(self.loop_v))
                    self.grid_test_name = test_name.text
            except exceptions.ElementNotInteractableException as e:
                print(e)

        except exceptions.ElementClickInterceptedException as error:
            print(error)

    def clone_test(self):

        if self.grid_test_name == self.loop_v:
            print('---------------------------------------Test name is validated --------------------------------')

            try:
                self.driver.implicitly_wait(5)
                more_actions = self.driver.find_element_by_xpath(page_elements.test['more_actions'])
                more_actions.click()
                time.sleep(2)

                clone_action = self.driver.find_element_by_xpath(page_elements.test['clone_test_action'])
                clone_action.click()
                time.sleep(3)

                new_test_name = self.driver.find_element_by_name(page_elements.test['assessment_name'])
                new_test_name.send_keys(self.test_name_sprint_version)

                time.sleep(4)
                from_date = self.driver.find_element_by_xpath(page_elements.test['from_date'])
                from_date.send_keys(self.xl_test_from_date)

                to_date = self.driver.find_element_by_xpath(page_elements.test['to_date'])
                to_date.send_keys(self.xl_test_to_date)

                clone_save_button = self.driver.find_element_by_xpath(page_elements.test['clone/save'])
                clone_save_button.click()
                time.sleep(5)

                print('---------------- Clone/Creation of test successfully ----------------')
                self.ui_test_clone = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)
        else:
            print('--------------- failed to create test ---------------------')


# Object = CreateTest()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.test_excel_read()
#     Object.test_advance_search()
#     Object.clone_test()
#     Object.browser_close()
