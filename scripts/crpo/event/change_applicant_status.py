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
            self.name_element_webdriver_wait(page_elements.grid['check_box'])
            self.name.click()

            # --------------------------- Change Applicant Status -------------------
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(2)

            self.x_path_element_webdriver_wait(page_elements.event_applicant['Change_applicant_status'])
            self.xpath.click()
            self.ui_change_applicant_status_action = 'Pass'

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event_applicant['change_stage'])
            self.xpath.send_keys(self.xl_change_applicant_stage)

            self.x_path_element_webdriver_wait(page_elements.event_applicant['change_status'])
            self.xpath.send_keys(self.xl_change_applicant_status)

            self.x_path_element_webdriver_wait(page_elements.event_applicant['comment'])
            self.xpath.send_keys(self.xl_change_status_comment)

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['status_change_button'])
            self.xpath.click()

            # --------------------------- Applicant common process -----------------------------------------------------
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
            time.sleep(1)

        except Exception as error:
            api_logger.error(error)
