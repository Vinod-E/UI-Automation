import common_login
import page_elements
import time


class Practice(common_login.CommonLogin):
    def __init__(self):
        super(Practice, self).__init__()

    def login(self):
        self.embrace_login()
        self.x_path_element_webdriver_wait(page_elements.tabs['embrace_candidate_tab'])
        self.xpath.click()

        self.web_element_click_xpath(page_elements.embrace['candidates_advance_search'])

        # time.sleep(8)
        # self.x_path_element_webdriver_wait(page_elements.embrace['candidates_advance_search'])
        # self.xpath.click()


Object = Practice()
Object.login()
