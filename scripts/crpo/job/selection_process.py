import time
import page_elements
from scripts.crpo.job import create_job
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys


class SelectionProcess(create_job.CreateJob):
    def __init__(self):
        super(SelectionProcess, self).__init__()

        self.ui_job_floating_action = []
        self.selection_process_created = []
        self.ui_selection_process_action = []

    def config_selection_process(self):
        # ---------------------------------- From Job details screen ---------------------------------------------------
        self.job_validation('selection process')
        if self.job_name_breadcumb == self.job_name_sprint_version:

            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.floating_action()
                self.ui_job_floating_action = 'Pass'

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['selection_process'])
                self.xpath.click()
                self.ui_selection_process_action = 'Pass'

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Selection Process"))
                self.xpath.send_keys(self.xl_selection_process)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                try:
                    time.sleep(3)
                    self.driver.execute_script("window.scrollTo(0,100);")
                    self.x_path_element_webdriver_wait(page_elements.buttons['sp-save'])
                    self.xpath.click()

                    self.selection_process_created = 'Pass'

                except Exception as save:
                    api_logger.error(save)
            except Exception as config_message:
                api_logger.error(config_message)

        if self.selection_process_created == 'Pass':
            print('**-------->>> Selection Process configured successfully')
        else:
            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.floating_action()
                self.ui_job_floating_action = 'Pass'

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['selection_process'])
                self.xpath.click()
                self.ui_job_floating_action = 'Pass'

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Selection Process"))
                self.xpath.send_keys(self.xl_selection_process)
                self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

                try:
                    time.sleep(3)
                    self.driver.execute_script("window.scrollTo(0,100);")
                    self.x_path_element_webdriver_wait(page_elements.buttons['sp-save'])
                    self.xpath.click()

                    self.selection_process_created = 'Pass'

                except Exception as save:
                    api_logger.error(save)
            except Exception as config_message:
                api_logger.error(config_message)


# ob = SelectionProcess()
# ob.config_selection_process()
