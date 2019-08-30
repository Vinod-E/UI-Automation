import time
import xlrd
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import test_data_inputpath
import page_elements
import create_test
from datetime import datetime


class CreateEvent(create_test.CreateTest):

    def __init__(self):
        super(CreateEvent, self).__init__()
        now = datetime.now()
        self.xl_event_from_date = now.strftime("%d/%m/%Y")
        self.xl_event_to_date = now.strftime("%d/%m/%Y")

        self.xl_event_name = []
        self.xl_req_name = []
        self.xl_job_name = []
        self.xl_slot = []
        self.xl_em = []
        self.xl_college = []
        self.xl_stage_status = []
        self.xl_positive_stage_status_Event = []
        self.xl_activity = []
        self.xl_task1 = []
        self.xl_task2 = []
        self.xl_task3 = []
        self.xl_task4 = []
        self.xl_event_test_name = []
        self.xl_event_test_stage = []
        self.xl_hopping_positive_status = []
        self.xl_hopping_negative_status = []
        self.xl_change_applicant_stage = []
        self.xl_change_applicant_status = []
        self.xl_change_status_comment = []
        self.xl_upload_candidate_name = []
        self.xl_call_back_status = []
        self.xl_total_tasks = []
        self.xl_completed_tasks = []
        self.xl_pending_tasks = []
        self.xl_submitted_tasks = []
        self.xl_rejected_tasks = []
        self.Upload_candidateName = ""
        self.hopping_positive_status = ""
        self.change_applicant_status = ""
        self.call_back_status = ""
        self.total_tasks = ""
        self.completed_tasks = ""
        self.pending_tasks = ""
        self.submitted_tasks = ""
        self.rejected_tasks = ""

        self.event_name_sprint_version = []
        self.job_name_sprint_version = []
        self.req_name_sprint_version = []
        self.event_test_sprint_version = []
        self.loop_v = []
        self.grid_event_name = []

        self.ui_create_event = []
        self.ui_event_task_config = []
        self.ui_event_test_config = []
        self.ui_event_owner_config = []
        self.ui_event_upload_candidate = []
        self.ui_event_applicants = []
        self.ui_event_applicant_search = []
        self.ui_event_applicant_getby = []
        self.ui_event_advance_search = []
        self.ui_applicant_current_status = []
        self.ui_ec_eligible = []
        self.ui_tag_to_test = []
        self.ui_task_candidate_name = []
        self.ui_call_back_status = []
        self.ui_total_tasks = []
        self.ui_approved_tasks = []
        self.ui_pending_tasks = []
        self.ui_submitted_tasks = []
        self.ui_rejected_tasks = []
        self.ui_a2_assignment = []

        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_event'])
        if self.login_server == 'beta':
            self.event_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.event_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.event_sheet1 = workbook.sheet_by_index(1)

        workbook1 = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['upload_candidate_file'])
        self.upload_sheet = workbook1.sheet_by_index(0)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def event_excel_read(self):
        # --------------------------------------candidate details-------------------------------------------------------
        for i in range(1, self.upload_sheet.nrows):
            number = i  # Counting number of rows
            rows = self.upload_sheet.row_values(number)

            if rows[0]:
                self.xl_upload_candidate_name.append(rows[0])
            for s in self.xl_upload_candidate_name:
                self.Upload_candidateName = s
        # --------------------------------------Event details-----------------------------------------------------------
        for i in range(1, self.event_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.event_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name.append(rows[0])
            if rows[1]:
                self.xl_req_name.append(rows[1])
            if rows[2]:
                self.xl_job_name.append(str(rows[2]))
            if rows[3]:
                self.xl_slot.append(str(rows[3]))
            if rows[4]:
                self.xl_em.append(str(rows[4]))
            if rows[5]:
                self.xl_college.append(str(rows[5]))
            if rows[6]:
                self.xl_stage_status.append(str(rows[6]))
            if rows[7]:
                self.xl_positive_stage_status_Event.append(str(rows[7]))
            if rows[8]:
                self.xl_activity.append(str(rows[8]))
            if rows[9]:
                self.xl_task1.append(str(rows[9]))
            if rows[10]:
                self.xl_task3.append(str(rows[10]))
            if rows[11]:
                self.xl_task2.append(str(rows[11]))
            if rows[12]:
                self.xl_task4.append(str(rows[12]))
            if rows[13]:
                self.xl_event_test_name.append(str(rows[13]))
            if rows[14]:
                self.xl_event_test_stage.append(str(rows[14]))
            if rows[15]:
                self.xl_hopping_positive_status.append(str(rows[15]))
            if rows[16]:
                self.xl_hopping_negative_status.append(str(rows[16]))
            if rows[17]:
                self.xl_change_applicant_stage.append(str(rows[17]))
            if rows[18]:
                self.xl_change_applicant_status.append(str(rows[18]))
            if rows[19]:
                self.xl_change_status_comment.append(str(rows[19]))
            if rows[20]:
                self.xl_call_back_status.append(str(rows[20]))
            if rows[21]:
                self.xl_total_tasks.append(int(rows[21]))
            if rows[22]:
                self.xl_completed_tasks.append(int(rows[22]))
            if rows[23]:
                self.xl_pending_tasks.append(int(rows[23]))
            if rows[24]:
                self.xl_submitted_tasks.append(int(rows[24]))
            if rows[25]:
                self.xl_rejected_tasks.append(int(rows[25]))

            for j in self.xl_event_name:
                event_name = j
                self.event_name_sprint_version = event_name.format(self.sprint_version)

            for k in self.xl_req_name:
                req_name = k
                self.req_name_sprint_version = req_name.format(self.sprint_version)

            for l in self.xl_job_name:
                job_name = l
                self.job_name_sprint_version = job_name.format(self.sprint_version)

            for v in self.xl_event_test_name:
                test_name = v
                self.event_test_sprint_version = test_name.format(self.sprint_version)

            for x in self.xl_hopping_positive_status:
                self.hopping_positive_status = x
            for y in self.xl_change_applicant_status:
                self.change_applicant_status = y
            for z in self.xl_call_back_status:
                self.call_back_status = z
            for a in self.xl_total_tasks:
                self.total_tasks = a
            for b in self.xl_pending_tasks:
                self.pending_tasks = b
            for c in self.xl_completed_tasks:
                self.completed_tasks = c
            for d in self.xl_submitted_tasks:
                self.submitted_tasks = d
            for e in self.xl_rejected_tasks:
                self.rejected_tasks = e

    def create_event(self):
        try:
            time.sleep(5)
            event_tab = self.driver.find_element_by_xpath(page_elements.event['event_tab'])
            event_tab.click()
            time.sleep(10)

            new_event = self.driver.find_element_by_xpath(page_elements.event['new_event_button'])
            new_event.click()

            time.sleep(5)
            event_name = self.driver.find_element_by_xpath(page_elements.event['event_name'])
            event_name.send_keys(self.event_name_sprint_version)

            req_name = self.driver.find_element_by_xpath(page_elements.event['event_req_name'])
            req_name.send_keys(self.req_name_sprint_version)
            req_name.send_keys(Keys.ARROW_DOWN)
            req_name.send_keys(Keys.ENTER)

            time.sleep(6)
            job_name_field = self.driver.find_element_by_xpath(page_elements.event['event_job_name_field'])
            job_name_field.click()

            job_name_search = self.driver.find_element_by_xpath(page_elements.event['event_job_name_text'])
            job_name_search.send_keys(self.job_name_sprint_version)

            job_selection = self.driver.find_element_by_xpath(page_elements.event['event_job_selection'])
            job_selection.click()
            time.sleep(3)
            done = self.driver.find_element_by_xpath(page_elements.event['selection_done'])
            done.click()

            slot = self.driver.find_element_by_xpath(page_elements.event['slot'])
            slot.send_keys(self.xl_slot)
            slot.send_keys(Keys.ARROW_DOWN)
            slot.send_keys(Keys.ENTER)
            time.sleep(3)

            from_date = self.driver.find_element_by_xpath(page_elements.event['from_date'])
            from_date.send_keys(self.xl_event_from_date)

            to_date = self.driver.find_element_by_xpath(page_elements.event['to_date'])
            to_date.send_keys(self.xl_event_to_date)

            em = self.driver.find_element_by_xpath(page_elements.event['event_manager'])
            em.send_keys(self.xl_em)
            time.sleep(2)
            em.send_keys(Keys.ARROW_DOWN)
            em.send_keys(Keys.ENTER)
            time.sleep(3)

            college = self.driver.find_element_by_xpath(page_elements.event['college'])
            college.send_keys(self.xl_college)
            college.send_keys(Keys.ARROW_DOWN)
            college.send_keys(Keys.ENTER)
            time.sleep(3)

            ec_enable = self.driver.find_element_by_xpath(page_elements.event['ec_enable'])
            ec_enable.click()

            time.sleep(5)
            create = self.driver.find_element_by_xpath(page_elements.event['create_event_button'])
            create.send_keys(Keys.DOWN)
            create.click()
            print('Event created successfully')
            self.ui_create_event = 'Pass'

            # ------------------------------ validating the event name -------------------------------------------------
            try:
                time.sleep(4)

                test_name = self.driver.find_element_by_xpath(
                    page_elements.test['grid_test_name'].format(self.event_name_sprint_version))
                self.grid_event_name = test_name.text
                if self.grid_event_name == self.event_name_sprint_version:
                    print('------------------ Event name is validated ------------------')
            except exceptions.ElementNotInteractableException as e:
                print(e)
        except exceptions.ElementNotInteractableException as error:
            print(error)

    def event_task_configure(self):

        if self.grid_event_name == self.event_name_sprint_version:

            try:
                config_tab = self.driver.find_element_by_xpath(page_elements.event['event_config_tab'])
                config_tab.send_keys(Keys.UP)
                config_tab.click()
                time.sleep(5)

                configure_task = self.driver.find_element_by_xpath(page_elements.event['event_task_configure'])
                configure_task.click()

                time.sleep(2)
                add_row = self.driver.find_element_by_xpath(page_elements.job['new_task_row'])
                time.sleep(2.2)
                add_row.click()

                time.sleep(5)
                job_name = self.driver.find_element_by_xpath(page_elements.event['task_config_job'])
                job_name.send_keys(self.job_name_sprint_version)
                job_name.send_keys(Keys.ARROW_DOWN)
                job_name.send_keys(Keys.ENTER)

                time.sleep(5)
                assign_stage_status = self.driver.find_element_by_xpath(page_elements.event['task_stage_status'])
                assign_stage_status.send_keys(self.xl_stage_status)
                assign_stage_status.send_keys(Keys.ARROW_DOWN)
                assign_stage_status.send_keys(Keys.ENTER)

                time.sleep(5)
                a1_positive_stage_status = self.driver.find_element_by_xpath(
                    page_elements.event['task_positive_stage_status'])
                a1_positive_stage_status.send_keys(self.xl_positive_stage_status_Event)
                a1_positive_stage_status.send_keys(Keys.ARROW_DOWN)
                a1_positive_stage_status.send_keys(Keys.ENTER)

                time.sleep(5)
                a1 = self.driver.find_element_by_xpath(page_elements.job['activity_1'])
                a1.send_keys(self.xl_activity)
                a1.send_keys(Keys.ARROW_DOWN)
                a1.send_keys(Keys.ENTER)

                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.job['Task_selection']).click()

                task_1 = self.driver.find_element_by_xpath(page_elements.event['task_search_in_configure'])
                task_1.send_keys(self.xl_task1)
                self.driver.find_element_by_xpath(page_elements.job['select_all_task']).click()

                task_2 = self.driver.find_element_by_xpath(page_elements.event['task_search_in_configure'])
                task_2.send_keys(self.xl_task2)
                self.driver.find_element_by_xpath(page_elements.job['select_all_task']).click()

                task_3 = self.driver.find_element_by_xpath(page_elements.event['task_search_in_configure'])
                task_3.send_keys(self.xl_task3)
                self.driver.find_element_by_xpath(page_elements.job['select_all_task']).click()

                task_4 = self.driver.find_element_by_xpath(page_elements.event['task_search_in_configure'])
                task_4.send_keys(self.xl_task4)
                self.driver.find_element_by_xpath(page_elements.job['select_all_task']).click()

                done = self.driver.find_element_by_xpath(page_elements.job['task_selection_done'])
                done.click()

                time.sleep(4)
                self.driver.find_element_by_xpath(page_elements.job['activity_task_configuration_save']).click()
                print('------------------ Event Task configuration done -----------------------')
                self.ui_event_task_config = 'Pass'
                time.sleep(2.2)

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def event_test_configure(self):

        if self.grid_event_name == self.event_name_sprint_version:

            try:
                self.driver.refresh()
                time.sleep(5)
                configure_test = self.driver.find_element_by_xpath(page_elements.event['Event_test_configure'])
                configure_test.click()

                time.sleep(3)
                jobrole = self.driver.find_element_by_xpath(page_elements.event['test_jobrole'])
                jobrole.send_keys(self.job_name_sprint_version)
                jobrole.send_keys(Keys.ARROW_DOWN)
                jobrole.send_keys(Keys.ENTER)

                time.sleep(3)
                stage = self.driver.find_element_by_xpath(page_elements.event['test_stage'])
                stage.send_keys(self.xl_event_test_stage)
                stage.send_keys(Keys.ARROW_DOWN)
                stage.send_keys(Keys.ENTER)

                time.sleep(3)
                test = self.driver.find_element_by_xpath(page_elements.event['test_name'])
                test.send_keys(self.event_test_sprint_version)
                test.send_keys(Keys.ARROW_DOWN)
                test.send_keys(Keys.ENTER)

                time.sleep(3)
                active = self.driver.find_element_by_xpath(page_elements.event['test_active'])
                active.click()

                time.sleep(3)
                save = self.driver.find_element_by_xpath(page_elements.event['test_save'])
                save.click()

                print('------------------ Event Test configuration has been done -----------------------')
                self.ui_event_test_config = 'Pass'
                time.sleep(2.2)

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def event_owner_configure(self):

        if self.grid_event_name == self.event_name_sprint_version:

            try:
                self.driver.refresh()
                time.sleep(5)
                owner_tab = self.driver.find_element_by_xpath(page_elements.event['event_owner_tab'])
                owner_tab.click()

                time.sleep(3)
                edit_owner = self.driver.find_element_by_xpath(page_elements.event['event_owner_edit'])
                edit_owner.click()

                time.sleep(3)
                add_int = self.driver.find_element_by_xpath(page_elements.event['event_interviewer_add'])
                add_int.click()
                time.sleep(3)
                add_int.send_keys(Keys.END)

                # time.sleep(3)
                # custom_users = self.driver.find_element_by_xpath(page_elements.event['event_custom_users'])
                # custom_users.click()

                # time.sleep(3)
                # role = self.driver.find_element_by_xpath(page_elements.event['role'])
                # role.send_keys('Event AEE')
                # role.send_keys(Keys.ARROW_DOWN)
                # role.send_keys(Keys.ENTER)
                # time.sleep(5)
                # role.send_keys(Keys.END)
                # self.driver.find_element_by_xpath(page_elements.event['custom_owner_add'])
                #
                time.sleep(3)
                update = self.driver.find_element_by_css_selector(page_elements.event['update_owners'])
                update.send_keys(Keys.ARROW_DOWN)
                update.click()

                time.sleep(5)
                print('------------------ Event Owners has been added -----------------------')
                self.ui_event_owner_config = 'Pass'

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def upload_candidates_to_event(self):
        if self.grid_event_name == self.event_name_sprint_version:

            try:
                self.driver.refresh()
                time.sleep(5)
                self.driver.find_element_by_xpath(page_elements.event['Floating_actions']).click()
                time.sleep(3)
                self.driver.find_element_by_xpath(page_elements.event['event_upload_candidates']).click()
                upload_file = self.driver.find_element_by_xpath(page_elements.event['event_upload_file'])
                upload_file.send_keys(test_data_inputpath.crpo_test_data_file['upload_candidate_file'])
                time.sleep(10)
                next_button = self.driver.find_element_by_xpath(page_elements.event['Next_Button'])
                next_button.click()
                time.sleep(4)
                declare = self.driver.find_element_by_xpath(page_elements.event['declare_checkbox'])
                declare.click()
                time.sleep(3)
                signature = self.driver.find_element_by_xpath(page_elements.event['signature'])
                signature.send_keys(Keys.DOWN)
                signature.send_keys('AutomationV')
                agree = self.driver.find_element_by_xpath(page_elements.event['Agree'])
                agree.click()
                time.sleep(4)
                save_uploads = self.driver.find_element_by_xpath(page_elements.event['save_uploads'])
                save_uploads.click()

                time.sleep(2.9)
                t = self.driver.find_element_by_xpath(page_elements.event['upload_candidate_count'])
                if t.text == 'Uploaded 1':
                    self.ui_event_upload_candidate = 'Pass'
                    print '----------------- Candidate created ---------------------------'
                else:
                    print '------------------------ Candidate creation Failed ----------------------'

                self.driver.find_element_by_xpath(page_elements.event['close_pop_details_window']).click()
                time.sleep(5.5)

            except exceptions.ElementNotInteractableException as error:
                print(error)

    def view_upload_candidates(self):
        event_tab = self.driver.find_element_by_xpath(page_elements.event['event_tab'])
        event_tab.click()

        time.sleep(2.22)
        search = self.driver.find_element_by_xpath(page_elements.event['Event_advance_search'])
        search.click()
        self.driver.find_element_by_name(page_elements.event['event_names']).send_keys(self.event_name_sprint_version)
        self.driver.find_element_by_xpath(page_elements.event['event_search_button']).click()
        time.sleep(1.2)
        self.driver.find_element_by_xpath(page_elements.event['Click_on_event_name']).click()
        self.ui_event_advance_search = 'Pass'
        time.sleep(1.2)

        if self.grid_event_name == self.event_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(10)
                self.driver.find_element_by_xpath(page_elements.event['Floating_actions']).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.event['View_Applicants']).click()
                self.ui_event_applicants = 'Pass'

                # --------------------------- Applicant Advance search -------------------
                time.sleep(2.5)
                advance_search = self.driver.find_element_by_xpath(page_elements.event['applicant_advance_search'])
                time.sleep(2)
                advance_search.click()
                applicant_name = self.driver.find_element_by_name(page_elements.event['applicant_name'])
                applicant_name.send_keys(self.Upload_candidateName)
                self.ui_event_applicant_search = 'Pass'
                time.sleep(2)
                self.driver.find_element_by_xpath(page_elements.event['applicant_search_button']).click()

                # --------------------------- Applicant Get By Id -------------------
                time.sleep(3)
                applicant_getbyid = self.driver.find_element_by_xpath(
                    page_elements.event['applicant_getbyid'].format(self.Upload_candidateName))
                applicant_getbyid.click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2.5)

                applicant_validate = self.driver.find_element_by_xpath(page_elements.event['applicant_validate'])
                if applicant_validate.text == self.Upload_candidateName:
                    self.ui_event_applicant_getby = 'Pass'
                    print "------------------ Applicant validated ---------------------"

                positive_hopping = self.driver.find_element_by_xpath(
                    page_elements.event['current_status'].format(self.hopping_positive_status))
                if positive_hopping.text == self.hopping_positive_status:
                    self.ui_ec_eligible = 'Pass'
                    self.ui_tag_to_test = 'Pass'
                    print "----------------- EC and Tag to test successfully ---------------"

                time.sleep(3.5)
                self.browser_close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            except exceptions.ElementNotInteractableException as error:
                print(error)

    def event_change_applicant_status(self):
        try:
            self.driver.refresh()
            self.driver.implicitly_wait(5)
            # --------------------------- Change Applicant Status -------------------
            self.driver.find_element_by_name(page_elements.event['applicant_select_checkbox']).click()
            time.sleep(2.4)
            change_applicant_status = \
                self.driver.find_element_by_xpath(page_elements.event['Change_applicant_status'])
            change_applicant_status.click()
            time.sleep(1.5)
            stage = self.driver.find_element_by_xpath(page_elements.event['change_stage'])
            stage.send_keys(self.xl_change_applicant_stage)

            status = self.driver.find_element_by_xpath(page_elements.event['change_status'])
            status.send_keys(self.xl_change_applicant_status)

            comment = self.driver.find_element_by_xpath(page_elements.event['comment'])
            comment.send_keys(self.xl_change_status_comment)
            time.sleep(1.9)
            self.driver.find_element_by_xpath(page_elements.event['change_button']).click()

            # --------------------------- Applicant Advance search -------------------
            time.sleep(5)
            advance_search = self.driver.find_element_by_xpath(page_elements.event['applicant_advance_search'])
            time.sleep(2.3)
            advance_search.click()
            applicant_name = self.driver.find_element_by_name(page_elements.event['applicant_name'])
            applicant_name.send_keys(self.Upload_candidateName)
            time.sleep(2)
            self.driver.find_element_by_xpath(page_elements.event['applicant_search_button']).click()

            # --------------------------- Applicant Get By Id -------------------
            time.sleep(3)
            applicant_getbyid = self.driver.find_element_by_xpath(
                page_elements.event['applicant_getbyid'].format(self.Upload_candidateName))
            applicant_getbyid.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2.5)

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format(self.change_applicant_status))
            if current_status.text == self.change_applicant_status:
                self.ui_applicant_current_status = 'Pass'
                print "------------------- Change applicant status successfully -----------------"

        except exceptions.ElementNotInteractableException as error:
            print(error)

    def task_assignment(self):
        try:
            time.sleep(2.5)
            self.driver.find_element_by_xpath(page_elements.event['candidate_details_floating_actions']).click()
            time.sleep(2.5)
            self.driver.find_element_by_xpath(page_elements.event['manage_task']).click()

            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(2.5)
            task_candidate_name = self.driver.find_element_by_xpath(page_elements.event['task_candidate_name'])
            if self.Upload_candidateName in task_candidate_name.text:
                self.ui_task_candidate_name = 'Pass'

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except exceptions.ElementNotInteractableException as error:
            print(error)

    def pofu_app(self):
        try:
            time.sleep(2.2)
            more_tabs = self.driver.find_element_by_xpath(page_elements.event['more_tabs'])
            more_tabs.click()
            time.sleep(5.5)
            embrace_tab = self.driver.find_element_by_xpath(page_elements.pofu['POFU_App'])
            embrace_tab.click()

            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.implicitly_wait(10)
            pofu_candi_tab = self.driver.find_element_by_xpath(page_elements.pofu['pofu_candidates_tab'])
            pofu_candi_tab.click()

            time.sleep(5)
            search = self.driver.find_element_by_xpath(page_elements.pofu['pofu_candidates_advance_search'])
            search.click()

            name = self.driver.find_element_by_xpath(page_elements.pofu['pofu_candi_text_box'])
            name.send_keys(self.Upload_candidateName)

            time.sleep(2.2)
            search_button = self.driver.find_element_by_xpath(page_elements.pofu['pofu_search_button'])
            search_button.click()

            time.sleep(5.2)
            behalf = self.driver.find_element_by_xpath(page_elements.pofu['submit_behalf_of'])
            behalf.click()

            time.sleep(2.5)
            task_01 = self.driver.find_element_by_name(page_elements.pofu['task_acceptance'])
            task_01.click()

            submit = self.driver.find_element_by_xpath(page_elements.pofu['submit_task'])
            submit.click()
            time.sleep(5)

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except exceptions.ElementNotInteractableException as error:
            print(error)

    def candidate_status(self):
        try:
            # --------------------------- Applicant Advance search -------------------
            time.sleep(3.9)
            applicant_name = self.driver.find_element_by_name(page_elements.event['applicant_name'])
            applicant_name.clear()
            applicant_name.send_keys(self.Upload_candidateName)
            time.sleep(2)
            self.driver.find_element_by_xpath(page_elements.event['applicant_search_button']).click()

            # --------------------------- Applicant Get By Id -------------------
            time.sleep(3)
            applicant_getbyid = self.driver.find_element_by_xpath(
                page_elements.event['applicant_getbyid'].format(self.Upload_candidateName))
            applicant_getbyid.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2.5)

            current_status = self.driver.find_element_by_xpath(
                page_elements.event['current_status'].format(self.call_back_status))
            if current_status.text == self.call_back_status:
                self.ui_call_back_status = 'Pass'
                print "------------------- call back activity successfully -----------------"

            time.sleep(2.5)
            self.driver.find_element_by_xpath(page_elements.event['candidate_details_floating_actions']).click()
            time.sleep(2.5)
            self.driver.find_element_by_xpath(page_elements.event['manage_task']).click()

            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(5)

            # ---------------- Total tasks --------------
            total = self.driver.find_element_by_xpath(page_elements.event['total_tasks'])
            if str(self.total_tasks) in total.text:
                self.ui_total_tasks = 'Pass'
                self.ui_a2_assignment = 'Pass'

            # ---------------- Approved tasks --------------
            approved = self.driver.find_element_by_xpath(page_elements.event['approved_tasks'])
            if str(self.completed_tasks) in approved.text:
                self.ui_approved_tasks = 'Pass'

            # ---------------- Pending tasks --------------
            pending = self.driver.find_element_by_xpath(page_elements.event['pending_tasks'])
            if str(self.pending_tasks) in pending.text:
                self.ui_pending_tasks = 'Pass'

            # ---------------- Submitted tasks --------------
            submitted = self.driver.find_element_by_xpath(page_elements.event['submitted_tasks'])
            if str(self.submitted_tasks) in submitted.text:
                self.ui_submitted_tasks = 'Pass'

            # ---------------- Rejected tasks --------------
            rejected = self.driver.find_element_by_xpath(page_elements.event['rejected_tasks'])
            if str(self.rejected_tasks) in rejected.text:
                self.ui_rejected_tasks = 'Pass'

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(5)

        except exceptions.ElementNotInteractableException as error:
            print(error)


# Object = CreateEvent()
# Object.login()
# Object.event_excel_read()
# if Object.status_of_login == 'administrator':
#     Object.create_event()
#     Object.event_task_configure()
#     time.sleep(6)
#     Object.upload_candidates_to_event()
#     Object.view_upload_candidates()
#     Object.driver.switch_to.window(Object.driver.window_handles[0])
#     Object.browser_close()
