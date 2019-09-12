import New_feedback_form
import page_elements
import time
from selenium.webdriver.common.keys import Keys


class NewUpdateFeedback(New_feedback_form.NewFeedBack):
    def __init__(self):
        super(NewUpdateFeedback, self).__init__()
        self.ui_int2_update_feedback = []
        self.ui_int2_manual_update_decision = []
        self.ui_int2_updated_feedback = []
        self.ui_int2_completed_interviews = []

    def update_feedback_and_decision(self):

        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
        self.xpath.click()
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)
        print "-------------------- Completed Feedback Bucket ------------------------"
        self.ui_int2_completed_interviews = 'Pass'

        time.sleep(3)
        self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
        self.name.click()

        self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
        self.xpath.click()

        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.new_feedback['u_Q1_comment'])
        self.xpath.send_keys('__Updated')

        self.x_path_element_webdriver_wait(page_elements.new_feedback['u_Q2_comment'])
        self.xpath.send_keys('__Updated')

        self.x_path_element_webdriver_wait(page_elements.new_feedback['u_overall'])
        self.xpath.send_keys('__Updated')

        time.sleep(3)
        self.x_path_element_webdriver_wait(page_elements.new_feedback['shortlist'])
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.new_feedback['update_feedback'])
        self.xpath.click()
        self.ui_int2_update_feedback = 'Pass'
        self.ui_int2_manual_update_decision = 'Pass'
        self.ui_int2_updated_feedback = 'Pass'

        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
