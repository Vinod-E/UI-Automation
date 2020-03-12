import time
import page_elements
from scripts.crpo.job import create_job
from logger_settings import api_logger


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

                self.web_element_click_xpath(page_elements.floating_actions['selection_process'])
                self.ui_selection_process_action = 'Pass'

                time.sleep(2)
                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Selection Process"),
                                                 self.xl_selection_process)
                self.drop_down_selection()

                time.sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,200);")
                self.web_element_click_xpath(page_elements.buttons['sp-save'])

                self.selection_process_created = 'Pass'

            except Exception as config_message:
                api_logger.error(config_message)

        if self.selection_process_created == 'Pass':
            print('**-------->>> Selection Process configured successfully')
        else:
            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.driver.refresh()
                self.driver.implicitly_wait(3)
                self.floating_action()
                self.ui_job_floating_action = 'Pass'

                self.web_element_click_xpath(page_elements.floating_actions['selection_process'])
                self.ui_selection_process_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Selection Process"),
                                                 self.xl_selection_process)
                self.drop_down_selection()

                time.sleep(1)
                self.driver.execute_script("window.scrollTo(0,100);")
                self.web_element_click_xpath(page_elements.buttons['sp-save'])
            except Exception as config_message:
                api_logger.error(config_message)
