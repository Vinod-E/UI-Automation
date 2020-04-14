import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.requirement import create_requirement


class RequirementConfig(create_requirement.CreateRequirement):
    def __init__(self):
        super(RequirementConfig, self).__init__()

        self.ui_req_config_tab = []
        self.ui_req_duplicity_tab = []
        self.ui_req_duplicity = []
        self.ui_req_advance_search = []
        self.ui_req_getbyid = []

        self.dont_allow = ''

    def requirement_configuration_tab(self):
        try:
            self.requirement_validation('duplicity check')

            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.tabs['req_configuration_tab'])
            self.ui_req_config_tab = 'Pass'

            self.web_element_click_xpath(page_elements.tabs['req_duplicity_check'])
            self.ui_req_duplicity_tab = 'Pass'

            self.web_element_text_xpath(page_elements.buttons['dont_allow'])
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buttons['dont_allow'])

            # ----------------------------------- Validation -----------------------------------------------------------
            self.dont_allow = self.text_value
            if self.dont_allow == 'Dont Allow':
                print('**-------->>> Duplicity check configured')
                self.ui_req_duplicity = 'Pass'
            else:
                print('Failed to configure duplicity check <<<--------**')
            # ----------------------------------------------------------------------------------------------------------

            self.driver.execute_script("window.scrollTo(0,-100);")
            self.requirement_search()

        except Exception as config_message:
            ui_logger.error(config_message)

    def requirement_search(self):

        try:
            self.advance_search(page_elements.tabs['requirement_tab'])

            self.name_search(self.requirement_sprint_version, 'requirement')

            if self.search == 'Pass':
                self.ui_req_advance_search = 'Pass'

            time.sleep(1)
            self.requirement_getby_details(self.requirement_sprint_version)

            time.sleep(1)
            self.requirement_validation('getbyid')
            if self.req_name_breadcumb == self.requirement_sprint_version:
                print('**-------->>> Requirement get by name is working')
                self.ui_req_getbyid = 'Pass'

        except Exception as search:
            ui_logger.error(search)
