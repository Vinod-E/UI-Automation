import time
import page_elements
import image_capture
from logger_settings import ui_logger
from scripts.crpo.job import tag_untag_requirement
from scripts.crpo.common import button_click


class EditJobRole(tag_untag_requirement.JobTagToRequirement):
    def __init__(self):
        super(EditJobRole, self).__init__()

        self.ui_update_job = []
        self.ui_job_getbyid = []
        self.ui_job_advance_search = []
        self.ui_job_edit_action = []

    def edit_job(self):
        self.driver.execute_script("window.scrollTo(0,-200);")
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name.strip() == self.job_name_sprint_version:
            print('**-------->>> Edit job functionality to job:: {}'.format(self.job_name_sprint_version))

            try:
                self.actions_dropdown()
                time.sleep(0.5)
                self.floating_action('job_edit')
                self.ui_job_edit_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.job['description_box'], self.j_description_u)
                time.sleep(2)
                button_click.button(self, 'Update')

                image_capture.screen_shot(self, 'Update_Job')

                # ------------------------ Validation ------------------------------------------------------------------
                self.job_search_flow()
                if self.header_name.strip() == self.job_name_sprint_version:
                    print('**-------->>> Job Edit/update successfully')
                    self.ui_update_job = 'Pass'

            except Exception as error:
                ui_logger.error(error)

    def job_search_flow(self):
        try:
            time.sleep(0.4)
            self.advance_search(page_elements.tabs['job_tab'])
            self.name_search(self.job_name_sprint_version, 'Job')
            if self.search == 'Pass':
                self.ui_job_advance_search = 'Pass'

            self.job_getby_name(self.job_name_sprint_version)

            time.sleep(0.5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.getby_details_screen(self.job_name_sprint_version)
            if self.header_name.strip() == self.job_name_sprint_version:
                print('**-------->>> Job get by name is working')
                self.ui_job_getbyid = 'Pass'

        except Exception as error:
            ui_logger.error(error)
