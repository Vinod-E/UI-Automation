import time
import config
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import tag_untag_requirement


class EditJobRole(tag_untag_requirement.JobTagToRequirement):
    def __init__(self):
        super(EditJobRole, self).__init__()

        self.ui_update_job = []
        self.ui_job_getbyid = []
        self.ui_job_advance_search = []
        self.ui_job_edit_action = []

    def edit_job(self):

        self.driver.implicitly_wait(5)
        self.job_validation('edit action')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                self.floating_action()

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['job_edit'])
                self.xpath.click()
                self.ui_job_edit_action = 'Pass'

                time.sleep(3)
                self.x_path_element_webdriver_wait(page_elements.job['description_box'])
                self.xpath.send_keys(self.j_description_u)

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.buttons['update'])
                self.xpath.click()

                time.sleep(3)
                self.driver.save_screenshot(config.image_config['screen_shot'].format('Update_Job'))

                # ------------------------ Validation ------------------------------------------------------------------
                self.job_search()
                if self.job_name_breadcumb == self.job_name_sprint_version:
                    print('**-------->>> Job Edit/update successfully')
                    self.ui_update_job = 'Pass'

            except Exception as error:
                api_logger.error(error)

    def job_search(self):
        try:
            self.advance_search(page_elements.tabs['job_tab'])

            self.name_search(self.job_name_sprint_version, 'Job')

            if self.search == 'Pass':
                self.ui_job_advance_search = 'Pass'

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.job['job_getbyid'].format(self.job_name_sprint_version))
            self.xpath.click()

            time.sleep(3)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.job_validation('getbyid')
            if self.job_name_breadcumb == self.job_name_sprint_version:
                print('**-------->>> Job get by name is working')
                self.ui_job_getbyid = 'Pass'
                time.sleep(3)

        except Exception as error:
            api_logger.error(error)


# ob = EditJobRole()
# ob.edit_job()
