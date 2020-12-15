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


def click_button(self, comma, button_name, commas):
    try:
        webdriver_functions.WebdriverFunctions.\
            web_element_click_xpath(self, page_elements.buttons['click_button'].
                                    format(comma, button_name, commas))
    except Exception as error:
        ui_logger(error)


def more_button(self):
    try:
        webdriver_functions.WebdriverFunctions.\
            web_element_click_xpath(self, page_elements.applicant_actions['more_actions'])
    except Exception as error:
        ui_logger(error)
