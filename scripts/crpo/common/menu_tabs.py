import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import applicant_status_change


class MenuTabs(applicant_status_change.ChangeStatus):
    def __init__(self):
        super(MenuTabs, self).__init__()

    def event_tab(self):
        try:
            self.web_element_click_xpath(page_elements.tabs['event_tab'])
        except Exception as error:
            ui_logger.error(error)

    def job_tab(self):
        try:
            time.sleep(1.5)
            self.web_element_click_xpath(page_elements.tabs['job_tab'])
        except Exception as error:
            ui_logger.error(error)

    def requirement_tab(self):
        try:
            time.sleep(1.5)
            self.web_element_click_xpath(page_elements.tabs['requirement_tab'])
        except Exception as error:
            ui_logger.error(error)

    def assessment_tab(self):
        try:
            self.web_element_click_xpath(page_elements.tabs['assessment_tab'])
        except Exception as error:
            ui_logger.error(error)

    def more_tab(self):
        try:
            self.web_element_click_xpath(page_elements.tabs['more_tabs'])
        except Exception as error:
            ui_logger.error(error)

    def embrace_tab(self):
        try:
            self.web_element_click_xpath(page_elements.tabs['embrace_tab'])
        except Exception as error:
            ui_logger.error(error)

    def help_tab(self):
        try:
            self.web_element_click_xpath(page_elements.tabs['help_desk_tab'])
        except Exception as error:
            ui_logger.error(error)

    def sub_tab(self, tab_name):
        try:
            self.web_element_click_xpath(page_elements.tabs[tab_name])
        except Exception as error:
            ui_logger.error(error)
