import time
import config
import page_elements
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.requirement import requirement_excel


class CreateRequirement(requirement_excel.RequirementExcelRead):
    def __init__(self):
        super(CreateRequirement, self).__init__()

        self.ui_create_requirement = []
        self.ui_requirement_validation = []
        self.req_name_breadcumb = ""

    def create_requirement(self):

        try:

            self.driver.refresh()
            time.sleep(4)
            self.requirement_tab()

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.buttons['create'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Name"))
            self.xpath.send_keys(self.requirement_sprint_version)

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.requirement['job_selection_field'])
            self.xpath.click()

            time.sleep(1.5)
            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Search"))
            self.xpath.send_keys(self.job_sprint_version)

            self.x_path_element_webdriver_wait(page_elements.requirement['particular_job_select'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Hiring Type"))
            self.xpath.send_keys(self.xl_hiring_track)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("College Type"))
            self.xpath.send_keys(self.xl_college_type)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.buttons['requirement_create'])
            self.xpath.click()

            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.driver.save_screenshot(config.image_config['screen_shot'].format('Requirement_created'))

            # -------------------------------- Validation --------------------------------------------------------------
            self.requirement_validation('the requirement')
            if self.req_name_breadcumb == self.requirement_sprint_version:
                print('**-------->>> Requirement created successfully ')
                self.ui_create_requirement = 'Pass'
            else:
                print('Failed to create Requirement <<<--------**')

        except Exception as create_req:
            api_logger.error(create_req)

    def requirement_validation(self, config_name):

        try:
            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.requirement_validations['requirement_name_breadcumb'])
            self.req_name_breadcumb = self.xpath.text
        except Exception as e1:
            api_logger.error(e1)

        if self.req_name_breadcumb == self.requirement_sprint_version:
            self.ui_requirement_validation = 'Pass'
            print('**-------->>> Req Validated and continuing '
                  'with {} to created requirement :: {}'.format(config_name, self.req_name_breadcumb))
        else:
            print('Req validation failed Or Req creation failed <<<--------**')


# ob = CreateRequirement()
# ob.create_requirement()
