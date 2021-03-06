import time
import page_elements
from scripts.crpo.job import create_job
from logger_settings import ui_logger
from scripts.crpo.common import button_click


class SelectionProcess(create_job.CreateJob):
    def __init__(self):
        super(SelectionProcess, self).__init__()

        self.ui_job_floating_action = ''
        self.selection_process_created = ''
        self.ui_selection_process_action = ''

    def config_selection_process(self):
        # ---------------------------------- From Job details screen ---------------------------------------------------
        self.getby_details_screen(self.job_name_sprint_version)
        if self.header_name == self.job_name_sprint_version:
            print('**-------->>> Selection process configuring to job:: {}'.format(self.job_name_sprint_version))
            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                time.sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,-200);")
                self.actions_dropdown()
                self.floating_action('selection_process')
                self.ui_job_floating_action = 'Pass'
                self.ui_selection_process_action = 'Pass'

                time.sleep(2)
                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Selection Process"),
                                                 self.xl_selection_process)
                self.drop_down_selection()

                time.sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,200);")
                button_click.button(self, 'Save')
                self.dismiss_message()

                self.selection_process_created = 'Pass'

            except Exception as config_message:
                ui_logger.error(config_message)

        if self.selection_process_created == 'Pass':
            print('**-------->>> Selection Process configured successfully')
        else:
            try:
                # ------------------------------------ Selection Process -----------------------------------------------
                self.driver.refresh()
                self.driver.implicitly_wait(3)
                self.actions_dropdown()
                self.floating_action('selection_process')
                self.ui_job_floating_action = 'Pass'
                self.ui_selection_process_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Selection Process"),
                                                 self.xl_selection_process)
                self.drop_down_selection()

                time.sleep(1)
                self.driver.execute_script("window.scrollTo(0,100);")
                button_click.button(self, 'Save')
                self.dismiss_message()

            except Exception as config_message:
                ui_logger.error(config_message)
