import config
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import check_box_selection


class Login(check_box_selection.CheckBox):
    def __init__(self):
        super(Login, self).__init__()
        self.staff_logging = ''

    def login(self, typeofuser, username, password):
        try:
            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(username)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(password)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print("******************** {} Login successfully ********************".format(typeofuser))

        except Exception as login_error:
            ui_logger.error(login_error)

    def staff_login_elements(self, tenant, username, password):
        try:
            self.web_element_send_keys_name(page_elements.embrace_login['username'], username)
            self.web_element_send_keys_name(page_elements.embrace_login['password'], password)
            self.web_element_click_xpath(page_elements.login['login_button'])

        except Exception as login_failed:
            ui_logger.error(login_failed)

    def staff_login(self, username, password, login_name_validate):
        try:
            # ----------------------------------------AMSIN Login---------------------------------------------------
            if self.login_server == 'amsin':
                self.driver.get(config.sever_config['embrace'].format(self.login_server))
                self.staff_login_elements(self._xl_tenant, username, password)
            # ----------------------------------------AMS Login---------------------------------------------------
            if self.login_server == 'ams':
                self.driver.get(config.sever_config['embrace'].format(self.login_server))
                self.staff_login_elements(self._xl_tenant, username, password)
            # ------------------------------------------BETA Login---------------------------------------------------
            if self.login_server == 'betaams':
                self.driver.get(config.sever_config['embrace'].format(self.login_server))
                self.staff_login_elements(self._xl_tenant, username, password)

        except Exception as embrace_login:
            ui_logger.error(embrace_login)
        # ---------------------------------------- Assertion for login -------------------------------------------------
        try:
            self.x_path_element_webdriver_wait(page_elements.embrace_login['login_success'])
            self.status_of_login = self.xpath.text
            assert login_name_validate in self.status_of_login.strip()
            self.staff_logging = 'True'
            print('Staffing login successfully with {}'.format(login_name_validate))
        except Exception as login_status:
            ui_logger.error(login_status)
