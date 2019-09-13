import update_feedback
import page_elements
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class LiveInterview(update_feedback.UpdateFeedback):
    def __init__(self):
        super(LiveInterview, self).__init__()

        self.ui_event_getby_id_l = []
        self.ui_live_interview_action_l = []
        self.ui_live_interview_stage_l = []
        self.ui_live_interview_advance_search_l = []
        self.ui_live_interview_schedule_l = []
        self.ui_live_interview_candidate_details_l = []
        self.ui_live_interview_PF_action_l = []
        self.ui_live_decision_l = []
        self.ui_live_feedback_screen_l = []
        self.ui_live_submit_feedback_l = []

    def live_int2_login(self):
        try:
            self.driver.refresh()
            time.sleep(5)
            # --------------------------------- event details ----------------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['event_tab'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.event['Event_advance_search'])
            self.xpath.click()

            self.name_element_webdriver_wait(page_elements.event['event_names'])
            self.name.send_keys(self.event_name_sprint_version_o)

            self.x_path_element_webdriver_wait(page_elements.event['event_search_button'])
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.event['Click_on_event_name'])
            self.xpath.click()
            print "-------------------- Event get by Details screen ------------------------"
            self.ui_event_getby_id_l = 'Pass'

            # --------------------------------- event floating actions -------------------------------------------------
            self.x_path_element_webdriver_wait(page_elements.event['Floating_actions'])
            self.xpath.click()

            time.sleep(2)
            self.x_path_element_webdriver_wait(page_elements.live_interview['live_interview_action'])
            self.xpath.click()
            print "-------------------- Live interview action ------------------------"
            self.ui_live_interview_action_l = 'Pass'

        except exceptions.NoSuchElementException as error:
            print error

    def live_schedule(self):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['select_stage'])
        self.xpath.send_keys('Final Interview')
        print "-------------------- Live interview stage ------------------------"
        self.ui_live_interview_stage_l = 'Pass'

        self.x_path_element_webdriver_wait(page_elements.live_interview['candidate_name'])
        self.xpath.send_keys(self.event_name_sprint_version_o)

        self.x_path_element_webdriver_wait(page_elements.live_interview['search_button'])
        self.xpath.click()
        print "-------------------- Live interview candidate search ------------------------"
        self.ui_live_interview_advance_search_l = 'Pass'

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['select_search_candidates'])
        self.xpath.click()

        self.x_path_element_webdriver_wait(page_elements.live_interview['schedule'])
        self.xpath.click()

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['scheduled'])
        self.xpath.click()
        time.sleep(3)
        print "-------------------- Live interview schedule------------------------"
        self.ui_live_interview_schedule_l = 'Pass'

    def live_provide_feedback(self):
        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['candidate_name'])
        self.xpath.clear()
        self.xpath.send_keys(self.event_name_sprint_version_o)

        self.x_path_element_webdriver_wait(page_elements.live_interview['search_button'])
        self.xpath.click()

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['details'])
        self.xpath.click()
        print "-------------------- Live interview candidate details------------------------"
        self.ui_live_interview_candidate_details_l = 'Pass'

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.live_interview['provide_feedback'])
        self.xpath.click()
        print "-------------------- Live interview provide feedback------------------------"
        self.ui_live_interview_PF_action_l = 'Pass'

        # --------------------------------- Provide feedback -------------------------------------------------------
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.x_path_element_webdriver_wait(page_elements.feedback['shortlist'])
        self.xpath.click()
        self.ui_live_decision_l = 'Pass'

        self.x_path_element_webdriver_wait(page_elements.feedback['rating_1'])
        self.xpath.click()
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)

        self.x_path_element_webdriver_wait(page_elements.feedback['comment_1'])
        self.xpath.send_keys(self.xl_change_status_comment_o)

        self.x_path_element_webdriver_wait(page_elements.feedback['rating_2'])
        self.xpath.click()
        self.xpath.send_keys(Keys.ARROW_DOWN)
        self.xpath.send_keys(Keys.ENTER)

        self.x_path_element_webdriver_wait(page_elements.feedback['comment_2'])
        self.xpath.send_keys(self.xl_change_status_comment_o)

        time.sleep(2)
        self.x_path_element_webdriver_wait(page_elements.feedback['overall'])
        self.xpath.send_keys(self.xl_cancel_reschedule_comment_o)

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
        self.ui_live_feedback_screen_l = 'Pass'
        self.ui_live_submit_feedback_l = 'Pass'

        self.driver.switch_to.window(self.driver.window_handles[0])
