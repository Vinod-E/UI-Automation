import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.manage_interviewers import nomination_acceptance


class EmAcceptance(nomination_acceptance.NominationAcceptance):
    def __init__(self):
        super(EmAcceptance, self).__init__()

        self.ui_event_tab_em = ''
        self.ui_advance_search_em = ''
        self.ui_event_details_em = ''
        self.ui_event_validation_em = ''
        self.ui_floating_action_em = ''
        self.ui_manage_interviews_action_em = ''
        self.ui_panel_skill11_search = ''
        self.ui_skill1_interviewer_status = ''
        self.ui_panel_skill12_search = ''
        self.ui_skill2_interviewer_status = ''
        self.ui_clear_search = ''
        self.ui_approve_action = ''
        self.ui_approved = ''
        self.ui_em_request_validated = ''
        self.ui_sync_interviewers = ''

    def em_approve(self):
        try:
            self.crpo_logout()
            self.login('EventManager', self.xl_username, self.xl_password)

            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_mi, 'Event')
            self.event_getby_details()
            self.event_validation('Manage Interviewers')
            self.floating_action()
            self.web_element_click_xpath(page_elements.floating_actions['manage_interviewers'])

            # -------------------- output report values ----------------
            if self.get_event_name.strip() == self.event_sprint_version_mi:
                self.ui_event_tab_em = 'Pass'
                self.ui_advance_search_em = 'Pass'
                self.ui_event_details_em = 'Pass'
                self.ui_event_validation_em = 'Pass'
                self.ui_floating_action_em = 'Pass'
                self.ui_manage_interviews_action_em = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def em_skill1_filter(self):
        try:
            time.sleep(2)
            self.web_element_send_keys_xpath(page_elements.manage_interviews['panel_search'], self.xl_skill1_mi)

            time.sleep(0.5)
            self.web_element_text_xpath(page_elements.manage_interviews['paging'])
            if '1-1' in self.text_value:
                self.ui_panel_skill11_search = 'Pass'
                print('**-------->>> Panel1 search is working')

            self.web_element_text_xpath(page_elements.title['title'].format('Pending'))
            if self.text_value == 'Accepted':
                self.ui_skill1_interviewer_status = 'Pass'
                print('**-------->>> Interviewer1 status verified - {}'.format(self.text_value))

        except Exception as error:
            ui_logger.error(error)

    def em_skill2_filter(self):
        try:
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.manage_interviews['panel_search'], self.xl_skill2_mi)

            self.web_element_text_xpath(page_elements.manage_interviews['paging'])
            if '1-1' in self.text_value:
                self.ui_panel_skill12_search = 'Pass'
                print('**-------->>> Panel2 search is working')

            self.web_element_text_xpath(page_elements.title['title'].format('Pending'))
            if self.text_value == 'Accepted':
                self.ui_skill2_interviewer_status = 'Pass'
                print('**-------->>> Interviewer2 status verified - {}'.format(self.text_value))
            time.sleep(1)

        except Exception as error:
            ui_logger.error(error)

    def approve_sync(self):
        try:
            self.web_element_click_xpath(page_elements.buttons['clear_refresh'])
            time.sleep(2)
            self.web_element_click_xpath(page_elements.grid['all'])
            self.web_element_click_xpath(page_elements.buttons['common_button'].format('Actions'))
            self.web_element_click_xpath(page_elements.manage_interviews['approve'])

            self.web_element_text_xpath(page_elements.title['title'].format('Approved'))
            if self.text_value == 'Approved':
                self.ui_clear_search = 'Pass'
                self.ui_approve_action = 'Pass'
                self.ui_approved = 'Pass'
                self.ui_em_request_validated = 'Pass'
                print('**-------->>> Event Manager - {}'.format(self.text_value))

            time.sleep(1)
            self.web_element_click_xpath(page_elements.title['title'].format('This will sync interviewers for'
                                                                             ' whom you have accepted nomination with '
                                                                             'the event owners'))
            self.glowing_messages('Interviewers have been successfully synced to event.')
            if self.message_validation == 'True':
                self.ui_sync_interviewers = 'Pass'

        except Exception as error:
            ui_logger.error(error)
