import webdriver_wait
from logger_settings import api_logger


class WebdriverFunctions(webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(WebdriverFunctions, self).__init__()
        self.text_value = ''

    def web_element_text(self, web_element):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.text_value = self.xpath.text
        except Exception as error:
            api_logger.error(error)

    def web_element_click(self, web_element):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def web_element_send_keys(self, web_element, key):
        try:
            self.x_path_element_webdriver_wait(web_element)
            self.xpath.send_keys(key)
        except Exception as error:
            api_logger.error(error)
