import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.applicant_actions import event_applicants


class ApplicantActions(event_applicants.ApplicantActions):
    def __init__(self):
        super(ApplicantActions, self).__init__()

        self.ui_change_applicant_status_action_a = []

    def event_change_applicant_status(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.check_box()
            # --------------------------- Change Applicant Status -------------------
            self.applicant_status_change(self.xl_stage_a,
                                         self.xl_status_a,
                                         self.xl_comment_a)
            self.ui_change_applicant_status_action_a = 'Pass'

        except Exception as e:
            api_logger.error(e)


o = ApplicantActions()
o.crpo_login()
o.event_tab_search()
o.event_change_applicant_status()
