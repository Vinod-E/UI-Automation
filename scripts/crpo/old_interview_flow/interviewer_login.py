import time
import config
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import old_interview_excel


class InterviewerLogin(old_interview_excel.OldInterviewExcelRead):
    def __init__(self):
        super(InterviewerLogin, self).__init__()

    def interviewer_login(self, username, password):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            time.sleep(2)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.sever_config['crpo'].format(self.login_server))
            print("-------------------- New tab open with URL ------------------------")

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(username)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(password)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print("------------------ Interviewer1 Login successfully ------------------------")

        except Exception as login_error:
            api_logger.error(login_error)
