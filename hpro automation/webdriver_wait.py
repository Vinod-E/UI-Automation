from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import environment_setup


class WebDriverElementWait(environment_setup.Environment):
    def __init__(self):
        super(WebDriverElementWait, self).__init__()
        self.xpath = ""
        self.id = ""
        self.name = ""

    def x_path_element_webdriver_wait(self, element_path):

        try:
            self.xpath = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, element_path)))

        except exceptions.ElementNotInteractableException as error:
            print error

    def id_element_webdriver_wait(self, element_path):

        try:
            self.id = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.ID, element_path)))

        except exceptions.ElementNotInteractableException as error:
            print error

    def name_element_webdriver_wait(self, element_path):

        try:
            self.name = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.NAME, element_path)))

        except exceptions.ElementNotInteractableException as error:
            print error

