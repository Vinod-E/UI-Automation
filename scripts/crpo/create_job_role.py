import crpo_login
import page_elements
import config
import time
import xlrd
import test_data_inputpath
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class CreateJobRole(crpo_login.CrpoLogin):
    def __init__(self):
        super(CreateJobRole, self).__init__()

        self.job_name = []
        self.file = []
        self.j_description = []
        self.j_location = []
        self.j_hm = []
        self.j_bu = []
        self.openings = []
        self.male_diversity = []
        self.female_diversity = []
        self.xl_selection_process = []
        self.xl_interview_stage_01 = []
        self.xl_interview_template_01 = []
        self.xl_interview_stage_02 = []
        self.xl_interview_template_02 = []
        self.xl_interview_stage_03 = []
        self.xl_interview_template_03 = []
        self.xl_tag_interviewers = []
        self.xl_eligibility_criteria = []
        self.xl_ec_stage = []
        self.xl_positive_status = []
        self.xl_negative_status = []
        self.xl_assign_stage_status = []
        self.xl_positive_stage_status_job = []
        self.xl_negative_stage_status_job = []
        self.xl_A1 = []
        self.xl_A1_T1 = []
        self.xl_hop_r_stage = []
        self.xl_hop_r_status = []
        self.xl_hop_e_stage = []
        self.xl_hop_e_status = []
        self.xl_hop_a_stage = []
        self.xl_hop_a_status = []
        self.xl_hop_hr_stage = []
        self.xl_hop_hr_status = []
        self.j_description_u = []
        self.xl_tag_req = []

        self.job_name_sprint_version = []
        self.job_name_grid_view = []

        self.job_name_breadcumb = ""
        self.tag_interviewers = ""
        self.selection_process_created = []

        self.ui_job_created = []
        self.ui_job_advance_search = []
        self.ui_selection_process = []
        self.ui_interview_stage1 = []
        self.ui_interview_stage2 = []
        self.ui_interview_stage3 = []
        self.ui_tag_interviews = []
        self.ui_ec_configure = []
        self.ui_task_configure = []
        self.ui_hopping_config = []
        self.ui_update_job = []
        self.ui_tag_requirement = []
        self.ui_un_tag_requirement = []

        self.ui_jobrole_tab = []
        self.ui_job_getbyid = []

        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_job'])
        if self.login_server == 'beta':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.job_sheet1 = workbook.sheet_by_index(1)

    def login(self):
        self.excel_read()
        self.crpo_login()

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
                self.j_bu.append(rows[5])
            if rows[6]:
                self.openings.append(str(int(rows[6])))
            if rows[7]:
                self.male_diversity.append(str(int(rows[7])))
            if rows[8]:
                self.female_diversity.append(str(int(rows[8])))
            if rows[9]:
                self.xl_selection_process.append((rows[9]))
            if rows[10]:
                self.xl_interview_stage_01.append(rows[10])
            if rows[11]:
                self.xl_interview_template_01.append(rows[11])
            if rows[12]:
                self.xl_interview_stage_02.append(rows[12])
            if rows[13]:
                self.xl_interview_template_02.append(rows[13])
            if rows[14]:
                self.xl_interview_stage_03.append(rows[14])
            if rows[15]:
                self.xl_interview_template_03.append(rows[15])
            if rows[16]:
                self.xl_tag_interviewers.append(rows[16])
            if rows[17]:
                self.xl_eligibility_criteria.append(rows[17])
            if rows[18]:
                self.xl_ec_stage.append(rows[18])
            if rows[19]:
                self.xl_positive_status.append(rows[19])
            if rows[20]:
                self.xl_negative_status.append(rows[20])
            if rows[21]:
                self.xl_assign_stage_status.append(rows[21])
            if rows[22]:
                self.xl_positive_stage_status_job.append(rows[22])
            if rows[23]:
                self.xl_negative_stage_status_job.append(rows[23])
            if rows[24]:
                self.xl_A1.append(rows[24])
            if rows[25]:
                self.xl_A1_T1.append(rows[25])
            if rows[26]:
                self.xl_hop_r_stage.append(rows[26])
            if rows[27]:
                self.xl_hop_r_status.append(rows[27])
            if rows[28]:
                self.xl_hop_e_stage.append(rows[28])
            if rows[29]:
                self.xl_hop_e_status.append(rows[29])
            if rows[30]:
                self.xl_hop_a_stage.append(rows[30])
            if rows[31]:
                self.xl_hop_a_status.append(rows[31])
            if rows[32]:
                self.xl_hop_hr_stage.append(rows[32])
            if rows[33]:
                self.xl_hop_hr_status.append(rows[33])
            if rows[34]:
                self.j_description_u.append(rows[34])
            if rows[35]:
                self.xl_tag_req.append(rows[35])

            for j in self.job_name:
                job_name = j
                self.job_name_sprint_version = job_name.format(self.sprint_version)

            for k in self.xl_tag_interviewers:
                interviewers = k
                self.tag_interviewers = interviewers

    def create_job_role(self):

        try:
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.job['job_tab']).click()
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.job['create_job_role']).click()
            time.sleep(10)
            self.driver.find_element_by_xpath(page_elements.job['Job_name'])\
                .send_keys(self.job_name_sprint_version)
            self.driver.find_element_by_xpath(page_elements.job['upload_job_file']).send_keys(self.file)
            self.driver.find_element_by_xpath(page_elements.job['job_description']).send_keys(self.j_description)

            location = self.driver.find_element_by_xpath(page_elements.job['job_location'])
            location.send_keys(self.j_location)
            location.send_keys(Keys.ARROW_DOWN)
            location.send_keys(Keys.ENTER)
            time.sleep(2)

            hiring_manager = self.driver.find_element_by_xpath(page_elements.job['job_hiring_manager'])
            hiring_manager.send_keys(self.j_hm)
            hiring_manager.send_keys(Keys.ARROW_DOWN)
            hiring_manager.send_keys(Keys.ENTER)
            time.sleep(2)

            business_unit = self.driver.find_element_by_xpath(page_elements.job['job_business_unit'])
            business_unit.send_keys(self.j_bu)
            business_unit.send_keys(Keys.ARROW_DOWN)
            business_unit.send_keys(Keys.ENTER)
            time.sleep(2)

            openings = self.driver.find_element_by_name(page_elements.job['job_openings'])
            openings.clear()
            openings.send_keys(self.openings)

            male = self.driver.find_element_by_xpath(page_elements.job['job_male_diversity'])
            male.clear()
            male.send_keys(self.male_diversity)

            female = self.driver.find_element_by_xpath(page_elements.job['job_female_diversity'])
            female.clear()
            female.send_keys(self.female_diversity)

            self.driver.find_element_by_xpath(page_elements.job['job_create_button']).click()
            time.sleep(5)

            self.driver.save_screenshot(config.configs['screen_shot'].format('Job'))

        except exceptions.NoSuchElementException as create_job:
            print create_job

        # ----------------------------------- duplicate job name case --------------------------------------------------
        # duplicate_job = self.driver.find_element_by_xpath('duplicate_job')
        # if duplicate_job.text == 'Requisition name already exists':
        #     self.driver.refresh()
        #     self.create_job_role()

        # ---------------------------- Checking whether the job created or not -----------------------------------------
        #     if self.driver.find_element_by_xpath(page_elements.job['jobrole_breadcrumbs']).is_displayed():
        try:
            job_name_from_breadcrumb = self.driver.find_element_by_xpath(page_elements.job['jobrole_breadcrumbs'])
            self.job_name_breadcumb = job_name_from_breadcrumb.text
        except exceptions.NoSuchElementException as e1:
            print (e1)

        # if self.driver.find_element_by_xpath(page_elements.job['job_from_grid_view']
        #                                                   .format(self.job_name_sprint_version)).is_displayed():
        # try:
        #     job_grid_view = self.driver.find_element_by_xpath(page_elements.job['job_getbyid']
        #                                                       .format(self.job_name_sprint_version))
        #     self.job_name_grid_view = job_grid_view.text
        # except exceptions.NoSuchElementException as e2:
        #     print (e2)

        if self.job_name_breadcumb == self.job_name_sprint_version:
            print('Job Created successfully')
            self.ui_job_created = 'Pass'

        elif self.job_name_sprint_version == self.job_name_grid_view:
            print('-----------------Job Created successfully-----------------')
        else:
            print('-----------------Job Creation Failed-----------------')

    def edit_job(self):

        self.driver.implicitly_wait(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                time.sleep(3)

                edit = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_edit_job'])
                edit.click()

                time.sleep(3)
                desc = self.driver.find_element_by_xpath(page_elements.job['job_description'])
                desc.send_keys(self.j_description_u)

                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['job_create_button']).click()
                print('-------------------- Job Edit/update successfully -----------------')
                self.ui_update_job = 'Pass'
                self.driver.refresh()
                time.sleep(10)

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def tag_requirement(self):
        self.driver.implicitly_wait(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()

                time.sleep(4)
                tag = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_tag_requirement'])
                tag.click()

                req = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_tag_requirement_field'])
                req.send_keys(self.xl_tag_req)
                req.send_keys(Keys.ARROW_DOWN)
                req.send_keys(Keys.ENTER)

                time.sleep(3)
                button = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_tag_requirement_button'])
                button.click()
                time.sleep(5)
                print('------------------------ Tag to requirement successfully ------------------------')
                self.ui_tag_requirement = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def un_tag_requirement(self):
        self.driver.implicitly_wait(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()

                time.sleep(5)
                tag = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_untag_requirement'])
                tag.click()

                ok = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_untag_requirement_ok'])
                ok.click()
                time.sleep(5)
                print('------------------------ Un_Tag to requirement successfully ------------------------')
                self.ui_un_tag_requirement = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def job_advance_search(self):
        try:
            self.driver.find_element_by_xpath(page_elements.job['job_tab']).click()
            time.sleep(5)
            self.ui_jobrole_tab = 'Pass'
            self.driver.find_element_by_xpath(page_elements.job['job_advance_search']).click()

            name = self.driver.find_element_by_name(page_elements.job['job_search_name_field'])
            time.sleep(3)
            name.click()
            name.send_keys(self.job_name_sprint_version)

            self.driver.find_element_by_xpath(page_elements.job['job_search_button']).click()
            time.sleep(5)

            self.driver.find_element_by_xpath(page_elements.job['job_getbyid']).click()
            time.sleep(3)
            print('---------------------Advance search is working fine ------------------')
            self.ui_job_advance_search = 'Pass'
            self.ui_job_getbyid = 'Pass'


        except exceptions.WebDriverException as search:
            print search

    def selection_process(self):

        # ---------------------------------- From Job details screen ---------------------------------------------------
        if self.job_name_breadcumb == self.job_name_sprint_version:

            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selection_process']).click()
                time.sleep(3)
                sp = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selectionProcess_text_field'])
                sp.send_keys(self.xl_selection_process)
                sp.send_keys(Keys.ARROW_DOWN)
                sp.send_keys(Keys.ENTER)

                try:
                    time.sleep(4)
                    sp_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selectionProcess_save'])
                    self.driver.implicitly_wait(5)
                    sp_save.click()
                    self.selection_process_created = 'Pass'
                    print('----------------------Selection Process configured successfully_01-------------------------')
                    self.ui_selection_process = 'Pass'

                except exceptions.ElementClickInterceptedException as save:
                    print(save)
            except exceptions.WebDriverException as config_message:
                print(config_message)

        if self.selection_process_created == 'Pass':
            pass
        else:
            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selection_process']).click()
                sp = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selectionProcess_text_field'])
                sp.send_keys(self.xl_selection_process)
                sp.send_keys(Keys.ARROW_DOWN)
                sp.send_keys(Keys.ENTER)

                try:
                    time.sleep(4)
                    sp_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_selectionProcess_save'])
                    sp_save.send_keys(Keys.DOWN)
                    sp_save.click()
                    print('----------------------Selection Process configured successfully_02-------------------------')
                    self.selection_process_created = 'Pass'
                except exceptions.ElementClickInterceptedException as save:
                    print(save)
            except exceptions.WebDriverException as config_message:
                print(config_message)

    def feedback_form(self):

        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                # -------------------------- Interview stage / feedback form configuration -----------------------------
                time.sleep(10)
                self.driver.refresh()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_feedback_form']).click()
                stage_01 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_configure'])
                stage_01.click()
                stage_01.send_keys(self.xl_interview_stage_01)
                stage_01.send_keys(Keys.ARROW_DOWN)
                stage_01.send_keys(Keys.ENTER)

                feedback_01 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_name_search'])
                feedback_01.send_keys(self.xl_interview_template_01)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_search_button']).click()
                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_use']).click()
                self.driver.find_element_by_xpath(page_elements.job['overall_comment_button']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['interview_reject_comment_button']).click()
                time.sleep(2)
                int_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_save_button'])
                int_save.send_keys(Keys.DOWN)
                int_save.click()
                print('-------------------interview feedback form configured successfully---------------------')
                self.ui_interview_stage1 = 'Pass'
            # ----------------------------------------------------------------------------------------------------------

                self.driver.implicitly_wait(5)
                stage_02 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_configure'])
                stage_02.clear()
                time.sleep(2)
                stage_02.send_keys(self.xl_interview_stage_02)
                stage_02.send_keys(Keys.ARROW_DOWN)
                stage_02.send_keys(Keys.ENTER)

                feedback_02 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_name_search'])
                feedback_02.send_keys(self.xl_interview_template_02)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_search_button']).click()
                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_use']).click()
                self.driver.find_element_by_xpath(page_elements.job['overall_comment_button']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['interview_reject_comment_button']).click()
                time.sleep(2)
                final_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_save_button'])
                final_save.send_keys(Keys.DOWN)
                final_save.click()
                time.sleep(6)
                print('-------------------Final interview feedback form configured successfully------------------')
                self.ui_interview_stage2 = 'Pass'
            # ----------------------------------------------------------------------------------------------------------

                self.driver.implicitly_wait(5)
                stage_03 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_configure'])
                stage_03.clear()
                time.sleep(2)
                stage_03.send_keys(self.xl_interview_stage_03)
                stage_03.send_keys(Keys.ARROW_DOWN)
                stage_03.send_keys(Keys.ENTER)

                feedback_03 = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_name_search'])
                feedback_03.send_keys(self.xl_interview_template_03)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_from_search_button']).click()
                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_form_use']).click()
                self.driver.find_element_by_xpath(page_elements.job['overall_comment_button']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['interview_reject_comment_button']).click()
                time.sleep(2)
                hr_save = self.driver.find_element_by_xpath(page_elements.job['getbyid_feedback_save_button'])
                hr_save.send_keys(Keys.DOWN)
                hr_save.click()
                time.sleep(5)
                print('-------------------HR interview feedback form configured successfully-----------------------')
                self.ui_interview_stage3 = 'Pass'
            except exceptions.WebDriverException as config_message:
                print(config_message)

    def tag_interview_panel(self):

        if self.job_name_breadcumb == self.job_name_sprint_version:
            self.driver.implicitly_wait(5)
            try:
                # --------------------------------------- Tag Interviewers----------------------------------------------
                self.driver.refresh()
                time.sleep(10)
                self.driver.find_element_by_xpath(page_elements.job['Floating_actions']).click()

                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['getbyid_menu_tag_interviewers']).click()

                time.sleep(5)
                # self.driver.find_element_by_xpath(page_elements.job['getbyid_tag_interviewers']).click()
                self.driver.find_element_by_xpath(page_elements.job['interview_panel'].format(
                    self.tag_interviewers)).click()

                time.sleep(4)
                add = self.driver.find_element_by_xpath(page_elements.job['add_interviewers_to_table'])
                add.click()
                time.sleep(6)
                self.driver.find_element_by_xpath(page_elements.job['save_interviewers_to_panel']).click()
                print('Interviewers are added to job role')
                print('-------------------Interviewers are added to job role-------------------------')
                self.ui_tag_interviews = 'Pass'
                time.sleep(5)

            except exceptions.WebDriverException as config_message:
                print('Tag interviewers :: ', config_message)
                self.driver.refresh()

    def ec_configurations_tab(self):
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:

                self.driver.implicitly_wait(10)
                self.driver.refresh()
                self.driver.find_element_by_xpath(page_elements.job['configuration_sub_tab']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['ec_configure']).click()
                time.sleep(5)
                ec = self.driver.find_element_by_xpath(page_elements.job['ec_text_field'])
                ec.send_keys(self.xl_eligibility_criteria)
                ec.send_keys(Keys.ARROW_DOWN)
                ec.send_keys(Keys.ENTER)

                time.sleep(3)
                p_ec_stage = self.driver.find_element_by_xpath(page_elements.job['ec_positive_stage'])
                p_ec_stage.send_keys(self.xl_ec_stage)
                p_ec_stage.send_keys(Keys.ARROW_DOWN)
                p_ec_stage.send_keys(Keys.ENTER)

                time.sleep(3)
                n_ec_status = self.driver.find_element_by_xpath(page_elements.job['ec_positive_status'])
                n_ec_status.send_keys(self.xl_positive_status)
                n_ec_status.send_keys(Keys.ARROW_DOWN)
                n_ec_status.send_keys(Keys.ENTER)

                time.sleep(3)
                n_ec_stage = self.driver.find_element_by_xpath(page_elements.job['ec_negative_stage'])
                n_ec_stage.send_keys(self.xl_ec_stage)
                n_ec_stage.send_keys(Keys.ARROW_DOWN)
                n_ec_stage.send_keys(Keys.ENTER)

                time.sleep(3)
                n_ec_status = self.driver.find_element_by_xpath(page_elements.job['ec_negative_status'])
                n_ec_status.send_keys(self.xl_negative_status)
                n_ec_status.send_keys(Keys.ARROW_DOWN)
                n_ec_status.send_keys(Keys.ENTER)

                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.job['ec_config_save']).click()
                print('----------------- Eligibility configuration done -------------------------- ')
                self.ui_ec_configure = 'Pass'

                time.sleep(5)
            except exceptions.NoSuchElementException as config_message:
                print(config_message)

    def task_configurations_tab(self):
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(page_elements.job['configuration_sub_tab']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.job['task_configure']).click()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['new_task_row']).click()
                time.sleep(5)
                assign_stage_status = self.driver.find_element_by_xpath(page_elements.job['task_stage_status'])
                assign_stage_status.send_keys(self.xl_assign_stage_status)
                assign_stage_status.send_keys(Keys.ARROW_DOWN)
                assign_stage_status.send_keys(Keys.ENTER)
                time.sleep(2)
                a1_positive_stage_status = self.driver.find_element_by_xpath(
                    page_elements.job['task_positive_stage_status'])
                a1_positive_stage_status.send_keys(self.xl_positive_stage_status_job)
                a1_positive_stage_status.send_keys(Keys.ARROW_DOWN)
                a1_positive_stage_status.send_keys(Keys.ENTER)
                time.sleep(2)
                a1_negative_stage_status = self.driver.find_element_by_xpath(
                    page_elements.job['task_negative_stage_status'])
                a1_negative_stage_status.send_keys(self.xl_negative_stage_status_job)
                a1_negative_stage_status.send_keys(Keys.ARROW_DOWN)
                a1_negative_stage_status.send_keys(Keys.ENTER)
                time.sleep(4)
                a1 = self.driver.find_element_by_xpath(page_elements.job['activity_1'])
                a1.send_keys(self.xl_A1)
                a1.send_keys(Keys.ARROW_DOWN)
                a1.send_keys(Keys.ENTER)
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Task_selection']).click()
                self.driver.find_element_by_xpath(page_elements.job['select_all_task']).click()
                done = self.driver.find_element_by_xpath(page_elements.job['task_selection_done'])
                done.click()
                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['activity_task_configuration_save']).click()
                print('-------------------- Job Task configuration done ------------------------------------')
                self.ui_task_configure = 'Pass'

            except exceptions.NoSuchElementException as config_message:
                print(config_message)

    def job_automation(self):
        time.sleep(5)
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(page_elements.job['automation_sub_tab']).click()

                aptitude_stage = self.driver.find_element_by_xpath(page_elements.job['aptitude_stage_hop'])
                aptitude_stage.click()
                time.sleep(2)
                a_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_stage'])
                a_h_stage.send_keys(self.xl_hop_a_stage)
                a_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_status'])
                a_h_stage.send_keys(self.xl_hop_a_status)

                eligible_stage = self.driver.find_element_by_xpath(page_elements.job['eligible_check_stage_hop'])
                eligible_stage.click()
                time.sleep(2)
                e_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_stage'])
                e_h_stage.send_keys(self.xl_hop_e_stage)
                e_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_status'])
                e_h_stage.send_keys(self.xl_hop_e_status)

                registration_stage = self.driver.find_element_by_xpath(page_elements.job['registration_stage_hop'])
                registration_stage.click()
                time.sleep(2)
                r_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_stage'])
                r_h_stage.send_keys(self.xl_hop_r_stage)
                r_h_status = self.driver.find_element_by_xpath(page_elements.job['hop_status'])
                r_h_status.send_keys(self.xl_hop_r_status)
                time.sleep(2)

                test_automation = self.driver.find_element_by_xpath(page_elements.job['test_automation_button'])
                test_automation.click()

                ec_on = self.driver.find_element_by_xpath(page_elements.job['ec_on_button'])
                ec_on.click()

                self.driver.implicitly_wait(5)
                save = self.driver.find_element_by_xpath(page_elements.job['Hopping_save_button'])
                save.click()
                time.sleep(4)
                # save1 = WebDriverWait(self.driver, 10).until(
                #     ec.element_to_be_selected((By.XPATH, '//*[@id="mainBodyElement"]/div[3]
                # /div/div[1]/div[4]/div/section/div[1]/button')))
                # save1.click()

                self.driver.refresh()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(page_elements.job['automation_sub_tab']).click()

                hr_int_stage = self.driver.find_element_by_xpath(page_elements.job['Hr_Interview_stage_hop'])
                hr_int_stage.click()
                time.sleep(2)
                hr_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_stage'])
                hr_h_stage.send_keys(self.xl_hop_hr_stage)
                hr_h_stage = self.driver.find_element_by_xpath(page_elements.job['hop_status'])
                hr_h_stage.send_keys(self.xl_hop_hr_status)

                ready_to_schedule = self.driver.find_element_by_xpath(page_elements.job['ready_schedule_button'])
                ready_to_schedule.click()

                self.driver.implicitly_wait(5)
                save = self.driver.find_element_by_xpath(page_elements.job['Hopping_save_button'])
                save.send_keys(Keys.UP)
                save.click()
                time.sleep(4)

                print('--------------------------- hopping set done -------------------------------------')
                self.ui_hopping_config = 'Pass'
            except exceptions.NoSuchElementException as config_message:
                print(config_message)


# Object = CreateJobRole()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.job_excel_read()
#     Object.create_job_role()
#     # Object.job_advance_search()
#     Object.selection_process()
#     Object.feedback_form()
#     Object.tag_interview_panel()
#     Object.ec_configurations_tab()
#     Object.task_configurations_tab()
#     Object.job_automation()
#     Object.browser_close()
# else:
#     Object.server_connection_error()
#     Object.browser_close()
