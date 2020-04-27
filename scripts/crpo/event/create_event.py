import time
import page_elements
from datetime import datetime
from logger_settings import ui_logger
from scripts.crpo.event import event_excel


class CreateEvent(event_excel.EventExcelRead):
    def __init__(self):
        super(CreateEvent, self).__init__()

        now = datetime.now()
        self.event_date = now.strftime("%d/%m/%Y")

        # --------------- Value initialization ----------------
        self.validation_check = ''
        self.get_event_name = []

        self.ui_create_event = []
        self.event_validation_check = []

    def create_event(self):
        try:
            self.event_tab()

            self.web_element_click_xpath(page_elements.buttons['create'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name"),
                                             self.event_sprint_version)

            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Requirement"),
                                             self.req_name_sprint_version)
            time.sleep(1)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.event['job_field'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.job_name_sprint_version)

            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            self.web_element_click_xpath(page_elements.buttons['done'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Slot"),
                                             self.xl_slot)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("From"),
                                             self.event_date)

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("To"),
                                             self.event_date)

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Event Manager"),
                                             self.xl_em)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("College"),
                                             self.xl_college)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.event['ec_enable'])

            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_click_xpath(page_elements.buttons['event_create'])

            # ------------------------------- Validating event ---------------------------------------------------------
            self.event_validation('the event')
            if self.validation_check == 'True':
                print('**-------->>> Event created successfully')
                self.ui_create_event = 'Pass'
            else:
                print('Failed to create event <<<--------**')

        except Exception as error:
            ui_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version))
            self.get_event_name = self.text_value

            if self.get_event_name.strip() == self.event_sprint_version:
                self.validation_check = 'True'
                self.event_validation_check = 'Pass'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            ui_logger.error(e)
