import page_elements
import webdriver_functions
from logger_settings import ui_logger


def button(self, button_name):
    try:
        webdriver_functions.WebdriverFunctions.\
            web_element_click_xpath(self, page_elements.buttons['common_button'].format(button_name))
    except Exception as error:
        ui_logger(error)


def all_buttons(self, button_name):
    try:
        webdriver_functions.WebdriverFunctions.\
            web_element_click_xpath(self, page_elements.buttons['all_buttons'].format(button_name))
    except Exception as error:
        ui_logger(error)
