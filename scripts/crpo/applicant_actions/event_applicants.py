import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.applicant_actions import applicant_action_excel


class ApplicantActions(applicant_action_excel.ApplicantActionsExcelRead):
    def __init__(self):
        super(ApplicantActions, self).__init__()

        self.validation_check = []

        self.ui_more_action = []
        self.ui_event_validation_check = []

        self.ui_event_tab_ea = []
        self.ui_advance_search_ea = []
        self.ui_event_details_ea = []
        self.ui_event_validation_ea = []
        self.ui_floating_action_ea = []
        self.ui_event_applicant_action_ea = []
        self.ui_applicant_advance_search_ea = []

    def more_actions(self):
        self.web_element_click_xpath(page_elements.applicant_actions['more_actions'])

    def event_tab_search(self):
        try:
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_a, 'Event')
            self.event_getby_details()
            self.event_validation('the event')
            self.floating_action()

            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.floating_actions['View_Applicants'])

            time.sleep(0.5)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_a, 'Applicant grid')

            # -------------------- output report values ----------------
            if self.validation_check == 'True':
                self.ui_event_tab_ea = 'Pass'
                self.ui_advance_search_ea = 'Pass'
                self.ui_event_details_ea = 'Pass'
                self.ui_event_validation_ea = 'Pass'
                self.ui_floating_action_ea = 'Pass'
                self.ui_event_applicant_action_ea = 'Pass'
                self.ui_applicant_advance_search_ea = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            time.sleep(0.5)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_a))
            if self.text_value.strip() == self.event_sprint_version_a:
                self.validation_check = 'True'
                self.ui_event_validation_check = 'Pass'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.text_value.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            ui_logger.error(e)
