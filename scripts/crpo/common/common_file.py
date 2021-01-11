from scripts.crpo.common import validations_check
from selenium.common.exceptions import NoSuchElementException


class CommonFile(validations_check.ValidationCheck):
    def __init__(self):
        super(CommonFile, self).__init__()

    def check_exists_element(self, by_locator, element):
        try:
            self.driver.find_element(by_locator, element)
        except NoSuchElementException:
            return False
        return True
