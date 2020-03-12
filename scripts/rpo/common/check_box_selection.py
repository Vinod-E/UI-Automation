import page_elements
from logger_settings import api_logger
from scripts.crpo.common import getby_details


class CheckBox(getby_details.GetByDetails):
    def __init__(self):
        super(CheckBox, self).__init__()

    def check_box(self):
        try:
            self.web_element_click_name(page_elements.grid['check_box'])
        except Exception as error:
            api_logger.error(error)

    def all_check_box_unlock(self):
        try:
            self.web_element_click_xpath(page_elements.grid['all'])
        except Exception as error:
            api_logger.error(error)
