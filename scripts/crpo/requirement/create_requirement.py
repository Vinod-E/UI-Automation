import time
import page_elements
import image_capture
from logger_settings import ui_logger
from scripts.crpo.requirement import requirement_excel
from scripts.crpo.common import button_click


class CreateRequirement(requirement_excel.RequirementExcelRead):
    def __init__(self):
        super(CreateRequirement, self).__init__()

        self.ui_create_requirement = ''
        self.ui_requirement_validation = ''
        self.req_name_breadcumb = ""

    def create_requirement(self):
        try:
            self.driver.refresh()
            time.sleep(2)
            self.requirement_tab()

            self.web_element_click_xpath(page_elements.buttons['create'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name"),
                                             self.requirement_sprint_version)
            time.sleep(0.2)
            self.web_element_click_xpath(page_elements.requirement['job_selection_field'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.job_sprint_version)

            time.sleep(2)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])

            button_click.all_buttons(self, 'Done')

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Hiring Type"),
                                             self.xl_hiring_track)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("College Type"),
                                             self.xl_college_type)
            self.drop_down_selection()

            button_click.button(self, ' Create')

            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,-100);")
            image_capture.screen_shot(self, 'Requirement_created')

            # -------------------------------- Validation --------------------------------------------------------------
            self.getby_details_screen(self.requirement_sprint_version)
            if self.header_name.strip() == self.requirement_sprint_version:
                print('**-------->>> Requirement created successfully ')
                print('**-------->>> Req Validated and continuing '
                      'with the created requirement :: {}'.format(self.requirement_sprint_version))
                self.ui_create_requirement = 'Pass'
                self.ui_requirement_validation = 'Pass'
            else:
                print('Failed to create Requirement <<<--------**')

        except Exception as create_req:
            ui_logger.error(create_req)
