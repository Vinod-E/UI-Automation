import page_elements
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import create_job_role


class CreateRequirement(create_job_role.CreateJobRole):
    def __init__(self):
        super(CreateRequirement, self).__init__()

        self.requirement_name = []
        self.job_name = []
        self.xl_hiring_track = []
        self.xl_college_type = []

        self.requirement_sprint_version = []
        self.job_sprint_version = []

        self.req_name_breadcumb = ""

        self.ui_create_requirement = []
        self.ui_req_advance_search = []
        self.ui_req_getbyid = []
        self.ui_req_config_tab = []
        self.ui_req_duplicity = []

        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_requirement'])
        if self.login_server == 'beta':
            self.req_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.req_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.req_sheet1 = workbook.sheet_by_index(0)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def job_creation(self):
        self.job_excel_read()
        self.create_job_role()
        # self.job_advance_search()
        self.selection_process()
        self.feedback_form()
        self.tag_interview_panel()
        self.ec_configurations_tab()
        self.task_configurations_tab()
        self.job_automation()

    def requirement_excel_read(self):

        # --------------------------------------requirement details-----------------------------------------------------
        for i in range(1, self.req_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.req_sheet1.row_values(number)

            if rows[0]:
                self.requirement_name.append(rows[0])
            if rows[1]:
                self.job_name.append(rows[1])
            if rows[2]:
                self.xl_hiring_track.append(rows[2])
            if rows[3]:
                self.xl_college_type.append(rows[3])

            for k in self.job_name:
                job_name = k
                self.job_sprint_version = job_name.format(self.sprint_version)
            for j in self.requirement_name:
                requirement_name = j
                self.requirement_sprint_version = requirement_name.format(self.sprint_version)

    def create_requirement(self):

        try:
            self.driver.refresh()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath(page_elements.requirement['requirement_tab']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.requirement['create_requirement']).click()

            time.sleep(2)
            req_name = self.driver.find_element_by_xpath(page_elements.requirement['requirement_name'])
            req_name.send_keys(self.job_sprint_version)

            time.sleep(3)
            job_field = self.driver.find_element_by_xpath(page_elements.requirement['job_role_selection'])
            job_field.click()

            time.sleep(3)
            req_job_name_search = self.driver.find_element_by_xpath(page_elements.requirement['job_role_search'])
            req_job_name_search.send_keys(self.requirement_sprint_version)

            all_selection_button = self.driver.find_element_by_xpath(page_elements.requirement['job_select'])
            all_selection_button.click()

            time.sleep(2)
            done = self.driver.find_element_by_xpath(page_elements.requirement['jod_selection_done'])
            done.click()

            track = self.driver.find_element_by_xpath(page_elements.requirement['Hiring_track'])
            track.send_keys(self.xl_hiring_track)
            track.send_keys(Keys.ARROW_DOWN)
            track.send_keys(Keys.ENTER)

            college_type = self.driver.find_element_by_xpath(page_elements.requirement['college_type'])
            college_type.send_keys(self.xl_college_type)
            college_type.send_keys(Keys.ARROW_DOWN)
            college_type.send_keys(Keys.ENTER)

            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.requirement['requirement_create_button']).click()
            print(' Requirement created successfully ')
            self.ui_create_requirement = 'Pass'

        except exceptions.WebDriverException as create_req:
            print create_req

        # try:
        #     req_name_from_breadcrumb = self.driver.find_element_by_xpath(
        #         page_elements.requirement['req_name_breadcrumbs'])
        #     req_name_from_breadcrumb.send_keys(Keys.UP)
        #     self.req_name_breadcumb = req_name_from_breadcrumb.text
        # except exceptions.NoSuchElementException as e1:
        #     print (e1)

        # if self.req_name_breadcumb == self.requirement_sprint_version:
        #     print(' Requirement created successfully ')
        # else:
        #     print('-----------------Failed to create Requirement-----------------')

    def req_advance_search(self):
        try:
            self.driver.find_element_by_xpath(page_elements.requirement['requirement_tab']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.requirement['req_advance_search']).click()

            name = self.driver.find_element_by_name(page_elements.requirement['req_search_name_field'])
            name.click()
            name.send_keys(self.requirement_sprint_version)
            time.sleep(2)

            self.driver.find_element_by_xpath(page_elements.requirement['req_search_button']).click()
            time.sleep(5)
            print('----------------- Req advance search is working ------------------')
            self.ui_req_advance_search = 'Pass'

            getbyid = self.driver.find_element_by_xpath(
                page_elements.requirement['req_name_getbyid'].format(self.requirement_sprint_version))
            getbyid.click()
            print('----------------- req getbyid functionality is working ---------------')
            self.ui_req_getbyid = 'Pass'

            time.sleep(3)
        except exceptions.WebDriverException as search:
            print search

    def req_configuration_tab(self):
        try:
            self.driver.implicitly_wait(10)
            config = self.driver.find_element_by_xpath(page_elements.requirement['req_config_tab'])
            config.click()
            print('------------------- configuration tab functionality is working -------------------')
            self.ui_req_config_tab = 'Pass'

            time.sleep(3)
            duplicity = self.driver.find_element_by_xpath(page_elements.requirement['req_duplicity_check'])
            duplicity.click()

            time.sleep(4)
            duplicity_dont_allow = self.driver.find_element_by_xpath(
                page_elements.requirement['req_duplicity_dont_allow'])
            duplicity_dont_allow.click()
            time.sleep(5)
            print('------------------- Duplicity configured ----------------')
            self.ui_req_duplicity = 'Pass'

        except exceptions.ElementClickInterceptedException as config_message:
            print(config_message)


# Object = CreateRequirement()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.requirement_excel_read()
#     Object.create_requirement()
#     Object.req_configuration_tab()
#     Object.req_advance_search()
#     Object.browser_close()
# else:
#     Object.server_connection_error()
#     Object.browser_close()
