import page_elements
from logger_settings import api_logger
from scripts.crpo.event import test_task_config


class EventOwnersConfig(test_task_config.TestTaskConfig):
    def __init__(self):
        super(EventOwnersConfig, self).__init__()

        self.ui_event_owners_tab = []
        self.ui_owner_edit_action = []
        self.ui_event_owner_config = []

    def event_owner_configure(self):
        self.event_validation('Owners config')
        if self.validation_check == 'True':

            try:
                self.web_element_click_xpath(page_elements.tabs['event_owner_tab'])
                self.ui_event_owners_tab = 'Pass'

                self.web_element_click_xpath(page_elements.event_config['event_owner_edit'])
                self.ui_owner_edit_action = 'Pass'

                self.web_element_click_xpath(page_elements.event_config['event_interviewer_add'])

                self.driver.execute_script("window.scrollTo(0,200);")
                self.web_element_click_xpath(page_elements.buttons['update_event_owners'])

                print('**-------->>> Event Owners has been added')
                self.ui_event_owner_config = 'Pass'

            except Exception as error:
                api_logger.error(error)
                print('Failed to configure Event Owners <<<--------**')
