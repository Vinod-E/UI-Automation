import time
import config
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.job import job_excel
from selenium.webdriver.common.keys import Keys


class CreateJob(job_excel.JobExcelRead):
    def __init__(self):
        super(CreateJob, self).__init__()

        self.job_file = test_data_inputpath.attachments['attachment']
        self.job_name_breadcumb = ""
        self.ui_job_created = []
        self.ui_job_validation = []

    def create_job_role(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['job_tab'])
            self.xpath.click()

            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.buttons['create'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Name"))
            self.xpath.send_keys(self.job_name_sprint_version)

            time.sleep(2.4)
            self.driver.find_element_by_xpath(page_elements.file['upload_file']).send_keys(self.job_file)

            self.x_path_element_webdriver_wait(page_elements.job['description_box'])
            self.xpath.send_keys(self.xl_job_desc)

            self.x_path_element_webdriver_wait(page_elements.job['location'])
            self.xpath.send_keys(self.xl_job_loc)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.job['hiring_manager'])
            self.xpath.send_keys(self.xl_job_hm)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.job['business_unit'])
            self.xpath.send_keys(self.xl_job_bu)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            time.sleep(2)
            self.name_element_webdriver_wait(page_elements.job['openings'])
            self.name.clear()
            self.name.send_keys(self.xl_openings)

            self.name_element_webdriver_wait(page_elements.job['max_applicant'])
            self.name.send_keys(self.xl_openings)

            self.x_path_element_webdriver_wait(page_elements.job['male_diversity'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_male_diversity)

            self.x_path_element_webdriver_wait(page_elements.job['female_diversity'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_female_diversity)

            self.x_path_element_webdriver_wait(page_elements.buttons['create-save'])
            self.xpath.click()

            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.driver.save_screenshot(config.image_config['screen_shot'].format('Job_created'))

        except Exception as create_job:
            api_logger.error(create_job)
            self.driver.save_screenshot(config.image_config['screen_shot'].format('Job'))

        self.job_validation('the job')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            self.ui_job_created = 'Pass'
            print('**-------->>> Job Created successfully')
        else:
            print('**-------->>> Job Created Failed')

        # ----------------------------------- duplicate job name case --------------------------------------------------
        # duplicate_job = self.driver.find_element_by_xpath('duplicate_job')
        # if duplicate_job.text == 'Requisition name already exists':
        #     self.driver.refresh()
        #     self.create_job_role()

        # ---------------------------- Checking whether the job created or not -----------------------------------------
        #     if self.driver.find_element_by_xpath(page_elements.job['jobrole_breadcrumbs']).is_displayed():

    def job_validation(self, config_name):
        try:
            self.x_path_element_webdriver_wait(page_elements.job_validations['job_name_breadcumb'])
            self.job_name_breadcumb = self.xpath.text
        except Exception as e1:
            api_logger.error(e1)

        if self.job_name_breadcumb == self.job_name_sprint_version:
            self.ui_job_validation = 'Pass'
            print('**-------->>> Job Validated and continuing '
                  'with {} to created job :: {}'.format(config_name, self.job_name_breadcumb))
        else:
            print('Job validation failed Or Job creation failed <<<--------**')


# ob = CreateJob()
# ob.create_job_role()
