import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.live_interview_flow import provide_feedback


class LiveInterviewSchedule(provide_feedback.ProvideFeedback):
    def __init__(self):
        super(LiveInterviewSchedule, self).__init__()

        self.applicant_current_status = ''
        self.get_event_name = ''
        self.event_name_in_live = ''
        self.live_submit = ''
        self.event_validation_check = []

        self.ui_event_tab_li = []
        self.ui_advance_search_li = []
        self.ui_event_details_li = []
        self.ui_event_validation_li = []
        self.ui_floating_action_li = []
        self.ui_live_interviews_action_li = []

        self.ui_live_interview_validation = []
        self.ui_live_schedule = []
        self.ui_provide_feedback_button = []

    def live_schedule(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_l, 'Event')
            self.event_getby_details()
            self.event_validation('live-interview-schedule')
            self.floating_action()
            self.web_element_click_xpath(page_elements.floating_actions['live_interview'])

# ---------- Validation
            time.sleep(1)
            self.live_screen_validation()

            self.web_element_click_xpath(page_elements.buckets['select_interview_stage'].format(self.stage1_l))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Candidate Name'),
                                             self.event_sprint_version_l)
            self.web_element_click_xpath(page_elements.buttons['live_applicant_search'])

            time.sleep(0.6)
            self.all_check_box_unlock()
            self.web_element_click_xpath(page_elements.buttons['live_schedule_multiple'])
            self.web_element_click_xpath(page_elements.live_interview['int1_select'])
            self.web_element_click_xpath(page_elements.live_interview['int2_select'])
            self.web_element_click_xpath(page_elements.buttons['live_schedule'])

            # -------------------- output report values ----------------
            if self.get_event_name.strip() == self.event_sprint_version_l:
                self.ui_event_tab_li = 'Pass'
                self.ui_advance_search_li = 'Pass'
                self.ui_event_details_li = 'Pass'
                self.ui_event_validation_li = 'Pass'
                self.ui_floating_action_li = 'Pass'
                self.ui_live_interviews_action_li = 'Pass'

            if self.event_sprint_version_l in self.event_name_in_live:
                self.ui_live_interview_validation = 'Pass'
                self.ui_live_schedule = 'Pass'
                self.ui_provide_feedback_button = 'Pass'

        except Exception as e:
            ui_logger.error(e)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.web_element_text_xpath(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_l))
            self.get_event_name = self.text_value

            if self.get_event_name.strip() == self.event_sprint_version_l:
                self.event_validation_check = 'Pass'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            ui_logger.error(e)

    def live_screen_validation(self):
        try:
            self.web_element_text_xpath(page_elements.live_interview['validate'])
            self.event_name_in_live = self.text_value
            if self.event_sprint_version_l in self.event_name_in_live:
                print('**-------->>> Entered into live interview schedule screen')
        except Exception as e:
            ui_logger.error(e)

