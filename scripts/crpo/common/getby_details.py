import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import menu_tabs


class GetByDetails(menu_tabs.MenuTabs):
    def __init__(self):
        super(GetByDetails, self).__init__()

    def __common(self, name):
        try:
            self.web_element_click_xpath(page_elements.getby_details['getbyid'].format(name))
            print('**-------->>> Entered into get by details screen')
        except Exception as getby:
            ui_logger.error(getby)

    def event_getby_name(self):
        try:
            self.web_element_click_xpath(page_elements.getby_details['event_getbyid'])
            print('**-------->>> Entered into get by details screen')
        except Exception as getby:
            ui_logger.error(getby)

    def job_getby_name(self, job_name):
        self.__common(job_name)

    def requirement_getby_name(self, requirement_name):
        self.__common(requirement_name)

    def applicant_getby_name(self, applicant_name):
        self.__common(applicant_name)

# ------------------------- In details screen ---------------------------------
    def __details_screen(self, name):
        try:
            self.web_element_text_xpath(page_elements.getby_details['getbyid'].format(name))
            self.header_name = self.text_value
            if self.header_name.strip() == name:
                print('**-------->>> In the details page of created:: {}'.format(name))
        except Exception as getby:
            ui_logger.error(getby)

    def getby_details_screen(self, event_name):
        self.__details_screen(event_name)
