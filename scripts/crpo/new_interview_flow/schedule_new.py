import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.new_interview_flow import feedback_form_configure


class Schedule(feedback_form_configure.FeedbackConfiguration):
    def __init__(self):
        super(Schedule, self).__init__()

        self.applicant_current_status = ''
        self.get_event_name = ''
        self.event_validation_check = []

        self.ui_event_tab_n = []
        self.ui_advance_search_n = []
        self.ui_event_details_n = []
        self.ui_event_validation_n = []
        self.ui_floating_action_n = []
        self.ui_event_applicant_action_n = []
        self.ui_applicant_advance_search_n = []
        self.ui_change_applicant_status_action_n = []
        self.ui_change_applicant_status_n = []
        self.ui_candidate_getby_n = []
        self.ui_applicant_current_status_n = []

    def new_interview_schedule(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            time.sleep(0.5)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.job_sprint_version_n, 'Event')
            self.event_getby_name()
            self.event_validation('interview-schedule', self.get_event_name.strip())
            self.actions_dropdown()
            time.sleep(0.3)
            self.floating_action('View_Applicants')

            time.sleep(1)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.job_sprint_version_n, 'Applicant grid')

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,100);")
            self.check_box()
            self.applicant_schedule_status_change(self.xl_stage_n,
                                                  self.xl_status_n,
                                                  self.xl_comment_n)
            self.dismiss_message()
            if self.applicant_schedule_statuschange == 'True':
                print('**-------->>> Interview schedule happened successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab_n = 'Pass'
                self.ui_advance_search_n = 'Pass'
                self.ui_event_details_n = 'Pass'
                self.ui_event_validation_n = 'Pass'
                self.ui_floating_action_n = 'Pass'
                self.ui_event_applicant_action_n = 'Pass'
                self.ui_applicant_advance_search_n = 'Pass'
                self.ui_change_applicant_status_action_n = 'Pass'
                self.ui_change_applicant_status_n = 'Pass'

            time.sleep(1)
            self.applicant_getby_name(self.job_sprint_version_n)
            self.ui_candidate_getby_n = 'Pass'
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation('Scheduled')

            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)

    def current_status_validation(self, status):
        try:
            self.web_element_text_xpath(page_elements.event_applicant['applicant_validation'].format(status))
            self.applicant_current_status = self.text_value
            if self.applicant_current_status.strip() == status:
                self.ui_applicant_current_status_n = 'Pass'
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
            time.sleep(1)

        except Exception as error:
            ui_logger.error(error)
