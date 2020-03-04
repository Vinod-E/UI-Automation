import time
import page_elements
import common_login
from logger_settings import api_logger


class AdvanceSearch(common_login.CommonLogin):
    def __init__(self):
        super(AdvanceSearch, self).__init__()

        self.search = []
        self.job_search = ''

    def advance_search(self, tab):
        try:

            self.x_path_element_webdriver_wait(tab)
            self.xpath.click()
            self.driver.execute_script("window.scrollTo(0,-100);")
            time.sleep(2.5)

            self.id_element_webdriver_wait(page_elements.advance_search['search'])
            self.id.click()

        except Exception as search:
            api_logger.error(search)

    def applicant_advance_search(self):
        try:

            self.driver.execute_script("window.scrollTo(0,-50);")
            time.sleep(2)

            self.id_element_webdriver_wait(page_elements.advance_search['search'])
            self.id.click()

        except Exception as search:
            api_logger.error(search)

    def name_search(self, name, where_search_is_happening):
        try:

            self.name_element_webdriver_wait(page_elements.advance_search['name'])
            time.sleep(1)
            self.name.send_keys(name)

            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.buttons['search'])
            self.xpath.click()
            print('**-------->>> {} advance search is working'.format(where_search_is_happening))
            self.search = 'Pass'

        except Exception as search:
            api_logger.error(search)

    def assessment_name_search(self, name, where_search_is_happening):
        try:

            self.name_element_webdriver_wait(page_elements.advance_search['assessment_name'])
            time.sleep(2)
            self.name.send_keys(name)

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.buttons['search'])
            self.xpath.click()
            print('**-------->>> {} advance search is working'.format(where_search_is_happening))
            self.search = 'Pass'

        except Exception as search:
            api_logger.error(search)

    def applicant_name_search(self, name, where_search_is_happening):
        try:

            self.name_element_webdriver_wait(page_elements.advance_search['a_name'])
            time.sleep(2)
            self.name.clear()
            self.name.send_keys(name)

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.buttons['search'])
            self.xpath.click()
            print('**-------->>> {} advance search is working'.format(where_search_is_happening))
            self.search = 'Pass'

        except Exception as search:
            api_logger.error(search)

    def job_applicant_name_search(self, job_name):

        self.web_element_send_keys_name(page_elements.advance_search['job_applicant_name'], job_name)
        time.sleep(1.5)
        self.web_element_click_xpath(page_elements.buttons['search'])
        print('**-------->>> {} advance search is working'.format(job_name))
        self.job_search = 'True'
