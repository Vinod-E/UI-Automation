import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.quick_interview_flow import event_search


class ProvideFeedback(event_search.QuickEventSearch):
    def __init__(self):
        super(ProvideFeedback, self).__init__()

    def provide_feedback(self, decision, comment):
        try:

            self.web_element_click_id(page_elements.grid_actions['provide_feedback'])

            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.web_element_click_xpath(decision)
            self.web_element_send_keys_xpath(page_elements.interview['rating_1'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_1'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['rating_2'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_2'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['overall_comment'], comment)

        # ------ Submitted
            time.sleep(1)
            button_click.all_buttons(self, 'Submit Feedback')
            self.driver.execute_script("window.scrollTo(0,200);")
            time.sleep(0.3)
            button_click.all_buttons(self, 'Agree and Submit')
            button_click.all_buttons(self, 'Agree and Submit')
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as error:
            ui_logger.error(error)
