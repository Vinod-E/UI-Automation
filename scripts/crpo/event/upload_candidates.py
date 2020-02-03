import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from scripts.crpo.event import owners_config


class EventUploadCandidates(owners_config.EventOwnersConfig):
    def __init__(self):
        super(EventUploadCandidates, self).__init__()

        self.ui_event_floating_action = []
        self.ui_event_upload_candidate_action = []
        self.ui_event_upload_candidate = []

        self.file = test_data_inputpath.attachments['upload_candidates']

    def upload_candidates_to_event(self, email_id):
        self.event_validation('upload candidates')
        if self.validation_check == 'True':

            try:
                self.floating_action()
                self.ui_event_floating_action = 'Pass'

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.floating_actions['event_upload_candidates'])
                self.xpath.click()
                self.ui_event_upload_candidate_action = 'Pass'

                upload_file = self.driver.find_element_by_xpath(page_elements.file['event_upload_file'])
                upload_file.send_keys(self.file)

                time.sleep(5)
                self.x_path_element_webdriver_wait(page_elements.event_config['Next_Button'])
                self.xpath.click()

                self.x_path_element_webdriver_wait(page_elements.event_config['declare_checkbox'])
                self.xpath.click()

                self.driver.execute_script("window.scrollTo(0,100);")
                self.x_path_element_webdriver_wait(page_elements.event_config['signature'])
                self.xpath.send_keys('AutomationVS')

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.event_config['Agree'])
                self.xpath.click()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.event_config['edit_candidate_details'])
                self.xpath.click()

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.event_config['upload_candidate_name'])
                self.xpath.clear()
                self.xpath.send_keys(self.event_sprint_version)

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.event_config['upload_candidate_email'])
                self.xpath.clear()
                self.xpath.send_keys(email_id)

                time.sleep(1)
                self.x_path_element_webdriver_wait(page_elements.event_config['upload_candidate_usn'])
                self.xpath.clear()
                self.xpath.send_keys(self.event_sprint_version)

                self.x_path_element_webdriver_wait(page_elements.event_config['details_save'])
                self.xpath.click()

                time.sleep(2)
                self.x_path_element_webdriver_wait(page_elements.buttons['event_upload_candidate_save'])
                self.xpath.click()

# -------- Validation check
                self.upload_candidate_validation()

            except Exception as error:
                api_logger.error(error)

    def upload_candidate_validation(self):
        try:
            time.sleep(2.9)
            self.x_path_element_webdriver_wait(page_elements.event_config['upload_candidate_count'])

            if self.xpath.text == 'Uploaded 1':
                self.ui_event_upload_candidate = 'Pass'
                print('**-------->>> Candidate uploaded to event successfully')
            else:
                print('Failed to upload candidate to event <<<--------**')

            self.driver.find_element_by_xpath(page_elements.event_config['close_pop_details_window']).click()
            self.driver.refresh()
            time.sleep(3.5)

        except Exception as error:
            api_logger.error(error)
