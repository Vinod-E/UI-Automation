import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import save_darft_new


class SubmitFeedbackInt1(save_darft_new.DraftNew):
    def __init__(self):
        super(SubmitFeedbackInt1, self).__init__()

        self.ui_provide_feedback_action_n_int1 = []
        self.ui_submit_feedback_new_int1 = []

        self.interview_status = ''

    def submit_feedback_int1(self):
        try:
            self.id_element_webdriver_wait(page_elements.grid_actions['provide_feedback'])
            self.id.click()

            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.new_interview['overall'])
            self.xpath.send_keys('INT1')

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['new_submit_feedback'])
            self.xpath.click()
            time.sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.refresh()
            time.sleep(2)
            self.submit_feed_validation(self.xl_int1)

            # -------------------- output report values ----------------
            self.ui_provide_feedback_action_n_int1 = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def submit_feed_validation(self, interviewer):
        try:
            self.x_path_element_webdriver_wait(page_elements.title['title'].format('Shortlisted'))
            self.interview_status = self.xpath.text
            if self.interview_status == 'Shortlisted':
                self.ui_submit_feedback_new_int1 = 'Pass'
                print('**-------->>> Feedback submitted successfully by {}'.format(interviewer))
        except Exception as error:
            api_logger.error(error)
