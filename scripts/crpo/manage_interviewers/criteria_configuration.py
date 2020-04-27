import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.manage_interviewers import manage_excel


class CriteriaConfig(manage_excel.ManageInterviewExcelRead):
    def __init__(self):
        super(CriteriaConfig, self).__init__()

        self.get_event_name = ''
        self.event_validation_check = ''
        self.nomination_validation_check = ''

        self.ui_event_tab_mi = ''
        self.ui_advance_search_mi = ''
        self.ui_event_details_mi = ''
        self.ui_event_validation_mi = ''
        self.ui_floating_action_mi = ''
        self.ui_manage_interviews_action_mi = ''

        self.skill1_configured = ''
        self.skill2_configured = ''
        self.nomination_on_off = ''
        self.send_mail_to_interviewers = ''

    def event_search(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_mi, 'Event')
            self.event_getby_details()
            self.event_validation('Manage Interviewers')
            self.floating_action()
            self.web_element_click_xpath(page_elements.floating_actions['manage_interviewers'])

            # -------------------- output report values ----------------
            if self.get_event_name.strip() == self.event_sprint_version_mi:
                self.ui_event_tab_mi = 'Pass'
                self.ui_advance_search_mi = 'Pass'
                self.ui_event_details_mi = 'Pass'
                self.ui_event_validation_mi = 'Pass'
                self.ui_floating_action_mi = 'Pass'
                self.ui_manage_interviews_action_mi = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_mi))
            self.get_event_name = self.text_value

            if self.get_event_name.strip() == self.event_sprint_version_mi:
                self.event_validation_check = 'True'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            ui_logger.error(e)

    def invite_interviewers_config(self):
        try:
            self.skill_1()
            self.web_element_click_xpath(page_elements.manage_interviews['add_criteria'])
            self.skill_2()
            self.web_element_click_xpath(page_elements.buttons['save_invite_int'])
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buttons['send_mail'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            time.sleep(0.3)
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Mail will be sent to all interviewers fulfilling the criteria')
            time.sleep(0.3)
            if self.message_validation == 'True':
                self.skill1_configured = 'Pass'
                self.skill2_configured = 'Pass'
                self.nomination_on_off = 'Pass'
                self.send_mail_to_interviewers = 'Pass'
                print('**-------->>> Nomination mail sent to interviewers successfully')

        except Exception as error:
            ui_logger.error(error)

    def skill_1(self):
        try:
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Select Panel Type'),
                                             self.xl_skill1_mi)
            self.drop_down_selection()
            self.web_element_click_xpath(page_elements.manage_interviews['Search_interviewers'])

            time.sleep(0.5)
            self.clear(page_elements.text_fields['text_number'].format('Eg: 20'))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_number'].format('Eg: 20'), '1')
            self.clear(page_elements.text_fields['text_number'].format('Eg: 50'))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_number'].format('Eg: 50'), '1')

        except Exception as error:
            ui_logger.error(error)

    def skill_2(self):
        try:
            self.web_element_send_keys_xpath(page_elements.manage_interviews['panel2'],
                                             self.xl_skill2_mi)
            self.drop_down_selection()
            self.web_element_click_xpath(page_elements.manage_interviews['Search_interviewers2'])

            time.sleep(0.5)
            self.clear(page_elements.manage_interviews['required_int'])
            self.web_element_send_keys_xpath(page_elements.manage_interviews['required_int'], '1')
            self.clear(page_elements.manage_interviews['required_nom'])
            self.web_element_send_keys_xpath(page_elements.manage_interviews['required_nom'], '1')
        except Exception as error:
            ui_logger.error(error)

    def nomination_validation(self):
        try:
            self.web_element_text_xpath(page_elements.manage_interviews['header'])
            if self.text_value.strip() == 'Nominations Sent':
                self.nomination_validation_check = 'True'
        except Exception as error:
            ui_logger.error(error)
