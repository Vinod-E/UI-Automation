import time
import page_elements
from logger_settings import ui_logger
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
            time.sleep(1.5)
            self.web_element_click_xpath(page_elements.live_interview['down'])

            time.sleep(1.5)
            self.live_provide_feedback(page_elements.live_interview['shortlist'], self.xl_comment_l)

            # ------- validation
            self.live_schedule_submit_validation(self.stage1_l, 'Shortlisted')

            # -------------------- output report values ----------------
            if self.live_submit == 'Shortlisted':
                self.ui_behalf_choose = 'Pass'
                self.live_provide_feedback_submitted = 'Pass'
                self.live_submit_validation = 'Pass'

        except Exception as error:
            ui_logger.error(error)

    def live_schedule_submit_validation(self, stage, status):
        try:
            self.driver.refresh()
            time.sleep(2)
            self.web_element_click_xpath(page_elements.buckets['select_interview_stage'].format(stage))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Candidate Name'),
                                             self.event_sprint_version_l)
            self.web_element_click_xpath(page_elements.buttons['live_applicant_search'])

            self.web_element_text_xpath(page_elements.title['title'].format(status))
            self.live_submit = self.text_value
            if self.live_submit == status:
                print('**-------->>> Live provide feedback submitted successfully')
        except Exception as e:
            ui_logger.error(e)
