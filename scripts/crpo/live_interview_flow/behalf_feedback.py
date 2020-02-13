import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.live_interview_flow import live_schedule


class BehalfFeedback(live_schedule.LiveInterviewSchedule):
    def __init__(self):
        super(BehalfFeedback, self).__init__()

        self.ui_behalf_choose = []
        self.live_provide_feedback_submitted = []
        self.live_submit_validation = []

    def behalf_of_submission(self):
        try:
            # ----------- feedback providing
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.live_interview['down'])
            self.xpath.click()

            self.provide_feedback(page_elements.live_interview['shortlist'],
                                  self.xl_comment_l)

            # --------- Behalf of Submission
            self.x_path_element_webdriver_wait(page_elements.live_interview['feedback_int1'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.live_interview['feedback_int2'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.buttons['submit_feedback'])
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['agree'].format("'", 'submitWithouChange', "'"))
            self.xpath.click()

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['agree'].format("'", 'agreeToChange', "'"))
            self.xpath.click()
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

            # ------- validation
            self.live_schedule_submit_validation(self.stage1_l, 'Shortlisted')

            # -------------------- output report values ----------------
            if self.live_submit == 'Shortlisted':
                self.ui_behalf_choose = 'Pass'
                self.live_provide_feedback_submitted = 'Pass'
                self.live_submit_validation = 'Pass'

        except Exception as error:
            api_logger.error(error)

    def live_schedule_submit_validation(self, stage, status):
        try:
            self.driver.refresh()
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.buckets['select_interview_stage'].format(stage))
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.title['title'].format(status))
            self.live_submit = self.xpath.text
            if self.live_submit == status:
                print('**-------->>> Live provide feedback submitted successfully')
        except Exception as e:
            api_logger.error(e)
