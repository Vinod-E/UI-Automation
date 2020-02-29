import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.applicant_actions import job_applicants


class JobApplicantActions(job_applicants.JobApplicants):
    def __init__(self):
        super(JobApplicantActions, self).__init__()

    def job_change_applicant_status(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.check_box()
            # --------------------------- Change Applicant Status -------------------
            self.job_applicant_status_change(self.xl_stage_a, self.xl_status_a, self.xl_comment_a)
            self.glowing_messages('Applicant status changed successfully for selected Applicant(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_change_applicant_status_action_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)
