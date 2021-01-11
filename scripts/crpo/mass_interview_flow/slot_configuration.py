import time
import page_elements
from datetime import datetime
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.mass_interview_flow import change_applicant_status


class SlotManagement(change_applicant_status.MassChangeAppStatus):
    def __init__(self):
        self.time = input('slot time (ex:- 10:10 AM) ::')
        super(SlotManagement, self).__init__()

        now = datetime.now()
        self.current_date = now.strftime("%d/%m/%Y")

        self.ui_event_tab_m_1 = ''
        self.ui_advance_search_m_1 = ''
        self.ui_event_details_m_1 = ''
        self.ui_event_validation_m_1 = ''
        self.ui_floating_action_m_1 = ''
        self.ui_slot_config_action_m = ''

        self.ui_event_config_tab = ''
        self.ui_auto_assign_on = ''
        self.ui_chat_config = ''
        self.ui_select_user = ''
        self.ui_save_config = ''

        self.ui_candidate_login_link_copied = ''
        self.candidate_login_link = ''

    def event_search(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            time.sleep(0.5)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_m, 'Event')
            self.event_getby_name()
            self.event_validation('Slot-Configurations', self.event_sprint_version_m)
            self.actions_dropdown()
            self.floating_action('Configure_slots')

            if self.event_validation_check == 'True':
                print('**-------->>> Landed into slot configuration screen successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_m_1 = 'Pass'
                self.ui_advance_search_m_1 = 'Pass'
                self.ui_event_details_m_1 = 'Pass'
                self.ui_event_validation_m_1 = 'Pass'
                self.ui_floating_action_m_1 = 'Pass'
                self.ui_slot_config_action_m = 'Pass'

        except Exception as e:
            ui_logger.error(e)

    def slot_config(self):
        try:
            self.web_element_click_xpath(page_elements.title['title'].format('Current Status'))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Search'), self.xl_stage_m)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')
            button_click.button(self, 'Go')
            print('**-------->>> Stage/Status search for slot configure successfully')
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_number'].
                                             format('No. Of Slots'), str(self.xl_size_m))
            button_click.button(self, 'Go')
            print('**-------->>> Number of slots configured successfully')

            time.sleep(0.9)
            self.web_element_send_keys_xpath(page_elements.text_fields['place_holder'].format('From Date'),
                                             self.current_date)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_number'].
                                             format('Count'), str(self.xl_size_m))
            self.clear(page_elements.text_fields['place_holder'].format('From Time'))
            self.web_element_send_keys_xpath(page_elements.text_fields['place_holder'].format('From Time'),
                                             self.time)
            print('**-------->>> Date/Time/Size entered in the fields')
            time.sleep(1)
            self.web_element_click_xpath(page_elements.title['tooltip'].format("'"'Assign slots'"'"))
            print('**-------->>> Assigned the slot to candidate successfully')
            time.sleep(1)
            button_click.all_buttons(self, 'OK')
            time.sleep(0.5)
            button_click.all_buttons(self, 'OK')
            print('**-------->>> Communicate the slot mail to candidate successfully')

        except Exception as e:
            ui_logger.error(e)

    def c_login_link(self):
        try:
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Candidate Id(s) (Eg: 1234, 2312,...)'),
                self.candidate_id_m)
            button_click.button(self, ' Search')
            self.web_element_click_xpath(page_elements.title['title'].format('View Interview Lobby Link'))
            time.sleep(0.5)

            self.driver.find_element_by_tag_name('h4').click()
            list = self.driver.find_elements_by_tag_name('a')
            for i in list:
                if i.get_attribute('href') is not None:
                    if self.candidate_id_m in i.get_attribute('href'):
                        self.candidate_login_link = i.get_attribute('href')
                        print(self.candidate_login_link)
                        self.ui_candidate_login_link_copied = 'Pass'

            time.sleep(2)
            self.driver.refresh()
            time.sleep(5)

        except Exception as e:
            ui_logger.error(e)

    def slot_auto_assign(self):
        try:
            self.sub_tab('event_configuration_tab')

            self.driver.execute_script("window.scrollTo(0,-300);")
            time.sleep(3)
            self.loop_list('label.btn', 'On')
            time.sleep(2)
            self.web_element_click_xpath(page_elements.title['title'].format('Current Status'))

            self.loop_list('option.ellipsis_text', 'admin')
            self.web_element_click_xpath(page_elements.multi_selection_box['moveSelectedItemsRight'])
            button_click.all_buttons(self, 'Done')
            time.sleep(2)
            button_click.button(self, 'save')

            self.ui_event_config_tab = 'Pass'
            self.ui_auto_assign_on = 'Pass'
            self.ui_chat_config = 'Pass'
            self.ui_select_user = 'Pass'
            self.ui_save_config = 'Pass'

        except Exception as e:
            ui_logger.error(e)

    def loop_list(self, element, value):
        try:
            list = self.driver.find_elements_by_css_selector(element)
            for i in list:
                if value in i.text.strip():
                    i.click()
                    break

        except Exception as e:
            ui_logger.error(e)
