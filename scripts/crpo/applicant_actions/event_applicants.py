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
            self.event_getby_name()
            self.getby_details_screen(self.event_sprint_version_a)
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.actions_dropdown()
            time.sleep(0.5)
            self.floating_action('View_Applicants')

            time.sleep(0.5)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_a, 'Applicant grid')

            # -------------------- output report values ----------------
            if self.header_name.strip() == self.event_sprint_version_a:
                print('**-------->>> Event get by name is working')
                self.ui_event_tab_ea = 'Pass'
                self.ui_advance_search_ea = 'Pass'
                self.ui_event_details_ea = 'Pass'
                self.ui_event_validation_ea = 'Pass'
                self.ui_floating_action_ea = 'Pass'
                self.ui_event_applicant_action_ea = 'Pass'
                self.ui_applicant_advance_search_ea = 'Pass'

        except Exception as error:
            ui_logger.error(error)
