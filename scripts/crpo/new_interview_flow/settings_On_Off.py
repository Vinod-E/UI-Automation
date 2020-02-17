import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import new_interview_excel


class Settings(new_interview_excel.NewInterviewExcelRead):
    def __init__(self):
        super(Settings, self).__init__()

        self.ui_common_settings = []
        self.ui_settings = []
        self.interview_module = []
        self.ui_new_feedback_enable = []
        self.ui_new_feedback_disable = []

    def new_feedback_on(self):
        try:
            # ----- settings part
            time.sleep(2)
            self.settings(page_elements.setting_modules['interview_module'])
            time.sleep(1.5)
            self.enable_new_feedback_form(page_elements.setting_modules['On'],
                                          'Enable')
            if self.enable_disable_validation == 'True':
                self.ui_common_settings = 'Pass'
                self.ui_settings = 'Pass'
                self.interview_module = 'Pass'
                self.ui_new_feedback_enable = 'Pass'
        except Exception as error:
            api_logger.error(error)

    def new_feedback_off(self):
        try:
            # ----- settings part
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.settings(page_elements.setting_modules['interview_module'])
            time.sleep(1.5)
            self.enable_new_feedback_form(page_elements.setting_modules['Off'],
                                          'Disable')
            if self.enable_disable_validation == 'True':
                self.ui_common_settings = 'Pass'
                self.ui_settings = 'Pass'
                self.interview_module = 'Pass'
                self.ui_new_feedback_disable = 'Pass'
        except Exception as error:
            api_logger.error(error)
