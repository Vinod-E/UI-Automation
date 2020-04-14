import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import interview_excel_old


class Login(interview_excel_old.OldInterviewExcelRead):
    def __init__(self):
        super(Login, self).__init__()

    def login(self, typeofuser, username, password):
        try:
            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.web_element_send_keys_name(page_elements.login['username'], username)

            self.web_element_send_keys_xpath(page_elements.login['password'], password)

            self.web_element_click_xpath(page_elements.login['login_button'])
            print("******************** {} Login successfully ********************".format(typeofuser))

        except Exception as login_error:
            ui_logger.error(login_error)
