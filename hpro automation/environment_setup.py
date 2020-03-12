from selenium import webdriver
from logger_settings import api_logger
import config
import datetime


class Environment(object):
    def __init__(self):

        self.login_server = input("Server name :: ")
        self.sprint_version = input("Enter the current sprint version :: ")

        try:
            self.driver = webdriver.Chrome(config.chrome)
            print("Run started at:: "+str(datetime.datetime.now()))
            print("Environment setup has been Done")
            print("**--------------------------------------------------------------**")

            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        except Exception as Environment_Error:
            api_logger.error(Environment_Error)

    def browser_close(self):
        print("**-------------------------------------------------------------**")
        print("Run completed at:: " + str(datetime.datetime.now()))
        print("Chrome environment Destroyed")
        self.driver.close()
