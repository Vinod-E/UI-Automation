import webdriver_wait
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys


class WebdriverFunctions(webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(WebdriverFunctions, self).__init__()
        self.text_value = ''

    def web_element_text_xpath(self, web_element):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.text_value = self.xpath.text
        except Exception as error:
            api_logger.error(error)

    def web_element_text_id(self, web_element):
        try:
            self.id_element_webdriver_wait(web_element)
            self.text_value = self.id.text
        except Exception as error:
            api_logger.error(error)

    def web_element_text_name(self, web_element):
        try:
            self.name_element_webdriver_wait(web_element)
            self.text_value = self.name.text
        except Exception as error:
            api_logger.error(error)

    def web_element_click_xpath(self, web_element):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def web_element_click_id(self, web_element):
        try:
            self.id_element_webdriver_wait(web_element)
            self.id.click()
        except Exception as error:
            api_logger.error(error)

    def web_element_click_name(self, web_element):
        try:
            self.name_element_webdriver_wait(web_element)
            self.name.click()
        except Exception as error:
            api_logger.error(error)

    def web_element_send_keys_xpath(self, web_element, key):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.xpath.send_keys(key)
        except Exception as error:
            api_logger.error(error)

    def web_element_send_keys_id(self, web_element, key):
        try:
            self.id_element_webdriver_wait(web_element)
            self.id.send_keys(key)
        except Exception as error:
            api_logger.error(error)

    def web_element_send_keys_name(self, web_element, key):
        try:
            self.name_element_webdriver_wait(web_element)
            self.name.send_keys(key)
        except Exception as error:
            api_logger.error(error)

    def drop_down_selection(self):
        self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
