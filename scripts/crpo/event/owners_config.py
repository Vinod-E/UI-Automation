import page_elements
from logger_settings import ui_logger
from scripts.crpo.event import test_task_config
from scripts.crpo.common import button_click


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

                button_click.button(self, 'Edit')
                self.ui_owner_edit_action = 'Pass'

                self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])

                self.driver.execute_script("window.scrollTo(0,200);")
                button_click.button(self, 'Update')

                print('**-------->>> Event Owners has been added')
                self.ui_event_owner_config = 'Pass'

            except Exception as error:
                ui_logger.error(error)
                print('Failed to configure Event Owners <<<--------**')
