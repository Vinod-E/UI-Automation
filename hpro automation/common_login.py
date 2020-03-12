from logger_settings import api_logger
import webdriver_functions
import page_elements
import test_data_inputpath
import xlrd
import time
import config


class CommonLogin(webdriver_functions.WebdriverFunctions):
    def __init__(self):
        super(CommonLogin, self).__init__()

        self.login_details_file = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['login_credentials'])
        self._xl_tenant = []
        self.xl_username = []
        self.xl_password = []
        self._xl_rpo_tenant = []
        self.xl_rpo_password = []
        self._xl_pofu_tenant = []
        self.xl_pofu_password = []

        self.status_of_login = ""
        self.tenant_screen_text = ""
        self.invalid_details = "Please provide valid login name / email-id and password"

        # ------------------------------- Iterate Excel sheet ----------------------------------------------------------
        self.excel_read_based_on_server()

    def excel_read_loop(self, index):
        try:
            workbook = self.login_details_file
            sheet = workbook.sheet_by_index(index)
            for i in range(1, sheet.nrows):
                number = i  # Counting number of rows
                rows = sheet.row_values(number)

                if rows[0]:
                    self._xl_tenant.append(rows[0])
                if rows[1]:
                    self.xl_username.append(rows[1])
                if rows[2]:
                    self.xl_password.append(rows[2])
                if rows[3]:
                    self._xl_rpo_tenant.append(rows[3])
                if rows[4]:
                    self.xl_rpo_password.append(rows[4])
                if rows[5]:
                    self._xl_pofu_tenant.append(rows[5])
                if rows[6]:
                    self.xl_pofu_password.append(rows[6])
        except Exception as file_error:
            api_logger.error(file_error)

    def excel_read_based_on_server(self):
        # --------------------------------------amsin details-----------------------------------------------------------
        if self.login_server == 'amsin':
            self.excel_read_loop(0)
        # ----------------------------------------ams details-----------------------------------------------------------
        if self.login_server == 'betaams':
            self.excel_read_loop(1)
        # ----------------------------------------ams details-----------------------------------------------------------
        if self.login_server == 'ams':
            self.excel_read_loop(1)

    def tenant_alias_screen_validation(self):
        # --------------------------- Tenant screen verification by screen shot ----------------------------------------
        try:
            self.driver.get(config.sever_config['crpo'].format(self.login_server))

            self.x_path_element_webdriver_wait(page_elements.login['tenant_alias_page'])

            assert 'You are almost there' in self.xpath.text
            self.driver.save_screenshot(config.image_config['screen_shot'].format('CRPO_Tenant_Page'))
            print("Tenant page screen shot has been saved")

        except Exception as Tenant_Screen_Error:
            api_logger.error(Tenant_Screen_Error)

    def crpo_login_elements(self, tenant, password):
        try:
            self.name_element_webdriver_wait(page_elements.login['tenant'])
            self.name.send_keys(tenant)
            self.x_path_element_webdriver_wait(page_elements.login['next_button'])
            self.xpath.click()
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username)
            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(password)
            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()

            time.sleep(3)
            print("Application Login successfully")
            self.driver.save_screenshot(config.image_config['screen_shot'].format('CRPO_Login_Welcome_Page'))
            print("Login welcome page screen shot has been saved")
        except Exception as login_failed:
            api_logger.error(login_failed)

    def crpo_login(self):
        try:
            # ----------------------------------------AMSIN Login---------------------------------------------------
            if self.login_server == 'amsin':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_tenant, self.xl_password)
            # ----------------------------------------AMS Login---------------------------------------------------
            if self.login_server == 'ams':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_tenant, self.xl_password)
            # ------------------------------------------BETA Login---------------------------------------------------
            if self.login_server == 'betaams':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_tenant, self.xl_password)

        except Exception as crpo_login:
            api_logger.error(crpo_login)
        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            self.x_path_element_webdriver_wait(page_elements.login['login_success'])
            self.status_of_login = self.xpath.text
            assert self.status_of_login.strip() == 'administrator'
            print("**---------------------- In main screen ------------------------**")
        except Exception as login_status:
            api_logger.error(login_status)

    def crpo_logout(self):
        try:
            self.web_element_click_xpath(page_elements.login['login_success'])
            self.web_element_click_id(page_elements.login['logout'])
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.login['login_back'])
        except Exception as logout_status:
            api_logger.error(logout_status)

    def rpo_login(self):
        try:
            # ----------------------------------------AMSIN Login---------------------------------------------------
            if self.login_server == 'amsin':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_rpo_tenant, self.xl_rpo_password)
            # ----------------------------------------AMS Login---------------------------------------------------
            if self.login_server == 'ams':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_rpo_tenant, self.xl_rpo_password)
            # ------------------------------------------BETA Login---------------------------------------------------
            if self.login_server == 'betaams':
                self.tenant_alias_screen_validation()
                self.crpo_login_elements(self._xl_rpo_tenant, self.xl_rpo_password)

        except Exception as crpo_login:
            api_logger.error(crpo_login)
        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            self.x_path_element_webdriver_wait(page_elements.login['login_success'])
            self.status_of_login = self.xpath.text
            assert self.status_of_login.strip() == 'administrator'
            print("**---------------------- In main screen ------------------------**")
        except Exception as login_status:
            api_logger.error(login_status)

    def embrace_alias_screen_validation(self):
        # --------------------------- Tenant screen verification by screen shot ----------------------------------------
        try:
            self.driver.get(config.sever_config['embrace'].format(self.login_server))

            self.x_path_element_webdriver_wait(page_elements.embrace_login['tenant_alias_page'])

            assert 'Enter the Tenant Name for Authentication' in self.xpath.text
            self.driver.save_screenshot(config.image_config['screen_shot'].format('Embrace_Tenant_Page'))
            print("Tenant page screen shot has been saved")

        except Exception as Tenant_Screen_Error:
            api_logger.error(Tenant_Screen_Error)

    def embrace_login_elements(self):
        try:
            self.name_element_webdriver_wait(page_elements.login['tenant'])
            self.name.send_keys(self._xl_pofu_tenant)
            self.x_path_element_webdriver_wait(page_elements.embrace_login['next_button'])
            self.xpath.click()
            self.name_element_webdriver_wait(page_elements.embrace_login['username'])
            self.name.send_keys(self.xl_username)
            self.name_element_webdriver_wait(page_elements.embrace_login['password'])
            self.name.send_keys(self.xl_pofu_password)
            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()

            time.sleep(3)
            print("Application Login successfully")
            self.driver.save_screenshot(config.image_config['screen_shot'].format('CRPO_Login_Welcome_Page'))
            print("Login welcome page screen shot has been saved")
        except Exception as login_failed:
            api_logger.error(login_failed)

    def embrace_login(self):
        try:
            # ----------------------------------------AMSIN Login---------------------------------------------------
            if self.login_server == 'amsin':
                self.embrace_alias_screen_validation()
                self.embrace_login_elements()
            # ----------------------------------------AMS Login---------------------------------------------------
            if self.login_server == 'ams':
                self.embrace_alias_screen_validation()
                self.embrace_login_elements()
            # ------------------------------------------BETA Login---------------------------------------------------
            if self.login_server == 'betaams':
                self.embrace_alias_screen_validation()
                self.embrace_login_elements()

        except Exception as embrace_login:
            api_logger.error(embrace_login)
        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            self.x_path_element_webdriver_wait(page_elements.embrace_login['login_success'])
            self.status_of_login = self.xpath.text
            assert self.status_of_login.strip() == 'Administrator'
            print("**---------------------- In main screen ------------------------**")
        except Exception as login_status:
            api_logger.error(login_status)

    def server_connection_error(self):
        # ----------------------------------------- Server Connection error --------------------------------------------
        try:
            unable_to_reach_server = self.driver.find_element_by_xpath(page_elements.login['page_cant_be_reached'])
            try:
                assert 'This site' in unable_to_reach_server.text
                self.driver.save_screenshot(config.image_config['screen_shot'].format('server connection failed'))
                print("Server connection has been lost and screen shot saved")
            except Exception as error:
                api_logger.error(error)
        except Exception as error1:
            api_logger.error(error1)

    def internet_not_available(self):
        # ----------------------------------------- Internet Connection error ------------------------------------------
        try:
            internet_error = self.driver.find_element_by_xpath(page_elements.login['internet_error'])
            try:
                assert 'No Internet' in internet_error.text
                self.driver.save_screenshot(config.image_config['screen_shot'].format('No Internet'))
                print("No Internet connection and screen shot saved")
            except Exception as error:
                api_logger.error(error)
        except Exception as error2:
            api_logger.error(error2)
