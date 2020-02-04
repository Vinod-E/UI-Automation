import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.event import upload_candidates


class EventApplicants(upload_candidates.EventUploadCandidates):
    def __init__(self):
        super(EventApplicants, self).__init__()

        self.applicant_in_event = ''
        self.applicant_hopping = ''

        self.ui_event_advance_search = []
        self.ui_event_applicants_action = []
        self.ui_applicant_advance_search = []
        self.ui_applicant_getby = []
        self.ui_candidate_details_validation = []

    def event_applicants(self):

        try:
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version, 'Event')
            self.ui_event_advance_search = 'Pass'

            self.event_getby_details()

        except Exception as error:
            api_logger.error(error)

# ------ Event applicants
        self.event_validation('event applicants')
        if self.validation_check == 'True':
            try:
                time.sleep(2)
                self.floating_action()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['View_Applicants'])
                self.xpath.click()
                self.ui_event_applicants_action = 'Pass'

                # --------------------------- Applicant Advance search -------------------------------------------------
                self.applicant_advance_search()
                self.applicant_name_search(self.event_sprint_version, 'Applicant grid')
                self.ui_applicant_advance_search = 'Pass'

                # --------------------------- Applicant Grid ------------------------------------------------------
                self.applicant_get_by()
                self.ui_applicant_getby = 'Pass'

                # -------------------- applicant validations -----------------------------------------------------------
                self.applicant_event_validation()
                self.applicant_hopping_validation()
                self.ui_candidate_details_validation = 'Pass'

                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
            except Exception as error:
                api_logger.error(error)

    def applicant_get_by(self):
        try:
            time.sleep(3)
            self.applicant_getby_details(self.event_sprint_version)
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as error:
            api_logger.error(error)

    def applicant_event_validation(self,):
        try:
            self.x_path_element_webdriver_wait(
                page_elements.event_applicant['applicant_validation'].format(self.event_sprint_version))
            self.applicant_in_event = self.xpath.text
            if self.applicant_in_event.strip() == self.event_sprint_version:
                print('**-------->>> Applicant tagged to respected event :: {}'.format(self.applicant_in_event))
            else:
                print('Applicant is tagged to wrong event <<<---------**')
            time.sleep(1)

        except Exception as error:
            api_logger.error(error)

    def applicant_hopping_validation(self):
        try:
            self.x_path_element_webdriver_wait(
                page_elements.event_applicant['applicant_validation'].format(self.hopping_positive_status))
            self.applicant_hopping = self.xpath.text
            if self.applicant_hopping == self.hopping_positive_status:
                print('**-------->>> Applicant movement happened '
                      'through hopping in event :: {}'.format(self.applicant_in_event))
            else:
                print('Failed in applicant hopping <<<---------**')
            time.sleep(2)

        except Exception as error:
            api_logger.error(error)
