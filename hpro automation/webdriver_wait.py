from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import environment_setup


class WebDriverElementWait(environment_setup.Environment):
    def __init__(self):
        super(WebDriverElementWait, self).__init__()

    def element_webdriver_wait(self, element_path):
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located((By.XPATH, element_path)))
