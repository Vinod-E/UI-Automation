import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.help_desk import query_excel


class QueryConfig(query_excel.QueryExcelReadHelpDesk):
    def __init__(self):
        super(QueryConfig, self).__init__()

        self.req_name_breadcumb = ''

        self.ui_req_tab_he = []
        self.ui_req_advance_search_he = []
        self.ui_req_getbyid_he = []
        self.ui_req_config_tab_he = []
        self.ui_requirement_validation_he = []

    def query_configuration(self):
        try:
            self.requirement_tab()
            self.requirement_search()

            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.tabs['req_configuration_tab'])
            self.ui_req_tab_he = 'Pass'
            self.ui_req_config_tab_he = 'Pass'

            self.web_element_click_xpath(page_elements.tabs['req_query_config'])

        except Exception as error:
            api_logger.error(error)

    def requirement_search(self):

        try:
            self.advance_search(page_elements.tabs['requirement_tab'])

            self.name_search(self.requirement_sprint_version, 'requirement')

            if self.search == 'Pass':
                self.ui_req_advance_search_he = 'Pass'

            time.sleep(1)
            self.requirement_getby_details(self.requirement_sprint_version)

            time.sleep(1)
            self.requirement_validation('getbyid')
            if self.req_name_breadcumb == self.requirement_sprint_version:
                print('**-------->>> Requirement get by name is working')
                self.ui_req_getbyid_he = 'Pass'

        except Exception as search:
            api_logger.error(search)

    def requirement_validation(self, config_name):

        try:
            time.sleep(1)
            self.web_element_text_xpath(page_elements.requirement_validations['requirement_name_breadcumb'])
            self.req_name_breadcumb = self.text_value
        except Exception as e1:
            api_logger.error(e1)

        if self.req_name_breadcumb == self.requirement_sprint_version:
            self.ui_requirement_validation_he = 'Pass'
            print('**-------->>> Req Validated and continuing '
                  'with {} to created requirement :: {}'.format(config_name, self.req_name_breadcumb))
        else:
            print('Req validation failed Or Req creation failed <<<--------**')
