import time
import page_elements
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.new_interview_flow import job_search


class FeedbackConfiguration(job_search.JobSearch):
    def __init__(self):
        super(FeedbackConfiguration, self).__init__()

        self.configure_form = ''
        self.form = ''

        self.ui_floating_action_n = []
        self.ui_feedback_form_action_n = []
        self.ui_feedback_form_validation = []
        self.ui_feedback_form_search = []

    def feedback_configuration(self):
        try:

            # --------- job process
            self.job_search_new()
            self.floating_action()

            self.x_path_element_webdriver_wait(page_elements.floating_actions['feedback_form'])
            self.xpath.click()
            self.ui_floating_action_n = 'Pass'
            self.ui_feedback_form_action_n = 'Pass'

# ---------- Configure new feedback
            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Interview Stages"))
            self.xpath.clear()
            self.xpath.send_keys(self.xl_stage_n)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Name like."))
            self.xpath.send_keys(self.xl_new_form)

            time.sleep(1)
            self.x_path_element_webdriver_wait(page_elements.buttons['new_template_search'].format("'", 'search', "'"))
            self.xpath.click()

            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.buttons['use'].format("'", 'tag', "'"))
            self.xpath.click()

            time.sleep(1)
            self.feedback_form_validation()

        except Exception as error:
            api_logger.error(error)

    def feedback_form_validation(self):
        try:
            for i in self.xl_new_form:
                self.form = i
            self.driver.execute_script("window.scrollTo(0,100);")
            self.x_path_element_webdriver_wait(page_elements.title['title'].format('Name'))
            self.configure_form = self.xpath.text

            if self.form in self.configure_form:
                print('**-------->>> Feedback form configure to {} successfully'.format(self.xl_stage_n))
                self.ui_feedback_form_search = 'Pass'
                self.ui_feedback_form_validation = 'Pass'
        except Exception as ee:
            api_logger.error(ee)
