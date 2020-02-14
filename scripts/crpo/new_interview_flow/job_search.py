import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import settings_On_Off


class JobSearch(settings_On_Off.Settings):
    def __init__(self):
        super(JobSearch, self).__init__()

        self.job_name_breadcumb = ''

        self.ui_new_feedback_enable = []
        self.ui_job_advance_search_n = []
        self.ui_job_getbyid_n = []

    def job_search(self):
        try:
            time.sleep(5)
            self.advance_search(page_elements.tabs['job_tab'])

            self.name_search(self.job_sprint_version_n, 'Job')

            if self.search == 'Pass':
                self.ui_job_advance_search_n = 'Pass'

            time.sleep(2)
            self.job_getby_details(self.job_sprint_version_n)

            time.sleep(3)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.job_validation('getbyid')
            if self.job_name_breadcumb == self.job_sprint_version_n:
                print('**-------->>> Job get by name is working')
                self.ui_job_getbyid_n = 'Pass'
                time.sleep(3)

        except Exception as error:
            api_logger.error(error)

    def job_validation(self, config_name):
        try:
            self.x_path_element_webdriver_wait(page_elements.job_validations['job_name_breadcumb'])
            self.job_name_breadcumb = self.xpath.text
        except Exception as e1:
            api_logger.error(e1)

        if self.job_name_breadcumb == self.job_sprint_version_n:
            print('**-------->>> Job Validated and continuing '
                  'with {} to created job :: {}'.format(config_name, self.job_name_breadcumb))
        else:
            print('Job validation failed Or Job creation failed <<<--------**')
