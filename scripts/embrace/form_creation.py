import time
import common_login
from datetime import datetime
import xlwt
import xlrd


class AmitTesting(common_login.CommonLogin):
    def __init__(self):
        super(AmitTesting, self).__init__()
        self.embrace_login()

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

    def create_form(self):
        self.web_element_click_xpath('//*[@ui-sref="pofu.activity.forms.info"]')
        self.web_element_click_xpath('//*[@ng-if="vm.isAdmin"]')

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

        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.formType.Title"]', final_name)
        self.web_element_click_xpath('//*[@data-ng-click="vm.goToNextTab();"]')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]')

        self.web_element_send_keys_id("cmbFieldType", 'Text')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "candidate name")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'DateTime')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "date and time")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'DropDown')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "College")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.CatalogMasterName"]', 'Colleges')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Radio')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "gender")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', 'male,female')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'CheckBox')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "country")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', "india,pakistan")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'TextArea')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "address")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Date')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "birth date")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Time')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "current time")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Video')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "python tutorial")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', "https://youtu.be/WGJJIrtnfpk")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Link')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', "java tutorial")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]',
                                         "https://www.tutorialspoint.com/java/java_basic_syntax.htm")
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        # last step of create form
        self.web_element_click_xpath('//*[@data-ng-click="vm.saveForm(vm.mode);"]')
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
                print("Element is a date time field")

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
                print("Element is a video field")

            if self.driver.find_element_by_xpath('//*[@ng-href="https://www.tutorialspoint.com'
                                                 '/java/java_basic_syntax.htm"]').get_attribute('href') == 'https://www.tutorialspoint.com/java/java_basic_syntax.htm':

                print('Element is a link field')

        except Exception as e:
            print(e)


Object = AmitTesting()
Object.create_form()
Object.output()
Object.validation()
