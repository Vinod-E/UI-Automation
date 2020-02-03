import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import interview_panel
from selenium.webdriver.common.keys import Keys


class JobTagToRequirement(interview_panel.InterviewPanel):
    def __init__(self):
        super(JobTagToRequirement, self).__init__()

        self.ui_tag_requirement_action = []
        self.ui_tag_requirement = []
        self.ui_un_tag_requirement_action = []
        self.ui_un_tag_requirement = []

    def tag_requirement(self):
        self.driver.implicitly_wait(5)
        self.job_validation('requirement tag')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.floating_action()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['tag_requirement'])
                self.xpath.click()
                self.ui_tag_requirement_action = 'Pass'

                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Requirements'))
                self.xpath.send_keys(self.xl_tag_req)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                time.sleep(3)
                self.x_path_element_webdriver_wait(page_elements.buttons['job_requirement_tag'])
                self.xpath.click()
                print('**-------->>> Job tag to requirement successfully')
                self.ui_tag_requirement = 'Pass'

            except Exception as error:
                api_logger.error(error)

    def un_tag_requirement(self):
        self.driver.implicitly_wait(5)
        self.job_validation('requirement un-tag')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.driver.refresh()
                time.sleep(5)
                self.floating_action()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['un-tag_requirement'])
                self.xpath.click()
                self.ui_un_tag_requirement_action = 'Pass'

                self.x_path_element_webdriver_wait(page_elements.buttons['ok'])
                self.xpath.click()
                time.sleep(5)
                print('**-------->>> Job un-tag to requirement successfully')
                self.ui_un_tag_requirement = 'Pass'

            except Exception as error:
                api_logger.error(error)


# ob = JobTagToRequirement()
# ob.tag_requirement()
# ob.un_tag_requirement()
