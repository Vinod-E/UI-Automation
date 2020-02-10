import page_elements
from logger_settings import api_logger
from scripts.crpo.common import getby_details


class CheckBox(getby_details.GetByDetails):
    def __init__(self):
        super(CheckBox, self).__init__()

    def check_box(self):
        try:
            self.name_element_webdriver_wait(page_elements.grid['check_box'])
            self.name.click()
        except Exception as image_error:
            api_logger.error(image_error)
