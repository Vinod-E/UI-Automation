import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.help_desk import query_excel
from scripts.crpo.common import button_click


class QueryConfig(query_excel.QueryExcelReadHelpDesk):
    def __init__(self):
        super(QueryConfig, self).__init__()

        self.req_name_breadcumb = ''

        self.ui_req_tab_he = ''
        self.ui_req_advance_search_he = ''
        self.ui_req_getbyid_he = ''
        self.ui_req_config_tab_he = ''
        self.ui_requirement_validation_he = ''
        self.ui_query_configuration = ''

    def query_configuration(self):
        try:
            self.requirement_tab()
            self.requirement_search()

            time.sleep(1)
            self.sub_tab('req_configuration_tab')
            self.ui_req_tab_he = 'Pass'
            self.ui_req_config_tab_he = 'Pass'

            self.sub_tab('req_query_config')
# validation ------
            self.web_element_text_xpath(page_elements.buttons['all_buttons'].format('Default Level Configuration'))
            if self.text_value == 'Default Level Configuration':
                self.ui_query_configuration = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def requirement_search(self):
        try:
            self.advance_search(page_elements.tabs['requirement_tab'])
            self.name_search(self.requirement_sprint_version, 'requirement')

            if self.search == 'Pass':
                self.ui_req_advance_search_he = 'Pass'

            time.sleep(1)
            self.requirement_getby_name(self.requirement_sprint_version)

            time.sleep(1.5)
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.getby_details_screen(self.requirement_sprint_version)
            if self.header_name.strip() == self.requirement_sprint_version:
                print('**-------->>> Requirement get by name is working')
                self.ui_req_getbyid_he = 'Pass'
                self.ui_requirement_validation_he = 'Pass'

        except Exception as search:
            ui_logger.error(search)
