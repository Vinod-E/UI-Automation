import webdriver_wait
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys


class WebdriverFunctions(webdriver_wait.WebDriverElementWait):
    def __init__(self):
        super(WebdriverFunctions, self).__init__()
        self.text_value = ''
        self.xpath_send_keys = ''

    def web_element_text_xpath(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                xpath_text = self.driver.find_element_by_xpath(web_element)
                self.text_value = xpath_text.text

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_text_id(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                id_text = self.driver.find_element_by_id(web_element)
                self.text_value = id_text.text

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_text_name(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                name_text = self.driver.find_element_by_name(web_element)
                self.text_value = name_text.text

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_click_xpath(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                xpath_click = self.driver.find_element_by_xpath(web_element)
                xpath_click.click()

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_click_id(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                id_click = self.driver.find_element_by_id(web_element)
                id_click.click()

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_click_name(self, web_element):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                name_click = self.name_element_webdriver_wait(web_element)
                name_click.click()

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_send_keys_xpath(self, web_element, key):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                self.xpath_send_keys = self.driver.find_element_by_xpath(web_element)
                self.xpath_send_keys.send_keys(key)

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_send_keys_id(self, web_element, key):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                id_send_keys = self.driver.find_element_by_id(web_element)
                id_send_keys.send_keys(key)

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def web_element_send_keys_name(self, web_element, key):
        result = False
        attempts = 0
        while attempts < 10:
            try:
                name_send_keys = self.driver.find_element_by_name(web_element)
                name_send_keys.send_keys(key)

                result = True
                break
            except Exception as error:
                api_logger.error(error)
            attempts += 1
        # print('Number of attempts = {}'.format(attempts))
        return result

    def drop_down_selection(self):
        self.xpath_send_keys.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
