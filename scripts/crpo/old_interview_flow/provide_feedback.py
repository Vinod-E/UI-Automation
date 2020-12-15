import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.old_interview_flow import cancel_request_acceptance


class ProvideFeedback(cancel_request_acceptance.CancelRequestAcceptance):
    def __init__(self):
        super(ProvideFeedback, self).__init__()

    def provide_feedback(self, decision, comment):
        try:

            time.sleep(2)
            self.web_element_click_id(page_elements.grid_actions['provide_feedback'])

            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.web_element_click_xpath(decision)
            self.web_element_send_keys_xpath(page_elements.interview['rating_1'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_1'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['rating_2'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_2'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['overall_comment'], comment)

        except Exception as error:
            ui_logger.error(error)
