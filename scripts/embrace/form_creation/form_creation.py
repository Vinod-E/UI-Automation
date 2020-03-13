import time
import common_login
import datetime
import xlrd


class FormCreation(common_login.CommonLogin):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(FormCreation, self).__init__()
        self.embrace_login()


    def create_form(self):
        self.web_element_click_xpath('//*[@ui-sref="pofu.activity.forms.info"]')
        self.web_element_click_xpath('//*[@ng-if="vm.isAdmin"]')

        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.formType.Name"]', self.sprint_version)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.formType.Title"]', self.sprint_version)
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
