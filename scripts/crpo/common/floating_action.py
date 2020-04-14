import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import advance_search


class FloatingAction(advance_search.AdvanceSearch):
    def __init__(self):
        super(FloatingAction, self).__init__()

    def floating_action(self):
        try:
            # ------------------------------------ Selection Process -----------------------------------------------
            self.web_element_click_xpath(page_elements.floating_actions['floating_actions'])

        except Exception as error:
            ui_logger.error(error)
