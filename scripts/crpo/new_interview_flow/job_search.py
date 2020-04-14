import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.new_interview_flow import settings_On_Off


class JobSearch(settings_On_Off.Settings):
    def __init__(self):
        super(JobSearch, self).__init__()

        self.job_name_breadcumb = ''

        self.ui_job_tab = []
        self.ui_job_advance_search_n = []
        self.ui_job_getbyid_n = []
        self.ui_job_validation_n = []

    def job_search_new(self):
        try:
            time.sleep(2)
            self.advance_search(page_elements.tabs['job_tab'])

            self.name_search(self.job_sprint_version_n, 'Job')

            if self.search == 'Pass':
                self.ui_job_advance_search_n = 'Pass'

            time.sleep(0.5)
            self.job_getby_details(self.job_sprint_version_n)

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.job_validation('getbyid')
            if self.job_name_breadcumb == self.job_sprint_version_n:
                print('**-------->>> Job get by name is working')
                self.ui_job_tab = 'Pass'
                self.ui_job_getbyid_n = 'Pass'
                self.ui_job_validation_n = 'Pass'
                time.sleep(3)

        except Exception as error:
            ui_logger.error(error)

    def job_validation(self, config_name):
        try:
            self.web_element_text_xpath(page_elements.job_validations['job_name_breadcumb'])
            self.job_name_breadcumb = self.text_value
        except Exception as e1:
            ui_logger.error(e1)

        if self.job_name_breadcumb == self.job_sprint_version_n:
            print('**-------->>> Job Validated and continuing '
                  'with {} to created job :: {}'.format(config_name, self.job_name_breadcumb))
        else:
            print('Job validation failed Or Job creation failed <<<--------**')
