import crpo_login
import config
import page_elements
import webdriver_wait
import time

class example(crpo_login.CrpoLogin, webdriver_wait.WebDriverElementWait):

    def __init__(self):
        super(example, self).__init__()
        self.xl_amsin_tenant = []
        self.xl_amsin_username = []
        self.xl_amsin_password = []

    def login(self):
        self.excel_read()
        self.crpo_login()

    def abc(self):
        # --------------------------- New tab to login as interviewer ----------------------------------------------
        self.driver.execute_script("window.open('about:blank', 'tab1');")
        self.driver.switch_to.window("tab1")
        self.driver.get(config.configs[self.login_server])
        print "-------------------- New tab open with URL ------------------------"

        # --------------------------- Login as an interviewer ------------------------------------------------------
        self.name_element_webdriver_wait(page_elements.login['username'])
        self.name.send_keys('newint1')

        self.x_path_element_webdriver_wait(page_elements.login['password'])
        self.xpath.send_keys('newint1')

        self.x_path_element_webdriver_wait(page_elements.login['login_button'])
        self.xpath.click()
        print "-------------------- Interviewer1 Login successfully ------------------------"

    def cde(self):
        # self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
        time.sleep(10)
        # text = self.driver.find_element_by_xpath('//*[@id="mainBodyElement"]/div[3'
        #                                          ']/section/div/div/div[1]/div[2]/div/select').text
        # print text

        label = self.driver.find_element_by_xpath('//*[@label="Partial Submissions"]')
        label.click()
        # if text == 'Partial Submissions':
        #     self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
        #     self.xpath.click()
        #
        # Mapping_value_Dropdown = self.driver.find_elements_by_xpath(page_elements.feedback['Interview_bucket'])
        # for x in range(0, len(Mapping_value_Dropdown)):
        #
        #     if Mapping_value_Dropdown[x].is_displayed():
        #         time.sleep(2)
        #         Mapping_value_Dropdown[x].click()
        #
        #     for x in range(0, 1):
        #         select_College = self.driver.find_element_by_xpath(".//*[@ng-click='vm.onSelect(item)']")
        #         select_College.click()


o = example()
o.login()
o.abc()
o.cde()
