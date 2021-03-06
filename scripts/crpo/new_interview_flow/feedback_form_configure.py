import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.new_interview_flow import job_search
from scripts.crpo.common import button_click


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
            self.actions_dropdown()
            self.floating_action('feedback_form')

            self.ui_floating_action_n = 'Pass'
            self.ui_feedback_form_action_n = 'Pass'

# ---------- Configure new feedback
            self.clear(page_elements.text_fields['text_field'].format("Interview Stages"))
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Interview Stages"),
                                             self.xl_stage_n)
            self.drop_down_selection()

            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name like."),
                                             self.xl_new_form)
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['button_click'].format("'", 'search', "'"))
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(0.5)
            button_click.all_buttons(self, 'Use')
            # time.sleep(0.5)
            # self.dismiss_message()

            time.sleep(0.5)
            self.feedback_form_validation()

        except Exception as error:
            ui_logger.error(error)

    def feedback_form_validation(self):
        try:
            for i in self.xl_new_form:
                self.form = i
            self.driver.execute_script("window.scrollTo(0,100);")
            self.web_element_text_xpath(page_elements.title['title'].format('Name'))
            self.configure_form = self.text_value

            if self.form in self.configure_form:
                print('**-------->>> Feedback form configure to {} successfully'.format(self.xl_stage_n))
                self.ui_feedback_form_search = 'Pass'
                self.ui_feedback_form_validation = 'Pass'
        except Exception as ee:
            ui_logger.error(ee)
