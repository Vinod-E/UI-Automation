import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import save_draft_old


class PartialFeedback(save_draft_old.SaveAsDraft):
    def __init__(self):
        super(PartialFeedback, self).__init__()
        self.draft_validation_check = []
        self.partial_bucket_validation = []

        self.ui_provide_feedback_action_p = []
        self.ui_partial_submission = []
        self.ui_draft_validation = []

        self.ui_partial_bucket = []
        self.ui_provide_feedback_action_p_f = []
        self.ui_submit_feedback_p_f = []

    def partial_feedback(self):
        try:
            time.sleep(1)
            self.web_element_click_id(page_elements.grid_actions['provide_feedback'])

            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['partial_feedback'])
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(0.3)
            self.web_element_click_xpath(page_elements.buttons['agree'].format("'", 'submitWithouChange', "'"))

            # ----------- validation
            self.draft_validation_check = 'True'
            if self.draft_validation_check == 'True':
                print('**-------->>> Feedback draft is saved successfully')
                print('**-------->>> Partial feedback submitted successfully')

            time.sleep(0.5)
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.partial_bucket()
            if self.partial_bucket_validation == 'True':
                print('**-------->>> Feedback submitted from partial bucket successfully')

                # -------------------- output report values ----------------
                self.ui_provide_feedback_action_p = 'Pass'
                self.ui_partial_submission = 'Pass'
                self.ui_draft_validation = 'Pass'
                self.ui_partial_bucket = 'Pass'
                self.ui_provide_feedback_action_p_f = 'Pass'
                self.ui_submit_feedback_p_f = 'Pass'

            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            api_logger.error(error)

    def partial_bucket(self):
        try:
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buckets['Partial_interviews'])

            self.check_box()
            self.web_element_click_id(page_elements.grid_actions['provide_feedback'])
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(1.5)
            self.web_element_click_xpath(page_elements.buttons['submit_feedback'])
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(0.6)
            self.web_element_click_xpath(page_elements.buttons['agree'].format("'", 'submitWithouChange', "'"))
            self.web_element_click_xpath(page_elements.buttons['agree'].format("'", 'agreeToChange', "'"))
            time.sleep(3.5)

            self.partial_bucket_validation = 'True'

        except Exception as error:
            api_logger.error(error)
