import time
import webdriver_functions
from datetime import datetime
import xlwt
import xlrd
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class AmitTesting(webdriver_functions.WebdriverFunctions):
    def __init__(self):
        super(AmitTesting, self).__init__()
        self.driver = webdriver.Chrome('E:\\hirepro_automation\\UI-Automation\\drivers\\chromedriver.exe')
        self.driver.get('https://amsin.hirepro.in/staffing/#/login/')
        self.driver.maximize_window()

        now = datetime.now()
        self.__current_DateTime = now.strftime("%d-%m-%Y")
        self.__style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')
        self.__style1 = xlwt.easyxf('font: name Times New Roman, color-index green, bold on')
        self.__style2 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
        self.wb_result = xlwt.Workbook()
        self.ws = self.wb_result.add_sheet('create_form_ui_automation')
        self.ws.write(0, 0, 'Status', self.__style0)
        self.ws.write(0, 1, 'textField', self.__style0)
        self.ws.write(0, 2, 'dateAndTime', self.__style0)
        self.ws.write(0, 3, 'dropdownField', self.__style0)
        self.ws.write(0, 4, 'radioButtonField', self.__style0)
        self.ws.write(0, 5, 'checkboxField', self.__style0)
        self.ws.write(0, 6, 'textAreaField', self.__style0)
        self.ws.write(0, 7, 'dateField', self.__style0)
        self.ws.write(0, 8, 'timeField', self.__style0)
        self.ws.write(0, 9, 'videoField', self.__style0)
        self.ws.write(0, 10, 'linkField', self.__style0)

        self.input_file = xlrd.open_workbook('E:\Create Form UI Automation\Input Excel For Create Form.xls')
        self.sheet_name = self.input_file.sheet_names()
        print(self.sheet_name)
        self.inputFileByIndex = self.input_file.sheet_by_index(0)

    def login(self):
        tenant = self.driver.find_element_by_name('alias')
        tenant.send_keys('pofu')

        next = self.driver.find_element_by_xpath('//*[@ng-click="vm.getTenantConfiguration(vm.tenantAlias);$hide();"]')

        time.sleep(5)
        next.click()
        time.sleep(5)
        login = self.driver.find_element_by_name("userName")
        login.send_keys("admin")
        time.sleep(5)
        next = self.driver.find_element_by_xpath('//*[@ng-click="vm.validateUserName()"]')
        next.click()
        time.sleep(5)
        enter_password = self.driver.find_element_by_name("new-password")
        enter_password.send_keys("charuk@123")
        checkbox = self.driver.find_element_by_xpath('//*[@ng-model="vm.secureImageAccess"]')
        checkbox.click()
        time.sleep(5)
        login = self.driver.find_element_by_xpath('//*[@ng-click="vm.login()"]')
        login.click()
        time.sleep(15)

    def create_form(self):
        self.web_element_click_xpath('//*[@ui-sref="pofu.activity.forms.info"]')
        # form = self.driver.find_element_by_xpath('//*[@ui-sref="pofu.activity.forms.info"]').click()
        # time.sleep(12)

        create_new_form = self.driver.find_element_by_xpath('//*[@ng-if="vm.isAdmin"]').click()
        time.sleep(5)
        form_name = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.formType.Name"]')
        with open("E:\Create Form UI Automation\create form.txt", 'r') as f:
            a = f.readline()
            f.close()

        name = self.inputFileByIndex.cell(1, 0).value
        final_name = name + str(a)
        print(final_name)
        a = int(a) + 1
        with open("E:\Create Form UI Automation\create form.txt", 'w') as e:
            e.write(str(a))
            e.close()
        form_name.send_keys(final_name)
        time.sleep(5)
        form_title = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.formType.Title"]')
        form_title.send_keys(final_name)
        time.sleep(5)
        create_next = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.goToNextTab();"]')
        create_next.click()
        time.sleep(5)

        field_type = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]')
        field_type.click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(1)
        time.sleep(3)
        text_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        text_field.send_keys("candidate name")
        time.sleep(3)
        add_text_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select.select_by_index(2)
        date_time = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        date_time.send_keys("date and time")
        time.sleep(2)
        add_date_time = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select.select_by_index(3)
        drop_down = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        drop_down.send_keys("College")
        time.sleep(5)
        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.CatalogMasterName"]'))
        select.select_by_index(19)
        time.sleep(8)
        add_drop_down = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(4)
        radio_button = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        radio_button.send_keys("gender")
        radio_button = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]')
        radio_button.send_keys("male,female")
        add_radio_button = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(5)
        checkbox_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        checkbox_field.send_keys("country")
        checkbox_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]')
        checkbox_field.send_keys("india,pakistan")
        add_checkbox_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(6)
        text_area_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        text_area_field.send_keys("address")
        add_text_area_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(8)
        date_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        date_field.send_keys("birth date")
        add_date_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(9)
        time_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        time_field.send_keys("current time")
        add_time_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()
        time.sleep(5)

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(11)
        video_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        video_field.send_keys("python tutorial")
        video_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]')
        video_field.send_keys("https://youtu.be/WGJJIrtnfpk")
        add_video_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        select = Select(self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]'))
        select.select_by_index(12)
        link_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        link_field.send_keys("java tutorial")
        link_field = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]')
        link_field.send_keys("https://www.tutorialspoint.com/java/java_basic_syntax.htm")
        add_link_field = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.addFieldDetails();"]').click()

        # last step of create form
        create_form = self.driver.find_element_by_xpath('//*[@data-ng-click="vm.saveForm(vm.mode);"]').click()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(15)

    def output(self):
        file_data = xlrd.open_workbook("E:\Create Form UI Automation\Verification Excel.xls")
        verification_file = file_data.sheet_by_index(0)
        col_val = 1
        excel_data = []
        xlheaders = []

        for j in range(0, 10):
            xlheaders.append(verification_file.cell(0, j).value)
            excel_data.append(verification_file.cell(1, j).value)
        print(excel_data)
        # for i in range(len(xlheaders)):
        #     ws.write(0, col_val, xlheaders[i], __style2)
        ui_data = self.driver.find_elements_by_xpath('//*[@for="formname"]')
        data_ui = []
        for i in ui_data:
            data_ui.append(i.text)
            print(i.text)
        print(data_ui)
        for i in range(len(excel_data)):
            if excel_data[i] == data_ui[i]:
                self.ws.write(2, col_val, data_ui[i], self.__style1)
                print("pass")
            else:
                self.ws.write(2, col_val, data_ui[i], self.__style2)
                print("fail")
            self.ws.write(1, col_val, excel_data[i], self.__style0)
            col_val += 1
        self.ws.write(2, 0, "Pass", self.__style1)

        self.wb_result.save('E:\Create Form UI Automation\Output File\CreateFormResults(' + self.__current_DateTime + ').xls')

    def validation(self):
        try:
            if self.driver.find_element_by_name("candidate").get_attribute("type") == "text":
                print("Element is a text field")

            if self.driver.find_element_by_name("date").get_attribute("placeholder") == "Date":
                print("Element is a date field")

            if self.driver.find_element_by_xpath('[@placeholder="Time"]').get_attribute("data-time-format") == "HH:mm":
                print("Element is a time field")

            if self.driver.find_element_by_name("college").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a drop_down field")

            if self.driver.find_element_by_name("gender").get_attribute("type") == "radio":
                print("Element is a radio field")

            if self.driver.find_element_by_name("country").get_attribute("type") == "checkbox":
                print("Element is a checkbox field")

            if self.driver.find_element_by_name("address").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a textarea field")

            if self.driver.find_element_by_name("birth").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a birthdate field")

            if self.driver.find_element_by_name("current").get_attribute("data-ng-model") == "formControl.Value":
                print("Element is a current time field")

            if self.driver.find_element_by_name("python").get_attribute("type") == "text":
                print("Element is a link field")

        except Exception as e:
            print(e)


Object = AmitTesting()
Object.login()
Object.create_form()
Object.output()
Object.validation()
