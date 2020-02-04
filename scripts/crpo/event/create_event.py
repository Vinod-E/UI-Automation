import time
import page_elements
from datetime import datetime
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
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

            time.sleep(5)
            self.x_path_element_webdriver_wait(page_elements.buttons['create'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Name"))
            self.xpath.send_keys(self.event_sprint_version)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Requirement"))
            time.sleep(1)
            self.xpath.send_keys(self.req_name_sprint_version)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['job_field'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Search'))
            self.xpath.send_keys(self.job_name_sprint_version)

            self.x_path_element_webdriver_wait(page_elements.event['job_selection'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['done'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Slot'))
            self.xpath.send_keys(self.xl_slot)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('From'))
            self.xpath.send_keys(self.event_date)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('To'))
            self.xpath.send_keys(self.event_date)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('Event Manager'))
            time.sleep(1)
            self.xpath.send_keys(self.xl_em)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format('College'))
            self.xpath.send_keys(self.xl_college)
            time.sleep(1)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['ec_enable'])
            self.xpath.click()

            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.buttons['event_create'])
            self.xpath.click()
            time.sleep(3)

            # ------------------------------- Validating event ---------------------------------------------------------
            self.event_validation('the event')
            if self.validation_check == 'True':
                print('**-------->>> Event created successfully')
                self.ui_create_event = 'Pass'
            else:
                print('Failed to create event <<<--------**')

        except Exception as error:
            api_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.x_path_element_webdriver_wait(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version))
            self.get_event_name = self.xpath.text

            if self.get_event_name.strip() == self.event_sprint_version:
                self.validation_check = 'True'
                self.event_validation_check = 'Pass'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            api_logger.error(e)


# ob = CreateEvent()
# ob.create_event()
