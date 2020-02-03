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

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Interview Stages"))
            self.xpath.clear()
            self.xpath.send_keys(interview_stage)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.text_fields['text_field'].format("Name like."))
            self.xpath.send_keys(template)

            self.x_path_element_webdriver_wait(page_elements.buttons['template-search'])
            self.xpath.click()

            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.job_config['template_use'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.job_config['template_comment'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.job_config['template_reject'])
            self.xpath.click()

            self.driver.execute_script("window.scrollTo(0,200);")
            self.x_path_element_webdriver_wait(page_elements.buttons['template_save'])
            self.xpath.click()
            time.sleep(2)

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
                self.driver.refresh()
                time.sleep(5)
                self.floating_action()

                self.x_path_element_webdriver_wait(page_elements.floating_actions['feedback_form'])
                self.ui_feedback_form_action = 'Pass'
                self.xpath.click()
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


# ob = FeedbackForm()
# ob.config_feedback_form()
