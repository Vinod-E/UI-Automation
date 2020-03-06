import time
import page_elements
import image_capture
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.job import job_excel


class CreateJob(job_excel.JobExcelRead):
    def __init__(self):
        super(CreateJob, self).__init__()

        self.job_file = test_data_inputpath.attachments['attachment']
        self.job_name_breadcumb = ""
        self.ui_job_created = []
        self.ui_job_validation = []

    def create_job_role(self):
        try:
            self.job_tab()
            time.sleep(2)
            self.web_element_click_xpath(page_elements.buttons['create'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name"),
                                             self.job_name_sprint_version)
            self.web_element_send_keys_xpath(page_elements.file['upload_file'],
                                             self.job_file)
            self.web_element_send_keys_xpath(page_elements.job['description_box'],
                                             self.xl_job_desc)
            self.web_element_send_keys_xpath(page_elements.job['location'],
                                             self.xl_job_loc)
            self.drop_down_selection()
            self.web_element_send_keys_xpath(page_elements.job['hiring_manager'],
                                             self.xl_job_hm)
            self.drop_down_selection()
            self.web_element_send_keys_xpath(page_elements.job['business_unit'],
                                             self.xl_job_bu)
            self.drop_down_selection()

            self.driver.find_element_by_name(page_elements.job['openings']).clear()
            self.web_element_send_keys_name(page_elements.job['openings'],
                                            self.xl_openings)
            self.web_element_send_keys_name(page_elements.job['max_applicant'],
                                            self.xl_openings)

            self.driver.find_element_by_xpath(page_elements.job['male_diversity']).clear()
            self.web_element_send_keys_xpath(page_elements.job['male_diversity'],
                                             self.xl_male_diversity)

            self.driver.find_element_by_xpath(page_elements.job['female_diversity']).clear()
            self.web_element_send_keys_xpath(page_elements.job['female_diversity'],
                                             self.xl_female_diversity)

            self.web_element_click_xpath(page_elements.buttons['create-save'])

            self.dismiss_message()
            self.driver.execute_script("window.scrollTo(0,-200);")
            time.sleep(3)

        except Exception as create_job:
            api_logger.error(create_job)
            image_capture.screen_shot(self, 'Job')

        self.job_validation('the job')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            self.ui_job_created = 'Pass'
            print('**-------->>> Job Created successfully')
        else:
            print('**-------->>> Job Created Failed')

    def job_validation(self, config_name):
        try:
            self.web_element_text_xpath(page_elements.job_validations['job_name_breadcumb'])
            self.job_name_breadcumb = self.text_value
        except Exception as e1:
            api_logger.error(e1)

        if self.job_name_breadcumb == self.job_name_sprint_version:
            image_capture.screen_shot(self, 'Job_created')
            self.ui_job_validation = 'Pass'
            print('**-------->>> Job Validated and continuing '
                  'with {} to created job :: {}'.format(config_name, self.job_name_breadcumb))
        else:
            print('Job validation failed Or Job creation failed <<<--------**')