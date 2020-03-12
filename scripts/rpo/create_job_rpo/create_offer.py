import config
import page_elements
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import create_job_role
import crpo_login


class CreateOffer(create_job_role.CreateJobRole, crpo_login.CrpoLogin):
    def __init__(self):
        super(CreateOffer, self).__init__()
        self.job_name = []
        self.xl_offer_salary_structure = []
        self.xl_ctc_amount = []
        self.xl_designation = []
        self.xl_benefit = []
        self.xl_bonus = []
        self.xl_date_of_resignation = []
        self.xl_date_of_reliving = []
        self.xl_date_of_joining = []
        self.xl_plan_date_to_join = []
        self.xl_accept_with_date = []
        self.xl_reporting_manager = []
        self.xl_integer1 = []
        self.xl_integer2 = []
        self.xl_text1 = []
        self.xl_text2 = []
        self.xl_text_area1 = []
        self.xl_text_area2 = []
        self.xl_text_area3 = []
        self.job_name_sprint_version = []

        self.requirement_sprint_version = []
        self.job_sprint_version = []

        self.req_name_breadcumb = ""
        self.ui_offer_approved = []
        self.ui_create_offer = []
        self.ui_req_advance_search = []
        self.ui_req_getbyid = []
        self.ui_req_config_tab = []
        self.ui_req_duplicity = []
        self.ui_offer_advance_search = []

        workbook = xlrd.open_workbook(test_data_inputpath.test_data_file['create_offer'])
        if self.login_server == 'beta':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'ams':
            self.req_sheet1 = workbook.sheet_by_index(1)
        if self.login_server == 'amsin':
            self.req_sheet1 = workbook.sheet_by_index(0)

    def login(self):
        self.excel_read()
        self.crpo_login()

    # def job_creation(self):
    #     self.job_excel_read()
    #     self.create_job_role()
    #     # self.job_advance_search()
    #     self.selection_process()
    #     self.feedback_form()
    #     self.tag_interview_panel()
    #     self.ec_configurations_tab()
    #     self.task_configurations_tab()
    #     self.job_automation()

    def offer_excel_read(self):

        # --------------------------------------requirement details-----------------------------------------------------
        for i in range(1, self.req_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.req_sheet1.row_values(number)

            if rows[0]:
                self.job_name.append(rows[0])
            if rows[1]:
                self.xl_offer_salary_structure.append(rows[1])
            if rows[2]:
                self.xl_ctc_amount.append(str(int(rows[2])))
            if rows[3]:
                self.xl_designation.append(rows[3])
            if rows[4]:
                self.xl_benefit.append(str(int(rows[4])))
            if rows[5]:
                self.xl_bonus.append(str(int(rows[5])))
            if rows[6]:
                self.xl_date_of_resignation.append(rows[6])
            if rows[7]:
                self.xl_date_of_reliving.append(rows[7])
            if rows[8]:
                self.xl_date_of_joining.append(rows[8])
            if rows[9]:
                self.xl_plan_date_to_join.append(rows[9])
            if rows[10]:
                self.xl_accept_with_date.append(rows[10])
            if rows[11]:
                self.xl_reporting_manager.append(rows[11])
            if rows[12]:
                self.xl_integer1.append(str(int(rows[12])))
            if rows[13]:
                self.xl_integer2.append(str(int(rows[13])))
            if rows[14]:
                self.xl_text1.append(rows[14])
            if rows[15]:
                self.xl_text2.append(rows[15])
            if rows[16]:
                self.xl_text_area1.append(rows[16])
            if rows[17]:
                self.xl_text_area2.append(rows[17])
            if rows[18]:
                self.xl_text_area3.append(rows[18])

            for k in self.job_name:
                job_name = k
                self.job_name_sprint_version = job_name.format(self.sprint_version)
            # for j in self.requirement_name:
            #     requirement_name = j
            #     self.requirement_sprint_version = requirement_name.format(self.sprint_version)

    def offer_creation(self):
        time.sleep(5)
        try:
            print("offer module starting")
            time.sleep(4)
            # self.driver.get()
            self.driver.get(config.configs[self.login_server])
            print("Url is hitting")
            time.sleep(10)
            # poststatus = self.driver.window_handles[1]
            # self.driver.switch_to.window(poststatus)

            user = self.driver.find_element_by_name('loginName')
            user.send_keys("admin")

            pwd = self.driver.find_element_by_xpath(
                '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div[2]/form/div[2]/input')
            pwd.send_keys('rpo@1234')
            self.driver.find_element_by_xpath(page_elements.login['login_button']).click()
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.offer['offer_tab']).click()
            time.sleep(15)
            self.driver.save_screenshot(config.configs['screen_shot'].format('Offer Module Entered'))
            self.driver.find_element_by_xpath(page_elements.offer['offer_advance_search']).click()

            time.sleep(4)
            self.driver.find_element_by_xpath(page_elements.offer['offer_job_search']).click()
            time.sleep(3)
            # self.driver.execute_script("window.scrollTo(0,200);")
            search = self.driver.find_element_by_xpath(page_elements.offer['search'])
            search.send_keys(self.job_name_sprint_version)
            time.sleep(4)
            self.driver.find_element_by_xpath(page_elements.offer['moveAlltoRight']).click()
            time.sleep(3)
            self.driver.find_element_by_link_text('Done').click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 300)")
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath(page_elements.offer['search_button']).click()
                time.sleep(10)
            except exceptions.NoSuchElementException as search:
                print(search)
            print('------------------------offer Advance Search Suceesfully------------------')
            self.ui_offer_advance_search = 'Pass'
            self.driver.find_element_by_xpath(page_elements.offer['view_edit_offer']).click()
            time.sleep(5)
            newtab = self.driver.window_handles[1]
            self.driver.switch_to_window(newtab)
            time.sleep(5)
            sal_Structure = self.driver.find_element_by_xpath(page_elements.offer['salary_structure'])
            sal_Structure.send_keys(self.xl_offer_salary_structure)
            sal_Structure.send_keys(Keys.ARROW_DOWN)
            sal_Structure.send_keys(Keys.ENTER)
            time.sleep(2)

            ctc_amount_rupees = self.driver.find_element_by_xpath(page_elements.offer['offered_ctc'])
            ctc_amount_rupees.send_keys(self.xl_ctc_amount)
            time.sleep(3)

            split_ctc = self.driver.find_element_by_xpath(page_elements.offer['split_ctc'])
            split_ctc.click()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 400)")

            designation = self.driver.find_element_by_xpath(page_elements.offer['offer_designation'])
            designation.send_keys(self.xl_designation)
            designation.send_keys(Keys.ARROW_DOWN)
            designation.send_keys(Keys.ENTER)
            time.sleep(2)

            benifit = self.driver.find_element_by_xpath(page_elements.offer['offer_benifit'])
            benifit.send_keys(self.xl_benefit)
            time.sleep(1)

            bonus = self.driver.find_element_by_xpath(page_elements.offer['offer_bonus'])
            bonus.send_keys(self.xl_bonus)
            time.sleep(1)

            stock = self.driver.find_element_by_xpath(page_elements.offer['offer_stock'])
            stock.send_keys("IAMSTOCK")
            time.sleep(1)

            reaonofabort = self.driver.find_element_by_xpath(page_elements.offer['reason_abort'])
            reaonofabort.send_keys("NOREGION")
            time.sleep(2)

            resignation = self.driver.find_element_by_xpath(page_elements.offer['date_of_resignation'])
            resignation.send_keys("17/02/2020")
            time.sleep(2)

            reliving = self.driver.find_element_by_xpath(page_elements.offer['date_of_reliiving'])
            reliving.send_keys("18/02/2020")
            time.sleep(4)

            joining_date = self.driver.find_element_by_xpath(page_elements.offer['joining_date'])
            joining_date.send_keys("19/02/2020")
            time.sleep(3)

            plan_date = self.driver.find_element_by_xpath(page_elements.offer['plan_date_joining'])
            plan_date.send_keys("21/02/2020")
            time.sleep(3)

            accept_date = self.driver.find_element_by_xpath(page_elements.offer['accept_within_days'])
            accept_date.send_keys("5")
            time.sleep(1)

            reporting = self.driver.find_element_by_xpath(page_elements.offer['reporting_mangaer'])
            reporting.send_keys(self.xl_reporting_manager)
            reporting.send_keys(Keys.ARROW_DOWN)
            reporting.send_keys(Keys.ENTER)
            time.sleep(2)

            cus_integer1 = self.driver.find_element_by_xpath(page_elements.offer['cus_int1'])
            cus_integer1.send_keys(self.xl_integer1)
            cus_integer1.send_keys(Keys.ARROW_DOWN)
            cus_integer1.send_keys(Keys.ENTER)
            time.sleep(1)

            cus_integer2 = self.driver.find_element_by_xpath(page_elements.offer['cus_int2'])
            cus_integer2.send_keys(self.xl_integer2)
            cus_integer2.send_keys(Keys.ARROW_DOWN)
            cus_integer2.send_keys(Keys.ENTER)
            time.sleep(1)

            text_1 = self.driver.find_element_by_xpath(page_elements.offer['text_cus1'])
            text_1.send_keys(self.xl_text1)
            time.sleep(1)

            text_2 = self.driver.find_element_by_xpath(page_elements.offer['text_cus2'])
            text_2.send_keys(self.xl_text1)
            time.sleep(1)

            datecus_1 = self.driver.find_element_by_xpath(page_elements.offer['date_cus_1'])
            datecus_1.send_keys("20/04/1995")
            time.sleep(1)

            datecus_2 = self.driver.find_element_by_xpath(page_elements.offer['date_cus_2'])
            datecus_2.send_keys("20/04/1996")
            time.sleep(1)

            textarea_1 = self.driver.find_element_by_xpath(page_elements.offer['text_area_1'])
            textarea_1.send_keys(self.xl_text_area1)
            time.sleep(1)

            textarea_2 = self.driver.find_element_by_xpath(page_elements.offer['text_area_2'])
            textarea_2.send_keys(self.xl_text_area2)
            time.sleep(1)

            textarea_3 = self.driver.find_element_by_xpath(page_elements.offer['text_area_3'])
            textarea_3.send_keys(self.xl_text_area3)
            time.sleep(1)

            creatOffer = self.driver.find_element_by_xpath(page_elements.offer['create_offer'])
            creatOffer.click()
            time.sleep(2)
            popUpOk = self.driver.find_element_by_xpath(page_elements.offer['offerPopup'])
            popUpOk.click()
            self.ui_create_offer = 'Pass'
            print('--------------------------- Offer Created successfully -------------------------------------')
            time.sleep(5)

            CommentBox = self.driver.find_element_by_xpath(page_elements.offer['approverCommment'])
            CommentBox.send_keys("Offer Approved")
            time.sleep(2)
            AppBtn = self.driver.find_element_by_xpath(page_elements.offer['ApproveButton'])
            AppBtn.click()
            time.sleep(2)

            print('--------------------------- Offer approved successfully -------------------------------------')
            self.ui_offer_approved = 'Pass'
        except exceptions.NoSuchElementException as config_message:
            print(config_message)

#
# Object = CreateOffer()
# Object.login()
# if Object.status_of_login == 'admin':
#     Object.offer_excel_read()
#     Object.offer_creation()
#
#


#     Object.req_configuration_tab()
#     Object.req_advance_search()
#     Object.browser_close()
# else:
#     Object.server_connection_error()
#     Object.browser_close()
