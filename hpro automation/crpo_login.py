from selenium.common import exceptions
import environment_setup
import page_elements
import test_data_inputpath
import xlrd
import time
import config


class CrpoLogin(environment_setup.Environment):
    def __init__(self):
        super(CrpoLogin, self).__init__()

        self.xl_amsin_tenant = []
        self.xl_amsin_username = []
        self.xl_amsin_password = []

        self.xl_ams_tenant = []
        self.xl_ams_username = []
        self.xl_ams_password = []

        self.status_of_login = ""
        self.tenant_screen_text = ""
        self.invalid_details = "Please provide valid login name / email-id and password"

    def excel_read(self):
        # ----------------
        # Excel Data Read
        # ----------------

        # --------------------------------------amsin details-----------------------------------------------------------
        if self.login_server == 'amsin':
            workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['credentials_file'])
            sheet1 = workbook.sheet_by_index(0)
            for i in range(1, sheet1.nrows):
                number = i  # Counting number of rows
                rows = sheet1.row_values(number)

                if rows[0]:
                    self.xl_amsin_tenant.append(rows[0])
                if rows[1]:
                    self.xl_amsin_username.append(rows[1])
                if rows[2]:
                    self.xl_amsin_password.append(rows[2])

        # ----------------------------------------ams details-----------------------------------------------------------
        if self.login_server == 'beta':
            workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['credentials_file'])
            sheet1 = workbook.sheet_by_index(1)
            for j in range(1, sheet1.nrows):
                number = j  # Counting number of rows
                rows = sheet1.row_values(number)

                if rows[0]:
                    self.xl_ams_tenant.append(rows[0])
                if rows[1]:
                    self.xl_ams_username.append(rows[1])
                if rows[2]:
                    self.xl_ams_password.append(rows[2])

        # ----------------------------------------ams details-----------------------------------------------------------
        if self.login_server == 'ams':
            workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['credentials_file'])
            sheet1 = workbook.sheet_by_index(1)
            for j in range(1, sheet1.nrows):
                number = j  # Counting number of rows
                rows = sheet1.row_values(number)

                if rows[0]:
                    self.xl_ams_tenant.append(rows[0])
                if rows[1]:
                    self.xl_ams_username.append(rows[1])
                if rows[2]:
                    self.xl_ams_password.append(rows[2])

    def crpo_login(self):

        try:
            # ----------------------------------------AMSIN Login---------------------------------------------------
            if self.login_server == 'amsin':
                self.driver.find_element_by_name(page_elements.login['tenant']).send_keys(self.xl_amsin_tenant)
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.login['next_button']).click()
                self.driver.find_element_by_name(page_elements.login['username'])\
                    .send_keys(self.xl_amsin_username)
                self.driver.find_element_by_xpath(page_elements.login['password'])\
                    .send_keys(self.xl_amsin_password)
                self.driver.find_element_by_xpath(page_elements.login['login_button']).click()
                time.sleep(3)
                print "Application Login in successfully"
                self.driver.save_screenshot(config.configs['screen_shot'].format('CRPO_Login_Welcome_Page'))
                print("Login welcome page screen shot has been saved")

            # ----------------------------------------AMS Login---------------------------------------------------
            if self.login_server == 'ams':
                self.driver.find_element_by_name(page_elements.login['tenant']).send_keys(self.xl_ams_tenant)
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.login['next_button']).click()
                self.driver.find_element_by_name(page_elements.login['username']).send_keys(self.xl_ams_username)
                self.driver.find_element_by_xpath(page_elements.login['password']) \
                    .send_keys(self.xl_ams_password)
                self.driver.find_element_by_xpath(page_elements.login['login_button']).click()
                time.sleep(3)
                print "Application Login in successfully"
                self.driver.save_screenshot(config.configs['screen_shot'].format('CRPO_Login_Welcome_Page'))
                print("Login welcome page screen shot has been saved")

            # ------------------------------------------BETA Login---------------------------------------------------
            if self.login_server == 'beta':
                self.driver.find_element_by_name(page_elements.login['tenant']).send_keys(self.xl_ams_tenant)
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.login['next_button']).click()
                self.driver.find_element_by_name(page_elements.login['username']).send_keys(self.xl_ams_username)
                self.driver.find_element_by_xpath(page_elements.login['password'])\
                    .send_keys(self.xl_ams_password)
                self.driver.find_element_by_xpath(page_elements.login['login_button']).click()
                time.sleep(3)
                print "Application Login in successfully"
                self.driver.save_screenshot(config.configs['screen_shot'].format('CRPO_Login_Welcome_Page'))
                print("Login welcome page screen shot has been saved")
        except exceptions.NoSuchElementException as crpo_login:
            print(crpo_login)

        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            login_status = self.driver.find_element_by_xpath(page_elements.login['login_success'])
            self.status_of_login = login_status.text
            assert self.status_of_login == 'administrator'
            print ("**---------------------- In main screen ------------------------**")
        except exceptions.NoSuchElementException as login_status1:
            print login_status1

    def server_connection_error(self):
        # ----------------------------------------- Server Connection error --------------------------------------------
        try:
            unable_to_reach_server = self.driver.find_element_by_xpath(
                page_elements.login['page_cant_be_reached'])
            try:
                assert 'This site' in unable_to_reach_server.text
                self.driver.save_screenshot(config.configs['screen_shot'].format('server connection failed'))
                print("Server connection has been lost and screen shot saved")
            except AssertionError as error:
                print error
        except exceptions.WebDriverException as error1:
            print error1

    def internet_not_available(self):
        # ----------------------------------------- Internet Connection error ------------------------------------------
        try:
            internet_error = self.driver.find_element_by_xpath(
                page_elements.login['internet_error'])
            try:
                assert 'No Internet' in internet_error.text
                self.driver.save_screenshot(config.configs['screen_shot'].format('No Internet'))
                print("No Internet connection and screen shot saved")
            except AssertionError as error:
                print error
        except exceptions.WebDriverException as error2:
            print error2


# Object = CrpoLogin()
# Object.excel_read()
# Object.crpo_login()
# Object.browser_close()
# if Object.status_of_login != 'administrator':
#     Object.server_connection_error()
#     Object.browser_close()
