import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import interview_excel_old


class Login(interview_excel_old.OldInterviewExcelRead):
    def __init__(self):
        super(Login, self).__init__()

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
            api_logger.error(login_error)
