import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.manage_interviewers import manage_excel


class CriteriaConfig(manage_excel.ManageInterviewExcelRead):
    def __init__(self):
        super(CriteriaConfig, self).__init__()

        self.get_event_name = ''
        self.event_validation_check = ''

        self.ui_event_tab_mi = []
        self.ui_advance_search_mi = []
        self.ui_event_details_mi = []
        self.ui_event_validation_mi = []
        self.ui_floating_action_mi = []
        self.ui_manage_interviews_action_mi = []

    def event_search(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_mi, 'Event')
            self.event_getby_details()
            self.event_validation('Manage Interviewers')
            self.floating_action()
            self.web_element_click_xpath(page_elements.floating_actions['manage_interviewers'])

            # -------------------- output report values ----------------
            if self.get_event_name.strip() == self.event_sprint_version_mi:
                self.ui_event_tab_mi = 'Pass'
                self.ui_advance_search_mi = 'Pass'
                self.ui_event_details_mi = 'Pass'
                self.ui_event_validation_mi = 'Pass'
                self.ui_floating_action_mi = 'Pass'
                self.ui_manage_interviews_action_mi = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_mi))
            self.get_event_name = self.text_value

            if self.get_event_name.strip() == self.event_sprint_version_mi:
                self.event_validation_check = 'True'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            api_logger.error(e)
