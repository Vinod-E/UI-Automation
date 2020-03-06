import time
import config
import page_elements
import image_capture
from logger_settings import api_logger
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
            time.sleep(2)
            self.requirement_tab()

            self.web_element_click_xpath(page_elements.buttons['create'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name"),
                                             self.requirement_sprint_version)

            self.web_element_click_xpath(page_elements.requirement['job_selection_field'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.job_sprint_version)

            self.web_element_click_xpath(page_elements.requirement['particular_job_select'])

            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Hiring Type"),
                                             self.xl_hiring_track)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("College Type"),
                                             self.xl_college_type)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.buttons['requirement_create'])

            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,-100);")
            image_capture.screen_shot(self, 'Requirement_created')

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
            self.web_element_text_xpath(page_elements.requirement_validations['requirement_name_breadcumb'])
            self.req_name_breadcumb = self.text_value
        except Exception as e1:
            api_logger.error(e1)

        if self.req_name_breadcumb == self.requirement_sprint_version:
            self.ui_requirement_validation = 'Pass'
            print('**-------->>> Req Validated and continuing '
                  'with {} to created requirement :: {}'.format(config_name, self.req_name_breadcumb))
        else:
            print('Req validation failed Or Req creation failed <<<--------**')
