import provide_feedback
import page_elements
import config
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class UpdateFeedback(provide_feedback.OldProvideFeedback):
    def __init__(self):
        super(UpdateFeedback, self).__init__()

        self.ui_all_interviews_bucket_o = 'Pass'
        self.ui_completed_interview_bucket_o = 'Pass'
        self.ui_unlock_feedback_action_o = 'Pass'
        self.ui_unlock_feedback_o = 'Pass'
        self.ui_update_decision_int1_o = 'Pass'
        self.ui_update_feedback_int1_o = 'Pass'
        self.ui_update_decision_int2_o = 'Pass'
        self.ui_update_feedback_int2_o = 'Pass'

    def unlock_feedback(self):
        try:
            # --------------------------- New tab to login as admin ----------------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- admin login ------------------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_ams_username)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_ams_password)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "------------------ Admin Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            time.sleep(2)
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.unlock['All_my_interviews'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)
            print "-------------------- All interviews Bucket ------------------------"
            self.ui_all_interviews_bucket_o = 'Pass'

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)
            print "-------------------- Completed Feedback Bucket ------------------------"
            self.ui_completed_interview_bucket_o = 'Pass'

            time.sleep(3)
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.unlock['unlock_action'])
            self.xpath.click()
            self.ui_unlock_feedback_action_o = 'Pass'

            self.x_path_element_webdriver_wait(page_elements.unlock['all_interviewers'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.unlock['unlock_feedback_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.unlock['comment'])
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.unlock['ok'])
            self.xpath.click()
            print "-------------------- Unlocked Feedback ------------------------"
            self.ui_unlock_feedback_o = 'Pass'

        except exceptions.NoSuchElementException as error:
            print error

    def update_feedback_and_decision_int1(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int1_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "-------------------- Interviewer1 Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)
            print "-------------------- Completed Feedback Bucket ------------------------"

            time.sleep(3)
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()

            # --------------------------------- Provide feedback -------------------------------------------------------
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.update['shortlist'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['rating_1'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.feedback['comment_1'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['rating_2'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.feedback['comment_2'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['overall'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['submit_feedback'])
            self.xpath.click()
            print "-------------------- Submitted Feedback ------------------------"

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.feedback['feedback_form_validation_agree'])
            self.xpath.click()
            print "-------------------- feedback_form_validation_agree ------------------------"
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['review_feedback'])
            self.xpath.click()
            print "-------------------- review_feedback ------------------------"
            self.ui_update_decision_int1_o = 'Pass'
            self.ui_update_feedback_int1_o = 'Pass'

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except exceptions.NoSuchElementException as error:
            print error

    def update_feedback_and_decision_int2(self):
        try:
            # --------------------------- New tab to login as interviewer ----------------------------------------------
            time.sleep(3)
            self.driver.execute_script("window.open('about:blank', 'tab2');")
            self.driver.switch_to.window("tab2")
            self.driver.get(config.configs[self.login_server])
            print "-------------------- New tab open with URL ------------------------"

            # --------------------------- Login as an interviewer ------------------------------------------------------
            self.name_element_webdriver_wait(page_elements.login['username'])
            self.name.send_keys(self.xl_username_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['password'])
            self.xpath.send_keys(self.xl_password_int2_o)

            self.x_path_element_webdriver_wait(page_elements.login['login_button'])
            self.xpath.click()
            print "-------------------- Interviewer2 Login successfully ------------------------"

            # --------------------------------- event details ----------------------------------------------------------
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['event_interviews'])
            self.xpath.click()
            print "-------------------- Floating action ------------------------"

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['Interview_bucket'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)
            print "-------------------- Completed Feedback Bucket ------------------------"

            time.sleep(3)
            self.name_element_webdriver_wait(page_elements.event['applicant_select_checkbox'])
            self.name.click()

            self.x_path_element_webdriver_wait(page_elements.event['provide_feedback'])
            self.xpath.click()

            # --------------------------------- Provide feedback -------------------------------------------------------
            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.update['shortlist'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.feedback['rating_1'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.feedback['comment_1'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['rating_2'])
            self.xpath.click()
            self.xpath.send_keys(Keys.ARROW_DOWN)
            self.xpath.send_keys(Keys.ENTER)

            self.x_path_element_webdriver_wait(page_elements.feedback['comment_2'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['overall'])
            self.xpath.clear()
            self.xpath.send_keys(self.xl_update_feedback_comment_o)

            self.x_path_element_webdriver_wait(page_elements.feedback['submit_feedback'])
            self.xpath.click()
            print "-------------------- Submitted Feedback ------------------------"

            time.sleep(3)
            self.x_path_element_webdriver_wait(page_elements.feedback['feedback_form_validation_agree'])
            self.xpath.click()
            print "-------------------- feedback_form_validation_agree ------------------------"
            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.feedback['review_feedback'])
            self.xpath.click()
            print "-------------------- review_feedback ------------------------"
            self.ui_update_decision_int2_o = 'Pass'
            self.ui_update_feedback_int2_o = 'Pass'

            self.browser_close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        except exceptions.NoSuchElementException as error:
            print error
