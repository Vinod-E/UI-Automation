import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.quick_interview_flow import quick_interview_excel


class QuickEventSearch(quick_interview_excel.QuickInterviewExcelRead):
    def __init__(self):
        super(QuickEventSearch, self).__init__()
        self.current_status = ''
        self.event_validation_check = ''
        self.applicant_current_status = ''

        self.ui_event_tab_q = ''
        self.ui_advance_search_q = ''
        self.ui_event_details_q = ''
        self.ui_event_validation_q = ''
        self.ui_floating_action_q = ''
        self.ui_event_applicant_action_q = ''
        self.ui_applicant_advance_search_q = ''
        self.ui_more_button_q = ''
        self.ui_quick_interview_action = ''

        self.ui_candidate_getby_q = ''
        self.ui_applicant_current_status_q = ''

    def event_search(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            time.sleep(0.5)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_q, 'Event')
            self.event_getby_details()
            self.event_validation('Quick-interview-schedule')
            self.floating_action()

            time.sleep(0.3)
            self.web_element_click_xpath(page_elements.floating_actions['View_Applicants'])

            time.sleep(1)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_q, 'Applicant grid')

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,100);")
            self.check_box()
            button_click.more_button(self)
            button_click.all_buttons(self, 'Quick Interview Schedule')

            if self.event_validation_check == 'True':
                print('**-------->>> Interview schedule happened successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_q = 'Pass'
                self.ui_advance_search_q = 'Pass'
                self.ui_event_details_q = 'Pass'
                self.ui_event_validation_q = 'Pass'
                self.ui_floating_action_q = 'Pass'
                self.ui_event_applicant_action_q = 'Pass'
                self.ui_applicant_advance_search_q = 'Pass'
                self.ui_more_button_q = 'Pass'
                self.ui_quick_interview_action = 'Pass'

            self.driver.execute_script("window.scrollTo(0,200);")
            self.web_element_click_xpath(page_elements.title['title'].format('Interviewers'))
            self.web_element_send_keys_xpath(
                page_elements.title['title'].format('Type here to search'), self.xl_interview_names)
            self.web_element_click_xpath(page_elements.multi_selection_box['moveAllItemsRight'])
            button_click.all_buttons(self, 'Done')
            self.web_element_send_keys_xpath(
                page_elements.text_fields['text_field'].format('Select Interview Round'), self.xl_stage_q)
            self.drop_down_selection()
            self.web_element_send_keys_xpath(
                page_elements.text_fields['place_holder'].format('Your Comments'), self.xl_comment_q)
            self.web_element_click_xpath(
                page_elements.buttons['quick_schedule'].format("'", "scheduleInterview", "'"))
            self.dismiss_message()

            time.sleep(1)
            self.applicant_getby_details(self.event_sprint_version_q)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation('Scheduled')

            if self.current_status == 'True':
                print('**-------->>> Interview schedule happened successfully')

                # -------------------- output report values ----------------
                self.ui_candidate_getby_q = 'Pass'

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_q))
            get_event_name = self.text_value

            if get_event_name.strip() == self.event_sprint_version_q:
                self.event_validation_check = 'True'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            ui_logger.error(e)

    def current_status_validation(self, status):
        try:
            self.web_element_text_xpath(page_elements.event_applicant['applicant_validation'].format(status))
            self.applicant_current_status = self.text_value
            if self.applicant_current_status.strip() == status:
                self.current_status = 'True'
                self.ui_applicant_current_status_q = 'Pass'
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
            time.sleep(1)

        except Exception as error:
            ui_logger.error(error)
