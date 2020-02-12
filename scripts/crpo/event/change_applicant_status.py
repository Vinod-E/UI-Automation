import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.event import event_applicants


class ChangeApplicantStatus(event_applicants.EventApplicants):
    def __init__(self):
        super(ChangeApplicantStatus, self).__init__()

        self.applicant_current_status = ''

        self.ui_change_applicant_status_action = []
        self.ui_applicant_current_status = []
        self.ui_current_status_validation = []

    def event_change_applicant_status(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.check_box()
            # --------------------------- Change Applicant Status -------------------
            self.applicant_status_change(self.xl_change_applicant_stage,
                                         self.xl_change_applicant_status,
                                         self.xl_change_status_comment)
            self.ui_change_applicant_status_action = 'Pass'

            # --------------------------- Applicant common process -----------------------------------------------------
            time.sleep(1.2)
            self.applicant_get_by()
            self.applicant_current_status_validation(self.change_applicant_status)
            self.ui_current_status_validation = 'Pass'

        except Exception as error:
            print(error)

    def applicant_current_status_validation(self, status):
        try:
            self.x_path_element_webdriver_wait(
                page_elements.event_applicant['applicant_validation'].format(status))
            self.applicant_current_status = self.xpath.text
            if self.applicant_current_status.strip() == status:
                self.ui_applicant_current_status = 'Pass'
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
                self.image_capture('applicant_status_failed_expected_{}'.format(status))
                print('<<<----- Image captured please check ----->>>')
            time.sleep(1)

        except Exception as error:
            api_logger.error(error)
