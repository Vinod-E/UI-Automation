import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.mass_interview_flow import mass_excel


class MassChangeAppStatus(mass_excel.MassExcelRead):
    def __init__(self):
        super(MassChangeAppStatus, self).__init__()

        self.applicant_current_status = ''
        self.candidate_id_m = ''

        self.ui_event_tab_m = ''
        self.ui_advance_search_m = ''
        self.ui_event_details_m = ''
        self.ui_event_validation_m = ''
        self.ui_floating_action_m = ''
        self.ui_event_applicant_action_m = ''
        self.ui_event_applicant_grid_m = ''

        self.ui_applicant_search_action_m = ''
        self.ui_applicant_name_search_m = ''
        self.ui_change_applicant_status_action_m = ''
        self.ui_candidate_getby_m = ''
        self.ui_applicant_current_status_m = ''
        self.ui_candidate_id_copied_m = ''

    def applicant_status(self):
        try:
            # --------------------------- Advance search ---------------------------------------------------------------
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,-100);")
            self.advance_search(page_elements.tabs['event_tab'])
            self.name_search(self.event_sprint_version_m, 'Event')
            self.event_getby_name()
            self.event_validation('Slot-Configurations', self.event_sprint_version_m)
            self.actions_dropdown()
            self.floating_action('View_Applicants')

            # -------------------- output report values ----------------
            if self.event_validation_check == 'True':
                print('**-------->>> Landed into applicants screen successfully')
                self.ui_event_tab_m = 'Pass'
                self.ui_advance_search_m = 'Pass'
                self.ui_event_details_m = 'Pass'
                self.ui_event_validation_m = 'Pass'
                self.ui_floating_action_m = 'Pass'
                self.ui_event_applicant_action_m = 'Pass'
                self.ui_event_applicant_grid_m = 'Pass'
            time.sleep(1)
            # --------------------------- Applicant Advance search -----------------------------------------------------
            self.applicant_advance_search()
            self.applicant_name_search(self.event_sprint_version_m, 'Applicant grid')
            self.driver.execute_script("window.scrollTo(0,200);")

            # --------------------------- Change Applicant Status -------------------
            time.sleep(2)
            self.check_box()
            self.applicant_status_change(self.xl_stage_m,
                                         self.xl_status_m,
                                         self.xl_comment_m)
            time.sleep(0.5)
            self.dismiss_message()

            # --------------------------- Applicant common process -----------------------------------------------------
            time.sleep(1)
            self.applicant_getby_name(self.event_sprint_version_m)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.current_status_validation(self.xl_awaited[0])

            # -------------------- output report values ----------------
            if self.applicant_current_status.strip() == self.xl_awaited[0]:
                self.ui_applicant_search_action_m = 'Pass'
                self.ui_applicant_name_search_m = 'Pass'
                self.ui_change_applicant_status_action_m = 'Pass'
                self.ui_candidate_getby_m = 'Pass'
                self.ui_applicant_current_status_m = 'Pass'
                self.ui_candidate_id_copied_m = 'Pass'

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
                print('**-------->>> Applicant stage - status '
                      'movement happened in event :: {}'.format(self.applicant_current_status))
            else:
                print('Failed to change applicant status <<<---------**')
            time.sleep(1)
            self.web_element_text_xpath(page_elements.event_applicant['candidate_id'].format(status))
            self.candidate_id_m = self.text_value
            print(self.candidate_id_m)

        except Exception as error:
            ui_logger.error(error)
