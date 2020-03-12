import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.job import ec_task_config
from selenium.webdriver.common.keys import Keys


class FeedbackForm(ec_task_config.ECTaskconfig):
    def __init__(self):
        super(FeedbackForm, self).__init__()

        self.ui_interview_stage1 = []
        self.ui_interview_stage2 = []
        self.ui_interview_stage3 = []
        self.feedback_form_config_flag = []
        self.ui_feedback_form_action = []

    def feedback_form(self, interview_stage, template):
        try:
            # -------------------------- Interview stage / feedback form configuration -----------------------------

            self.driver.find_element_by_xpath(
                page_elements.text_fields['text_field'].format("Interview Stages")).clear()
            time.sleep(1.5)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Interview Stages"),
                                             interview_stage)
            time.sleep(1)
            self.drop_down_selection()

            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format("Name like."), template)

            self.web_element_click_xpath(page_elements.buttons['template-search'])

            self.driver.execute_script("window.scrollTo(0,200);")

            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.job_config['template_use'])

            self.web_element_click_xpath(page_elements.job_config['template_comment'])

            self.web_element_click_xpath(page_elements.job_config['template_reject'])

            self.driver.execute_script("window.scrollTo(0,300);")
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buttons['template_save'])

            # --------------- For validation check ---------------
            self.feedback_form_config_flag = 'Pass'
            self.driver.execute_script("window.scrollTo(0,-200);")

            print('**-------->>> {} feedbackForm configured successfully'.format(interview_stage))
        except Exception as error:
            api_logger.error(error)

    def config_feedback_form(self):
        self.job_validation('feedback form')
        if self.job_name_breadcumb == self.job_name_sprint_version:
            try:
                time.sleep(0.5)
                self.floating_action()

                self.web_element_click_xpath(page_elements.floating_actions['feedback_form'])
                self.ui_feedback_form_action = 'Pass'
                # -------------------------- Interview stage / feedback form configuration -----------------------------
                self.feedback_form(self.xl_interview_stage_01, self.xl_interview_template_01)
                if self.feedback_form_config_flag == 'Pass':
                    self.ui_interview_stage1 = 'Pass'

                self.feedback_form(self.xl_interview_stage_02, self.xl_interview_template_02)
                if self.feedback_form_config_flag == 'Pass':
                    self.ui_interview_stage2 = 'Pass'

                self.feedback_form(self.xl_interview_stage_03, self.xl_interview_template_03)
                if self.feedback_form_config_flag == 'Pass':
                    self.ui_interview_stage3 = 'Pass'

            except Exception as config_template:
                api_logger.error(config_template)
