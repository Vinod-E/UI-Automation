import time
import page_elements
from datetime import datetime
from logger_settings import ui_logger
from scripts.crpo.event import event_excel
from scripts.crpo.common import button_click


class CreateEvent(event_excel.EventExcelRead):
    def __init__(self):
        super(CreateEvent, self).__init__()

        now = datetime.now()
        self.event_date = now.strftime("%d/%m/%Y")

        # --------------- Value initialization ----------------
        self.validation_check = ''
        self.get_event_name = []

        self.ui_create_event = ''
        self.event_validation_check = ''

    def create_event(self):
        try:
            self.event_tab()

            self.web_element_click_xpath(page_elements.buttons['create'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name"),
                                             self.event_sprint_version)

            time.sleep(4)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Requirement"),
                                             self.req_name_sprint_version)
            time.sleep(1.5)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.event['job_field'])

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Search"),
                                             self.job_name_sprint_version)

            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Slot"),
                                             self.xl_slot)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("From"),
                                             self.event_date)

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("To"),
                                             self.event_date)

            self.web_element_send_keys_xpath(page_elements.text_fields['place_holder'].format("Reporting Date"),
                                             self.event_date)

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Event Manager"),
                                             self.xl_em)
            self.drop_down_selection()

            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("College"),
                                             self.xl_college)
            self.drop_down_selection()

            self.web_element_click_xpath(page_elements.event['ec_enable'])

            self.driver.execute_script("window.scrollTo(0,100);")
            button_click.button(self, 'Create')

            # ------------------------------- Validating event ---------------------------------------------------------
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.getby_details_screen(self.event_sprint_version)
            if self.header_name.strip() == self.event_sprint_version:
                print('**-------->>> Event Validated and continuing '
                      'with created event :: {}'.format(self.event_sprint_version))
                print('**-------->>> Event created successfully')
                self.ui_create_event = 'Pass'
                self.event_validation_check = 'Pass'
            else:
                print('Failed to create event <<<--------**')
                print('Event validation failed Or event creation failed <<<--------**')

        except Exception as error:
            ui_logger.error(error)
