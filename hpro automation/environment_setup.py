from selenium import webdriver
from selenium.common import exceptions
import config
import datetime
import page_elements


class Environment(object):
    def __init__(self):

        self.login_server = raw_input("Server name ::")
        login_browser = raw_input("Browser name ::")
        self.sprint_version = raw_input("Enter the current sprint version :: ")

        try:
            self.driver = webdriver.Chrome(config.configs[login_browser])
            print("Run started at:: "+str(datetime.datetime.now()))
            print("Environment setup has been Done")
            print("**--------------------------------------------------------------**")

            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(config.configs[self.login_server])

        except exceptions.WebDriverException as Environment_Error:
            print(Environment_Error)

        # --------------------------- Tenant screen verification by screen shot ----------------------------------------
        try:
            tenant_screen = self.driver.find_element_by_xpath(page_elements.login['tenant_alias_page'])

            assert 'You are almost there' in tenant_screen.text
            self.driver.save_screenshot(config.configs['screen_shot'].format('CRPO_Tenant_Page'))
            print("Tenant page screen shot has been saved")

        except exceptions.WebDriverException as Environment_Error:
            print(Environment_Error)

    def browser_close(self):
        print("**-------------------------------------------------------------**")
        print("Run completed at:: " + str(datetime.datetime.now()))
        print("Chrome environment Destroyed")

        self.driver.close()
