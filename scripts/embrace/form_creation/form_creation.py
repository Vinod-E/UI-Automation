import time
from logger_settings import ui_logger
import xlrd
from scripts.embrace.form_creation import create_form_excel


class FormCreation(create_form_excel.FormExcelRead):
    def __init__(self):
        super(FormCreation, self).__init__()

    def add_group(self, group_name):
        try:
            self.web_element_click_xpath('//*[@data-title="Add Group"]')
            time.sleep(1)
            self.web_element_send_keys_xpath('//*[@ng-model="vm.groupName"]', group_name)
            time.sleep(0.5)
            self.web_element_click_xpath('//*[@ng-click="vm.addGroupName();$hide()"]')
        except Exception as error:
            ui_logger.error(error)

    def create_form(self):
        self.web_element_click_xpath('//*[@ui-sref="pofu.activity.forms.info"]')
        self.web_element_click_xpath('//*[@ng-if="vm.isAdmin"]')

        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.formType.Name"]', self.sprint_version)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.formType.Title"]', self.sprint_version)
        self.web_element_click_xpath('//*[@data-ng-click="vm.goToNextTab();"]')
        self.add_group(self.xl_group_one)
        self.add_group(self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.FormControl"]')

        self.web_element_send_keys_id("cmbFieldType", 'Text')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]',
                                         self.xl_candidate_name_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_one)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'DateTime')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_date_time_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'DropDown')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_college_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.CatalogMasterName"]', 'Locations')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_one)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Radio')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_gender_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', 'male,female')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'CheckBox')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_country_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', "india,pakistan")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_one)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'TextArea')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_address_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Date')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_birth_date_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_one)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Time')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]',self.xl_current_time_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Video')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_python_tutorial_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]', "https://youtu.be/WGJJIrtnfpk")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_one)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Link')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]', self.xl_java_tutorial_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupBoxValuesText"]',
                                         "https://www.tutorialspoint.com/java/java_basic_syntax.htm")
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        self.web_element_send_keys_id("cmbFieldType", 'Attachment')
        time.sleep(5)
        # self.web_element_send_keys_id("button", 'image')
        self.web_element_click_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/div[1]/span/button")
        self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/form/div[3]/div/div[1]/span/div/'
                                     'div[2]/div[1]')
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]')
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.ControlLabel"]',
                                         self.resume_label)
        self.web_element_send_keys_xpath('//*[@data-ng-model="vm.fieldDetails.GroupName"]', self.xl_group_two)
        self.web_element_click_xpath('//*[@data-ng-model="vm.fieldDetails.IsMandatory"]')
        self.web_element_click_xpath('//*[@data-ng-click="vm.addFieldDetails();"]')

        # last step of create form
        self.web_element_click_xpath('//*[@data-ng-click="vm.saveForm(vm.mode);"]')
        time.sleep(2)
        self.driver.refresh()
        time.sleep(15)
