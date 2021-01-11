import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import login


class Schedule(login.Login):
    def __init__(self):
        super(Schedule, self).__init__()

        self.applicant_current_status = ''
        self.get_event_name = ''
        self.event_validation_check = []

        self.ui_event_tab = []
        self.ui_advance_search = []
        self.ui_event_details = []
        self.ui_event_validation = []
        self.ui_floating_action = []
        self.ui_event_applicant_action = []
        self.ui_applicant_advance_search = []
        self.ui_change_applicant_status_action = []
        self.ui_change_applicant_status = []
        self.ui_candidate_getby = []
        self.ui_applicant_current_status = []

    def interview_schedule(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            time.sleep(4)
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_name()
            self.event_validation('interview-schedule', self.event_sprint_version_o)
            self.actions_dropdown()
            self.floating_action('View_Applicants')

            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_o, 'Applicant grid')

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.check_box()
            self.applicant_schedule_status_change(self.xl_change_applicant_stage_o,
                                                  self.xl_change_applicant_status_o,
                                                  self.xl_change_status_comment_o)
            self.dismiss_message()
            time.sleep(0.2)
            if self.applicant_schedule_statuschange == 'True':
                print('**-------->>> Interview schedule happened successfully')

                # -------------------- output report values ----------------
                self.ui_event_tab = 'Pass'
                self.ui_advance_search = 'Pass'
                self.ui_event_details = 'Pass'
                self.ui_event_validation = 'Pass'
                self.ui_floating_action = 'Pass'
                self.ui_event_applicant_action = 'Pass'
                self.ui_applicant_advance_search = 'Pass'
                self.ui_change_applicant_status_action = 'Pass'
                self.ui_change_applicant_status = 'Pass'

            self.applicant_getby_name(self.event_sprint_version_o)
            self.ui_candidate_getby = 'Pass'
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation('Scheduled')

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)

    def current_status_validation(self, status):
        try:
            time.sleep(2)
            self.web_element_text_xpath(page_elements.event_applicant['applicant_validation'].format(status))
            self.applicant_current_status = self.text_value
            if self.applicant_current_status.strip() == status:
                self.ui_applicant_current_status = 'Pass'
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
            time.sleep(1)

        except Exception as error:
            ui_logger.error(error)

