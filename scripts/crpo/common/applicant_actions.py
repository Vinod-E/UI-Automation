import page_elements
import webdriver_functions
from logger_settings import ui_logger


def action(self, action_name):
    try:
        webdriver_functions.WebdriverFunctions.\
            web_element_click_xpath(self, page_elements.applicant_actions['actions'].format(action_name))
    except Exception as error:
        ui_logger(error)
