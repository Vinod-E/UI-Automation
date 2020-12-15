from selenium import webdriver
import time
from logger_settings import ui_logger
from scripts.embrace.form_creation import checkbox_validations



class screening_rule_input(checkbox_validations.CheckboxValidations):
    def __init__(self):
        super(screening_rule_input,self).__init__()


    def screening_rule_creation(self):
        try:
            self.web_element_click_xpath('//*[@ng-if="vm.config.Manage.Form.Tab"]')
            self.web_element_click_xpath('/html/body/div[2]/div/section/div/div/div/div/div/div/div'
                '[2]/div[1]/div[3]/div/div[2]/div/div/a[6]')
            self.web_element_click_xpath('//*[@data-ng-click="vm.showValidationModal();"]')
            self.web_element_send_keys_xpath('//*[@data-ng-model="vm.validationInfo.Title"]', 'new rule')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]/div'
                '[1]/div/div/span[3]')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]'
                                                          '/div[2]/div[1]/select', 'Equal')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]'
                                                          '/div[2]/div[2]/div/input', 'amit')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[3]/div[1]'
                                                   '/div/div/span[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div'
                '/select/option[1]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[4]/div[1]'
                                                  '/div/div/span[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[4]/div[2]'
                                                  '/div/select/option[1]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]/div[1]'
                                                   '/div/div/span[3]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]/div[2]'
                                                   '/div/select/option[1]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[1]'
                                                   '/div/div/span[2]')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]'
                                                   '/div[1]/select', 'Equal')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]'
                                                   '/div[2]/div/input', 'bangalore')
            self.web_element_click_xpath('//*[@data-ng-click="vm.saveValidationRule(vm.mode);"]')
            time.sleep(1)

            #second rule creation
            self.web_element_click_xpath('//*[@data-ng-click="vm.showValidationModal();"]')
            self.web_element_send_keys_xpath('//*[@data-ng-model="vm.validationInfo.Title"]', 'rule number 2')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]/div'
                '[1]/div/div/span[3]')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]'
                                                          '/div[2]/div[1]/select', 'Equal')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[1]'
                                                          '/div[2]/div[2]/div/input', 'vikas')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[3]/div[1]'
                                                   '/div/div/span[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[3]/div[2]/div'
                '/select/option[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[4]/div[1]'
                                                  '/div/div/span[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[4]/div[2]/div/'
                'select/option[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]/div[1]'
                                                   '/div/div/span[3]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]/div[2]'
                                                   '/div/select/option[2]')
            self.web_element_click_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[1]'
                                                   '/div/div/span[2]')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]'
                                                   '/div[1]/select', 'Equal')
            self.web_element_send_keys_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]/div[2]'
                                                   '/div[2]/div/input', 'mumbai')
            self.web_element_click_xpath('//*[@data-ng-click="vm.saveValidationRule(vm.mode);"]')

        except Exception as error:
            ui_logger.error(error)

    def screening_rule_verification(self):
            # opening rule number 1
            time.sleep(2)
            self.web_element_click_xpath('//*[@id="req-list-view"]/tr/td[4]/span[1]/a')
            self.title = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.validationInfo.Title"]').get_attribute('value')
            print(self.title)

            candidate_name_rule_1_verification = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]'
                '/div/form/div[1]/div[2]/div[1]/select/option[2]')

            self.candidate_n_r = candidate_name_rule_1_verification.get_attribute('label')
            print(self.candidate_n_r)


            candidate_name_verification = self.driver.find_element_by_xpath(
                '//*[@data-ng-model="vm.validationRules[formControl.Id].Rule"]')

            self.candidate_name = candidate_name_verification.get_attribute('value')
            print(self.candidate_name)


            college_verification = self.driver.find_element_by_xpath('//*[@data-ng-if="formControl.FormControl === 2 && '
                                                                'formControl.CatalogMasterName !== null"]')

            college = college_verification.get_attribute('value')
            print(college)
            college_v = college.replace('string:', '')
            self.college_v = college_v.strip()
            print(self.college_v)


            gender_verification = self.driver.find_element_by_xpath('//*[@data-ng-if="formControl.FormControl === 3 ||'
                                                               ' formControl.FormControl === 4"]')

            gender = gender_verification.get_attribute('value')
            print(gender)
            gender_v = gender.replace('string:', '')
            self.gender_v = gender_v.strip()
            print(self.gender_v)


            country_verification = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]'
                '/div[2]/div/select')

            country = country_verification.get_attribute('value')
            print(country)
            country_v = country.replace('string:', '')
            self.country_v = country_v.strip()
            print(self.country_v)


            address_rule_verification = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form'
                '/div[6]/div[2]/div[1]/select/option[2]')

            self.address_rule = address_rule_verification.get_attribute('label')
            print(self.address_rule)


            address_verication = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]'
                '/div[2]/div[2]/div/input')

            self.address = address_verication.get_attribute('value')
            print(self.address)


            self.web_element_click_xpath('//*[@ng-click="$hide()"]')
            time.sleep(2)


            # opening rule number 2
            self.web_element_click_xpath('//*[@id="req-list-view"]/tr[2]/td[4]/span[1]/a')
            time.sleep(2)

            title_verification_2 = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.validationInfo.Title"]')
            self.title_2 = title_verification_2.get_attribute('value')
            print(self.title_2)

            candidate_name_rule_2_verification = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]'
                '/div/form/div[1]/div[2]/div[1]/select/option[2]')

            self.candidate_n_r_2 = candidate_name_rule_2_verification.get_attribute('label')
            print(self.candidate_n_r_2)


            candidate_name_verification_2 = self.driver.find_element_by_xpath('//*[@data-ng-model="vm.validationRules'
                                                                         '[formControl.Id].Rule"]')

            self.candidate_name_2 = candidate_name_verification_2.get_attribute('value')
            print(self.candidate_name_2)


            college_verification_2 = self.driver.find_element_by_xpath('//*[@data-ng-if="formControl.FormControl === 2 && '
                                                                  'formControl.CatalogMasterName !== null"]')
            college_2 = college_verification_2.get_attribute('value')
            print(college_2)
            college_v_2 = college_2.replace('string:', '')
            self.college_v_2 = college_v_2.strip()
            print(self.college_v_2)

            gender_verification_2 = self.driver.find_element_by_xpath('//*[@data-ng-if="formControl.FormControl === 3 ||'
                                                                 ' formControl.FormControl === 4"]')
            gender_2 = gender_verification_2.get_attribute('value')
            print(gender_2)
            gender_v_2 = gender_2.replace('string:', '')
            self.gender_v_2 = gender_v_2.strip()
            print(self.gender_v_2)

            country_verification_2 = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[5]'
                '/div[2]/div/select')
            country_2 = country_verification_2.get_attribute('value')
            print(country_2)
            country_v_2 = country_2.replace('string:', '')
            self.country_v_2 = country_v_2.strip()
            print(self.country_v_2)

            address_rule_verification_2 = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form'
                '/div[6]/div[2]/div[1]/select/option[2]')
            self.address_rule_2 = address_rule_verification_2.get_attribute('label')
            print(self.address_rule_2)

            address_verication_2 = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/div/div[2]/div/form/div[6]'
                '/div[2]/div[2]/div/input')
            self.address_2 = address_verication_2.get_attribute('value')
            print(self.address_2)

            self.web_element_click_xpath('//*[@ng-click="$hide()"]')
            time.sleep(2)
