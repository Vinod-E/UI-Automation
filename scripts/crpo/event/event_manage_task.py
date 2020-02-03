import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.event import change_applicant_status


class EventManageTask(change_applicant_status.ChangeApplicantStatus):
    def __init__(self):
        super(EventManageTask, self).__init__()

        self.applicant_with_id = ''

        self.ui_candidate_floating_action = []
        self.ui_candidate_manage_task_action = []
        self.task_validation_check = []
        self.ui_task_candidate_name = []

    def manage_task_event(self):
        try:
            self.floating_action()
            self.ui_candidate_floating_action = 'Pass'

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.floating_actions['manage_task'])
            self.xpath.click()
            self.ui_candidate_manage_task_action = 'Pass'

            self.driver.switch_to.window(self.driver.window_handles[2])
            time.sleep(1.5)

            # -------------------------------- Task validation ---------------------------------------------------------
            self.activity_task_validation()
            if self.task_validation_check == 'Pass':
                self.ui_task_candidate_name = 'Pass'
                print('**-------->>> Task assigned to applicant successfully')

            self.driver.close()
            time.sleep(1.5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            time.sleep(1.5)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            api_logger.error(error)

    def activity_task_validation(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.event_applicant['task_candidate_name'])
            self.applicant_with_id = self.xpath.text
            if self.event_sprint_version in self.applicant_with_id:
                self.task_validation_check = 'Pass'
                print('**-------->>> Manage task candidate '
                      'details verified to event :: {}'.format(self.applicant_with_id))
            else:
                print('Wrong applicant got assigned task <<<---------**')

        except Exception as error:
            api_logger.error(error)
