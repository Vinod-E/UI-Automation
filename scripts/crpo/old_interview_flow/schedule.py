import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import interviewer_login


class Schedule(interviewer_login.InterviewerLogin):
    def __init__(self):
        super(Schedule, self).__init__()

        self.applicant_current_status = ''
        self.get_event_name = ''
        self.ui_applicant_current_status = []
        self.event_validation_check = []

    def interview_schedule(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_o, 'Event')
            self.event_getby_details()
            self.event_validation('interview-schedule')
            self.floating_action()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['View_Applicants'])
            self.xpath.click()

            time.sleep(5)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_o, 'Applicant grid')

            # --------------------------- Change Applicant Status to Schedule ------------------------------------------
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.name_element_webdriver_wait(page_elements.grid['check_box'])
            self.name.click()

            self.applicant_schedule_status_change(self.xl_change_applicant_stage_o,
                                                  self.xl_change_applicant_status_o,
                                                  self.xl_change_status_comment_o)

            self.applicant_getby_details(self.event_sprint_version_o)
            self.schedule_validation('Scheduled')

            self.driver.close()
            time.sleep(1.5)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            api_logger.error(error)

    def event_validation(self, config_name):
        # ------------------------------ validating the event name -------------------------------------------------
        try:
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.x_path_element_webdriver_wait(
                page_elements.event_validation['get_event_name'].format(self.event_sprint_version_o))
            self.get_event_name = self.xpath.text

            if self.get_event_name.strip() == self.event_sprint_version_o:
                self.event_validation_check = 'Pass'
                print('**-------->>> Event Validated and continuing '
                      'with {} to created event :: {}'.format(config_name, self.get_event_name.strip()))
            else:
                print('Event validation failed Or event creation failed <<<--------**')
        except Exception as e:
            api_logger.error(e)

    def schedule_validation(self, status):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.x_path_element_webdriver_wait(page_elements.event_applicant['applicant_validation'].format(status))
            self.applicant_current_status = self.xpath.text
            if self.applicant_current_status.strip() == status:
                self.ui_applicant_current_status = 'Pass'
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
            time.sleep(1)

        except Exception as error:
            api_logger.error(error)

