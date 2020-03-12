import time
import xlrd
import image_capture
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from scripts.crpo.common import menu_tabs
from logger_settings import api_logger
from scripts.rpo.common import login
import config
from scripts.crpo.common import getby_details
import page_elements
import test_data_inputpath


class CreateJobRole(login.Login, getby_details.GetByDetails ):
    def __init__(self):
        super(CreateJobRole, self).__init__()
        # --------- Rpo Login-------------
        self.rpo_login()

        self.job_name = []
        self.file = []
        self.j_description = []
        self.j_location = []
        self.j_hm = []
        self.j_recuirter = []
        self.j_bu = []
        self.j_sbu = []
        self.j_code = []
        self.openings = []
        self.j_sp = []
        self.j_type = []
        self.j_onecustome = []
        self.j_description_u = []
        # self.xl_selection_process = []
        self.xl_interview_stage_01 = []
        self.xl_interview_template_01 = []
        self.xl_tag_interviewers = []
        self.xl_posting_start_date = []
        self.xl_posting_end_date = []
        self.job_posting_type = []

        self.xl_posting_referal = []
        self.candi_resume = []
        self.candi_image = []
        self.candi_other_attach = []
        self.ui_job_posting_to_vendor = []
        self.ui_job_posting_to_referal = []
        self.job_name_sprint_version = []
        # self.job_name_grid_view = []
        self.job_name_breadcumb = ""
        self.tag_interviewers = ""
        self.selection_process_created = []
        self.ui_job_approved = []
        self.ui_job_created = []
        self.ui_job_advance_search = []
        self.ui_interview_feedback = []
        self.ui_interview_login = []
        self.ui_vendor_login = []
        self.ui_vendor_advance_search = []
        self.ui_vendor_extract_resume = []
        self.ui_source_candidate = []
        self.ui_interview_advance_search = []
        self.ui_interview_stage1 = []
        self.ui_status_change = []
        self.ui_tag_interviews = []
        self.ui_create_candidate = []
        self.ui_extract_resume = []
        self.ui_update_job = []
        self.ui_create_offer = []
        self.ui_status_change_to_offer_pending = []

        workbook = xlrd.open_workbook(test_data_inputpath.rpo_test_data_file['create_job'])
        if self.login_server == 'beta':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.job_sheet1 = workbook.sheet_by_index(1)

    def job_excel_read(self):

        # --------------------------------------job details-----------------------------------------------------------
        for i in range(1, self.job_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.job_sheet1.row_values(number)

            if rows[0]:
                self.job_name.append(rows[0])
            if rows[1]:
                self.file.append(rows[1])
            if rows[2]:
                self.j_description.append(rows[2])
            if rows[3]:
                self.j_location.append(rows[3])
            if rows[4]:
                self.j_hm.append(rows[4])
            if rows[5]:
                self.j_recuirter.append(rows[5])
            if rows[6]:
                self.j_bu.append(rows[6])
            if rows[7]:
                self.j_sbu.append(rows[7])
            if rows[8]:
                self.j_code.append(rows[8])
            if rows[9]:
                self.openings.append(str(int(rows[9])))
            if rows[10]:
                self.j_sp.append(rows[10])
            if rows[11]:
                self.j_type.append(rows[11])
            if rows[12]:
                self.j_onecustome.append(rows[12])
            if rows[13]:
                self.j_description_u.append(rows[13])
            if rows[14]:
                self.xl_tag_interviewers.append(rows[14])
            if rows[15]:
                self.xl_interview_stage_01.append(rows[15])
            if rows[16]:
                self.xl_interview_template_01.append(rows[16])
            if rows[17]:
                self.xl_posting_start_date.append((rows[17]))
            if rows[18]:
                self.xl_posting_end_date.append(rows[18])
            if rows[19]:
                self.job_posting_type.append(rows[19])
            if rows[20]:
                self.xl_posting_referal.append(rows[20])
            if rows[21]:
                self.candi_resume.append(rows[21])
            if rows[22]:
                self.candi_image.append(rows[22])
            if rows[23]:
                self.candi_other_attach.append(rows[23])
            # if rows[12]:
            #     self.xl_interview_stage_02.append(rows[12])
            # if rows[13]:
            #     self.xl_interview_template_02.append(rows[13])

            for j in self.job_name:
                job_name = j
                self.job_name_sprint_version = job_name.format(self.sprint_version)

            for k in self.xl_tag_interviewers:
                interviewers = k
                self.tag_interviewers = interviewers

    def create_job_role(self):

        try:
            self.job_tab()
            self.web_element_click_xpath(page_elements.buttons['create'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Job Name'),
                                             self.job_name_sprint_version)

            self.web_element_send_keys_xpath(page_elements.file['upload_file'], self.file)

            self.web_element_send_keys_xpath(page_elements.job['description_box'], self.j_description)
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.job['location'], self.j_location)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Type'), self.j_type)
            self.drop_down_selection()

            self.clear(page_elements.text_fields['number_field'].format('Number of Openings'))
            self.web_element_send_keys_xpath(page_elements.text_fields['number_field'].format('Number of Openings'),
                                             self.openings)

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Selection Process'),
                                             self.j_sp)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Hiring Manager'),
                                             self.j_hm)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Recruiter'),
                                             self.j_recuirter)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Unit'),
                                             self.j_bu)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Department'),
                                             self.j_sbu)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.job['description_box'], self.j_description)
            time.sleep(0.5)

            self.web_element_click_xpath(page_elements.title['title'].format('Admin'))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             'admin')
            self.web_element_click_xpath(page_elements.job['Official_Use_move'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('JobCode'),
                                             self.j_code)
            self.drop_down_selection()
            okay_button = self.driver.find_element_by_xpath("//div[6]/div/div/div[3]/div/div[1]")
            okay_button.click()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('I1'),
                                             self.j_onecustome)
            self.drop_down_selection()

            self.driver.find_element_by_xpath(page_elements.buttons['create-save']).click()
            image_capture.screen_shot(self, 'job')
            print('--------------------------- Job Created successfully -------------------------------------')

            # Approve job bySelf
            self.driver.find_element_by_xpath(page_elements.buttons['self_approve']).click()
            self.driver.find_element_by_xpath(page_elements.buttons['self_approve_ok']).click()

            print('----------------------------Job approved successfully -------------------------------------')
            image_capture.screen_shot(self, 'job')

        except exceptions.NoSuchElementException as create_job:
            print(create_job)
        try:
            time.sleep(5)
            job_name_from_breadcrumb = self.driver.find_element_by_xpath(page_elements.job_validations['job_name_breadcumb'])
            self.job_name_breadcumb = job_name_from_breadcrumb.text
        except exceptions.NoSuchElementException as e1:
            print(e1)

        time.sleep(3)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            # print('Job Created successfully')
            self.ui_job_created = 'Pass'

            # elif self.job_name_sprint_version == self.job_name_grid_view:
            print('-----------------Job Creation and Approvel Has Been Done Successfully-----------------')
        else:
            print('-------------------------Job Creation Failed------------------------------------------')

    def edit_job(self):
        self.job_validation('edit action')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.floating_action()
                self.web_element_click_xpath(page_elements.floating_actions['job_edit'])
                desc = self.driver.find_element_by_xpath(page_elements.job['job_description'])
                desc.send_keys(self.j_description_u)

                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['job_create_button']).click()
                print('-------------------------- Job Edit/update successfully -----------------')
                self.ui_update_job = 'Pass'
                self.driver.back()
                self.driver.refresh()
                self.driver.back()

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def tag_candidate(self):
        # self.driver.implicitly_wait(3)
        time.sleep(10)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()

                time.sleep(2)
                addCandidate = self.driver.find_element_by_xpath(page_elements.job['add_candidate'])
                addCandidate.click()
                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.job['upload_resume']).send_keys(self.candi_resume)
                time.sleep(15)
                self.driver.find_element_by_xpath(page_elements.job['extract_resume']).click()
                time.sleep(10)
                self.driver.find_element_by_xpath(page_elements.job['extract_details']).click()
                self.ui_extract_resume = 'Pass'
                print('------------------------ Resume Extraction Sucessfully ------------------------')
                # self.driver.find_element_by_xpath(page_elements.job['upload_attachment']).send_keys(self.candi_other_attach)
                time.sleep(20)
                # self.driver.find_element_by_xpath(page_elements.job['upload_photho']).send_keys(self.candi_image)
                create_candidate = self.driver.find_element_by_xpath(page_elements.job['create_candidate'])
                create_candidate.click()
                time.sleep(3)
                print('------------------------ Candidate Created successfully ------------------------')
                print('------------------------ Candidate Tag to Job successfully ------------------------')
                self.ui_create_candidate = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)

    #  Job Posting Rpo
    def job_posting(self):
        time.sleep(5)
        # self.driver.implicitly_wait(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(5)

                self.driver.find_element_by_link_text("Postings").click()
                # self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                # time.sleep(5)
                # job_post = self.driver.find_element_by_xpath(page_elements.job['job_posting_tab'])
                # job_post.click()

                time.sleep(4)
                postingFrom = self.driver.find_element_by_xpath(page_elements.job['job_posting_from'])
                postingFrom.send_keys(self.xl_posting_start_date)
                postingFrom.send_keys(Keys.ENTER)

                postingTo = self.driver.find_element_by_xpath(page_elements.job['job_posting_to'])
                postingTo.send_keys(self.xl_posting_end_date)
                postingTo.send_keys(Keys.ENTER)
                print("---------------------------")
                time.sleep(5)
                # posting job to Referal
                # postingType = self.driver.find_element_by_xpath(page_elements.job['posting_typ'])
                # postingType.send_keys(self.job_posting_type)
                # postingType.send_keys(Keys.ENTER)

                # posting job to Vendor
                postingType = self.driver.find_element_by_xpath(page_elements.job['posting_typ'])
                postingType.send_keys(self.job_posting_type)
                postingType.send_keys(Keys.ENTER)
                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.job['posting_vendor_select']).click()
                self.driver.find_element_by_xpath(page_elements.job['selvendor']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['moveToRight']).click()
                time.sleep(1)
                click_done = self.driver.find_element_by_xpath(page_elements.job['vendor_done'])
                click_done.click()

                self.driver.find_element_by_xpath(page_elements.job['post_add_click']).click()
                print(" Job Posted to Vendor Successfully")

                time.sleep(5)
                self.driver.refresh()
                time.sleep(5)
                postingFrom = self.driver.find_element_by_xpath(page_elements.job['job_posting_from'])
                postingFrom.send_keys(self.xl_posting_start_date)
                postingFrom.send_keys(Keys.ENTER)

                postingTo = self.driver.find_element_by_xpath(page_elements.job['job_posting_to'])
                postingTo.send_keys(self.xl_posting_end_date)
                postingTo.send_keys(Keys.ENTER)
                self.ui_job_posting_to_vendor = 'Pass'
                time.sleep(10)

                # posting job to Referal
                postingType = self.driver.find_element_by_xpath(page_elements.job['posting_typ'])
                postingType.send_keys(self.xl_posting_referal)
                postingType.send_keys(Keys.ENTER)
                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.job['post_add_click']).click()
                print("Job Posted to Referal Successfully")

                print('------------------------ job Posting Has Been Done------------------------')
                self.ui_job_posting_to_referal = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def job_advance_search(self):
        try:
            self.advance_search(page_elements.tabs['job_tab'])
            self.name_search(self.job_name_sprint_version, 'Job')
            self.job_getby_details(self.job_name_sprint_version)

            time.sleep(3)
            print('---------------------Advance search is working fine ------------------')
            self.ui_job_advance_search = 'Pass'

        except exceptions.WebDriverException as search:
            print(search)

    # Applicant Post Status Change
    def post_status_change(self):
        time.sleep(5)
        try:
            self.login('admin', self.xl_username, self.xl_rpo_password)
            self.driver.find_element_by_xpath(page_elements.job['job_tab']).click()
            time.sleep(3)
            self.job_advance_search()
            self.driver.close()
            time.sleep(4)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(3)
            try:
                time.sleep(5)
                job_name_from_breadcrumb = self.driver.find_element_by_xpath(page_elements.job['jobrole_breadcrumbs'])
                self.job_name_breadcumb = job_name_from_breadcrumb.text
                print(self.job_name_breadcumb)
                print(self.job_name_sprint_version)
            except exceptions.NoSuchElementException as e1:
                print(e1)
            if str(self.job_name_breadcumb) == str(self.job_name_sprint_version):
                try:
                    self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                    time.sleep(3)
                    viewApplicant = self.driver.find_element_by_xpath(page_elements.job['view_applicant'])
                    viewApplicant.click()
                    time.sleep(2)
                    self.driver.close()
                    poststatus = self.driver.window_handles[0]
                    self.driver.switch_to.window(poststatus)

                    self.driver.find_element_by_xpath(page_elements.job['against_candidate_action']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['change_app_action']).click()
                    time.sleep(6)
                    self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['second_interview']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(3)
                    self.driver.find_element_by_link_text('Pending').click()
                    time.sleep(4)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(3)
                    self.driver.find_element_by_link_text('Scheduled').click()
                    time.sleep(5)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(4)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(2)
                    self.driver.find_element_by_link_text('Shortlisted').click()
                    print("Second Interview Shortlisted ")
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(10)
                    print('----------------------second has been done--------------------')
                    self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['final_int']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(2)
                    # final pending Scheduled
                    self.driver.find_element_by_xpath(page_elements.job['second_pending']).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(4)
                    self.driver.find_element_by_link_text('Scheduled').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)

                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(4)
                    self.driver.find_element_by_link_text('Shortlisted').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)
                    print("Final Interview Shortlisted")
                    # final has been done

                    self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath(page_elements.job['hr_int']).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(2)
                    self.driver.find_element_by_link_text('Pending').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)

                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['sec_schedule']).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(4)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(5)
                    self.driver.find_element_by_link_text('Shortlisted').click()
                    print("HR Interview Shortlisted ")
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)
                    #  offer pending
                    self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
                    time.sleep(3)
                    self.driver.find_element_by_link_text('Offer').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
                    time.sleep(2)

                    self.driver.find_element_by_link_text('OfferPending').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
                    time.sleep(5)
                    print("Status change to Offer Pending")
                    self.ui_status_change_to_offer_pending = 'Pass'
                    # self.driver.close()

                    # poststatus = self.driver.window_handles[2]
                    # self.driver.switch_to.window(poststatus)

                except  exceptions.WebDriverException as poststatusss:
                    print(poststatusss)
        except exceptions.WebDriverException as post:
            print(post)

    def feedback_form(self):
        time.sleep(5)
        window_after1 = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after1)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                # -------------------------- Interview stage / feedback form configuration -----------------------------
                time.sleep(5)
                # self.driver.refresh()
                # self.driver.implicitly_wait(5)
                # time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_feedback_form']).click()
                time.sleep(3)
                stage_01 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_configure'])
                stage_01.click()
                time.sleep(3)
                stage_01.send_keys(self.xl_interview_stage_01)
                stage_01.send_keys(Keys.ARROW_DOWN)
                stage_01.send_keys(Keys.ENTER)
                time.sleep(3)
                feedback_01 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_name_search'])
                feedback_01.send_keys(self.xl_interview_template_01)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_search_button']).click()
                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_use']).click()
                time.sleep(3)
                int_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_save_button'])
                int_save.send_keys(Keys.DOWN)
                int_save.click()
                time.sleep(5)
                print('-------------------interview feedback form configured successfully---------------------')
                self.ui_interview_stage1 = 'Pass'
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            except exceptions.WebDriverException as config_message:
                print(config_message)

    def sourcedCandidate(self):
        try:
            time.sleep(5)

            self.login('vendor', 'automationV', 'admin@1234')
            try:
                self.x_path_element_webdriver_wait(page_elements.login['login_success'])
                self.status_of_login = self.xpath.text
                assert self.status_of_login.strip() == 'automationVendor'
                print("**---------------------- In main screen ------------------------**")
            except Exception as login_status:
                api_logger.error(login_status)

            time.sleep(4)
            self.advance_search(page_elements.tabs['vendor_job'])
            self.vendor_job_name_search(self.job_name_sprint_version, 'vendor_job')
            time.sleep(4)
            referCandidate = self.driver.find_element_by_xpath("//*[@ng-if='!action.isPopOver']")
            referCandidate.click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['upload_resume']).send_keys(self.candi_resume)
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.job['extract_resume']).click()
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.job['extract_details']).click()
            time.sleep(3)
            self.ui_vendor_extract_resume = 'Pass'
            self.driver.find_element_by_xpath(page_elements.job_vendor['custom7']).send_keys(
                self.job_name_sprint_version)
            self.driver.find_element_by_xpath(page_elements.job_vendor['custom6']).send_keys("Mai Hu Vendor")
            create_candidate = self.driver.find_element_by_xpath(page_elements.job['create_candidate'])
            create_candidate.click()
            time.sleep(3)

            print('------------------------ Candidate Sourced successfully ------------------------')
            self.ui_source_candidate = 'Pass'

        except exceptions.ElementNotInteractableException as error:
            print(error)

    def tag_interview_panel(self):
        time.sleep(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                # --------------------------------------- Tag Interviewers----------------------------------------------
                self.driver.refresh()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()

                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_tag_interviewers']).click()

                time.sleep(6)
                # self.driver.find_element_by_xpath(page_elements.job['getbyid_tag_interviewers']).click()
                self.driver.find_element_by_xpath(page_elements.job['interview_panel'].format(
                    self.tag_interviewers)).click()

                time.sleep(5)
                add = self.driver.find_element_by_xpath(page_elements.job['add_interviewers_to_table'])
                add.click()
                time.sleep(6)
                self.driver.find_element_by_xpath(page_elements.job['save_interviewers_to_panel']).click()
                print('-------------------Interviewers are added to job role-------------------------')
                self.ui_tag_interviews = 'Pass'
                time.sleep(5)

            except exceptions.WebDriverException as config_message:
                print('Tag interviewers :: ', config_message)
                self.driver.refresh()

    # Applicant Pre Status Change
    def status_change(self):
        try:
            time.sleep(5)
            # self.driver.implicitly_wait(5)
            self.driver.refresh()

            time.sleep(15)
            self.driver.find_element_by_xpath(page_elements.job['change_applicant_status']).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['click_status']).click()
            time.sleep(3)
            cv_screened = self.driver.find_element_by_xpath(page_elements.job['cv_screened']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
            print("Status change to Cv_screened")
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['tech_screen']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['status_click']).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['tech_pending']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['status_click']).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(page_elements.job['tech_short']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
            print("Status change to Tech Shortlisted")
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['stage_click']).click()
            time.sleep(3)
            self.driver.find_element_by_link_text('First Interview').click()
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['status_click']).click()
            time.sleep(3)
            self.driver.find_element_by_link_text('Pending').click()
            time.sleep(4)
            self.driver.find_element_by_xpath(page_elements.job['change_button']).click()
            print("Status change to First interview pending Sucessfully")
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['status_click']).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['first_schedule']).click()
            time.sleep(4)
            datetimeInterview = self.driver.find_element_by_xpath(page_elements.job['date_time'])
            datetimeInterview.send_keys("21/01/2020")
            time.sleep(3)
            self.driver.find_element_by_xpath(page_elements.job['interview_button']).click()
            time.sleep(3)
            print("Add interview")
            self.driver.find_element_by_xpath(page_elements.job['click_interviewer']).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(page_elements.job['right_move']).click()
            time.sleep(4)
            self.driver.find_element_by_xpath(page_elements.job['schedule_button_click']).click()
            time.sleep(10)

            print('------------------- Applicant interview schedule successfully-----------------------')
            self.ui_status_change = 'Pass'
        except exceptions.WebDriverException as status_change:
            print(status_change)

    def interviewModule(self):
        try:
            time.sleep(5)
            self.login('interviewer', 'Rajeshsir', 'admin@1234')
            try:
                login_statuss = self.driver.find_element_by_xpath(page_elements.login['login_success'])
                self.status_of_login = login_statuss.text
                assert self.status_of_login == 'Interviewer_R   '
                print("Interview login Sucessfully")
                self.ui_interview_login = 'Pass'
                print("**---------------------- In main screen ------------------------**")
            except exceptions.NoSuchElementException as login_status2:
                print(login_status2)

            self.driver.find_element_by_xpath(page_elements.job['interview_tab']).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(page_elements.job['job_advance_search']).click()
            time.sleep(5)

            job_name = self.driver.find_element_by_xpath(page_elements.job['search_job_role'])
            job_name.send_keys(self.job_name_sprint_version)
            job_name.send_keys(Keys.ARROW_DOWN)
            job_name.send_keys(Keys.ENTER)
            time.sleep(4)
            self.driver.execute_script("window.scrollTo(0,100);")
            try:
                search = self.driver.find_element_by_xpath(page_elements.job['job_search_button'])
                search.click()
                self.ui_interview_advance_search = 'Pass'
                time.sleep(5)
                print('------------------------Interview Advance Search Working Fine------------------')
            except exceptions.NoSuchElementException as jobSearch:
                print(jobSearch)

            self.driver.find_element_by_xpath(page_elements.job['provide_feedback']).click()
            time.sleep(5)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after)
            self.driver.execute_script("window.scrollTo(0,400);")
            time.sleep(5)
            Framework = Select(self.driver.find_element_by_xpath(page_elements.job['interview_res_rating']))
            Framework.select_by_visible_text('Develop')

            Academic = Select(self.driver.find_element_by_xpath(page_elements.job['interview_res_rat']))
            Academic.select_by_visible_text('Mature')
            time.sleep(3)

            comment1 = self.driver.find_element_by_xpath(page_elements.job['comments1']).send_keys("Good")
            time.sleep(2)
            comment2 = self.driver.find_element_by_xpath(page_elements.job['comments2']).send_keys("Better")
            time.sleep(2)

            comment2 = self.driver.find_element_by_xpath(page_elements.job['comments3']).send_keys("Best")
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(2)
            feedback = self.driver.find_element_by_xpath(page_elements.job['Shortlist']).click()
            self.driver.execute_script("window.scrollTo(200,200);")
            submit = self.driver.find_element_by_xpath(page_elements.job['submit_feedback']).click()
            time.sleep(5)
            window_goto = self.driver.window_handles[0]
            self.driver.switch_to.window(window_goto)
            self.driver.refresh()

            print('--------------------------- Feedback provided Sucessfully -------------------------------------')
            self.ui_interview_feedback = 'Pass'

        except exceptions.ElementNotInteractableException as error:
            print(error)
        # self.driver.refresh()


Object = CreateJobRole()
if Object.status_of_login.strip() == 'admin':
    Object.job_excel_read()
    Object.create_job_role()
    Object.job_advance_search()
    Object.feedback_form()
    Object.tag_interview_panel()
    Object.job_posting()
    Object.edit_job()
    Object.tag_candidate()
    Object.status_change()
    Object.interviewModule()
    Object.post_status_change()
    Object.sourcedCandidate()
else:
    Object.server_connection_error()
    Object.browser_close()
