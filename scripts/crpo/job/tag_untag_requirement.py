import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.job import interview_panel
from scripts.crpo.common import button_click


class JobTagToRequirement(interview_panel.InterviewPanel):
    def __init__(self):
        super(JobTagToRequirement, self).__init__()

        self.ui_tag_requirement_action = []
        self.ui_tag_requirement = []
        self.ui_un_tag_requirement_action = []
        self.ui_un_tag_requirement = []

    def tag_requirement(self):
        self.getby_details_screen(self.job_name_sprint_version)
        self.driver.refresh()
        time.sleep(2)
        if self.header_name.strip() == self.job_name_sprint_version:
            print('**-------->>> Tagging requirement to job:: {}'.format(self.job_name_sprint_version))
            try:
                self.actions_dropdown()
                self.floating_action('tag_requirement')
                self.ui_tag_requirement_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Requirements'),
                                                 self.xl_tag_req)
                self.drop_down_selection()
                button_click.button(self, 'Tag')
                print('**-------->>> Job tag to requirement successfully')
                self.ui_tag_requirement = 'Pass'

            except Exception as error:
                ui_logger.error(error)

    def un_tag_requirement(self):
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name.strip() == self.job_name_sprint_version:
            print('**-------->>> Un-Tagging requirement to job:: {}'.format(self.job_name_sprint_version))
            try:
                self.driver.refresh()
                time.sleep(2)
                self.actions_dropdown()
                self.floating_action('un-tag_requirement')
                self.ui_un_tag_requirement_action = 'Pass'

                button_click.all_buttons(self, 'OK')
                print('**-------->>> Job un-tag to requirement successfully')
                self.ui_un_tag_requirement = 'Pass'

            except Exception as error:
                ui_logger.error(error)
