import page_elements
from logger_settings import api_logger
from scripts.crpo.common import menu_tabs


class GetByDetails(menu_tabs.MenuTabs):
    def __init__(self):
        super(GetByDetails, self).__init__()

    def __common(self, name):
        try:
            self.web_element_click_xpath(page_elements.getby_details['getbyid'].format(name))
            print('**-------->>> Entered into get by details screen')
        except Exception as getby:
            api_logger.error(getby)

    def event_getby_details(self):
        try:
            self.web_element_click_xpath(page_elements.getby_details['event_getbyid'])
            print('**-------->>> Entered into get by details screen')
        except Exception as getby:
            api_logger.error(getby)

    def job_getby_details(self, job_name):
        self.__common(job_name)

    def requirement_getby_details(self, requirement_name):
        self.__common(requirement_name)

    def applicant_getby_details(self, applicant_name):
        self.__common(applicant_name)
