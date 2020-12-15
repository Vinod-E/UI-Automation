import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.requirement import create_requirement
from scripts.crpo.common import button_click


class RequirementConfig(create_requirement.CreateRequirement):
    def __init__(self):
        super(RequirementConfig, self).__init__()

        self.ui_req_config_tab = ''
        self.ui_req_duplicity_tab = ''
        self.ui_req_duplicity = ''
        self.ui_req_advance_search = ''
        self.ui_req_getbyid = ''

        self.dont_allow = ''

    def requirement_configuration_tab(self):
        self.getby_details_screen(self.requirement_sprint_version)
        if self.header_name.strip() == self.requirement_sprint_version:
            print('**-------->>> Req Validated and continuing '
                  'with the configuration to :: {}'.format(self.requirement_sprint_version))
        try:
            time.sleep(0.5)
            self.sub_tab('req_configuration_tab')
            self.ui_req_config_tab = 'Pass'

            self.sub_tab('req_duplicity_check')
            self.ui_req_duplicity_tab = 'Pass'

            time.sleep(0.5)
            button_click.all_buttons(self, 'Dont Allow')

            # ----------------------------------- Validation -----------------------------------------------------------
            self.web_element_text_xpath(page_elements.buttons['all_buttons'].format('Dont Allow'))
            self.dont_allow = self.text_value
            if self.dont_allow.strip() == 'Dont Allow':
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
            self.requirement_getby_name(self.requirement_sprint_version)

            time.sleep(1)
            self.getby_details_screen(self.requirement_sprint_version)
            if self.header_name.strip() == self.requirement_sprint_version:
                print('**-------->>> Requirement get by name is working')
                self.ui_req_getbyid = 'Pass'

        except Exception as search:
            ui_logger.error(search)
