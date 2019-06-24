import time
import xlrd
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import test_data_inputpath
import page_elements
import create_test


class CreateEvent(create_test.CreateTest):

    def __init__(self):
        super(CreateEvent, self).__init__()

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

        self.event_name_sprint_version = []
        self.job_name_sprint_version = []
        self.req_name_sprint_version = []
        self.loop_v = []
        self.grid_event_name = []

        self.ui_create_event = []
        self.ui_event_task_config = []

        workbook = xlrd.open_workbook(test_data_inputpath.test_data_file['create_event'])
        if self.login_server == 'beta':
            self.sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.sheet1 = workbook.sheet_by_index(1)

    def login(self):
        self.excel_read()
        self.crpo_login()

    def event_excel_read(self):
        # --------------------------------------Event details-----------------------------------------------------------
        for i in range(1, self.sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.sheet1.row_values(number)

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

            for j in self.xl_event_name:
                event_name = j
                self.event_name_sprint_version = event_name.format(self.sprint_version)

            for k in self.xl_req_name:
                req_name = k
                self.req_name_sprint_version = req_name.format(self.sprint_version)

            for l in self.xl_job_name:
                job_name = l
                self.job_name_sprint_version = job_name.format(self.sprint_version)

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

            time.sleep(4)
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

            em = self.driver.find_element_by_xpath(page_elements.event['event_manager'])
            em.send_keys(self.xl_em)
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
                    print('------------------- Event name is validated ------------------')
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

                time.sleep(3)
                add_row = self.driver.find_element_by_xpath(page_elements.job['new_task_row'])
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

            except exceptions.ElementNotInteractableException as error:
                print(error)


# Object = CreateEvent()
# Object.login()
# if Object.status_of_login == 'administrator':
#     Object.event_excel_read()
#     Object.create_event()
#     Object.event_task_configure()
#     Object.browser_close()
