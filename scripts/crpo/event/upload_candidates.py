import time
import page_elements
import test_data_inputpath
from logger_settings import ui_logger
from scripts.crpo.event import owners_config
from scripts.crpo.common import button_click


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
                time.sleep(0.5)
                self.floating_action()
                self.ui_event_floating_action = 'Pass'
                time.sleep(0.5)
                self.web_element_click_xpath(page_elements.floating_actions['event_upload_candidates'])
                self.ui_event_upload_candidate_action = 'Pass'

                self.web_element_send_keys_xpath(page_elements.file['event_upload_file'], self.file)

                time.sleep(1)
                button_click.button(self, 'Next')

                self.web_element_click_xpath(page_elements.event_config['declare_checkbox'])

                self.web_element_send_keys_xpath(page_elements.event_config['signature'],
                                                 'AutomationVS')

                time.sleep(0.5)
                button_click.button(self, 'I Agree')

                self.web_element_click_xpath(page_elements.title['title'].format('Edit'))

                time.sleep(0.5)
                self.driver.find_element_by_xpath(page_elements.event_config['upload_candidate_name']).clear()
                self.web_element_send_keys_xpath(page_elements.event_config['upload_candidate_name'],
                                                 self.event_sprint_version)

                time.sleep(0.5)
                self.driver.find_element_by_xpath(page_elements.event_config['upload_candidate_email']).clear()
                self.web_element_send_keys_xpath(page_elements.event_config['upload_candidate_email'], email_id)

                time.sleep(0.5)
                self.driver.find_element_by_xpath(page_elements.event_config['upload_candidate_usn']).clear()
                self.web_element_send_keys_xpath(page_elements.event_config['upload_candidate_usn'],
                                                 self.event_sprint_version)

                time.sleep(0.5)
                self.driver.execute_script("window.scrollTo(0,200);")
                self.web_element_click_xpath(page_elements.event_config['details_save'])
                time.sleep(0.5)
                button_click.button(self, 'Save')

# -------- Validation check
                self.upload_candidate_validation()

            except Exception as error:
                ui_logger.error(error)

    def upload_candidate_validation(self):
        try:
            time.sleep(3)
            self.web_element_text_xpath(page_elements.event_config['upload_candidate_count'])

            if self.text_value.strip() == 'Uploaded 1':
                self.ui_event_upload_candidate = 'Pass'
                print('**-------->>> Candidate uploaded to event successfully')
            else:
                print('Failed to upload candidate to event <<<--------**')

            time.sleep(1)
            self.web_element_click_xpath(page_elements.event_config['close_pop_details_window'])
            self.driver.refresh()

        except Exception as error:
            ui_logger.error(error)
