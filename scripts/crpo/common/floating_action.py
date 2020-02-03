import page_elements
from logger_settings import api_logger
from scripts.crpo.common import advance_search


class FloatingAction(advance_search.AdvanceSearch):
    def __init__(self):
        super(FloatingAction, self).__init__()

    def floating_action(self):
        try:
            # ------------------------------------ Selection Process -----------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.floating_actions['floating_actions'])
            self.xpath.click()

        except Exception as error:
            api_logger.error(error)
