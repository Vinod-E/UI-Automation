import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import cancel_request_acceptance


class ProvideFeedback(cancel_request_acceptance.CancelRequestAcceptance):
    def __init__(self):
        super(ProvideFeedback, self).__init__()

    def provide_feedback(self, decision, comment):
        try:

            self.id_element_webdriver_wait(page_elements.grid_actions['provide_feedback'])
            self.id.click()

            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(decision)
            self.xpath.click()

            self.x_path_element_webdriver_wait(page_elements.interview['rating_1'])
            self.xpath.send_keys('Develop')

            self.x_path_element_webdriver_wait(page_elements.interview['comment_1'])
            self.xpath.send_keys(comment)

            self.x_path_element_webdriver_wait(page_elements.interview['rating_2'])
            self.xpath.send_keys('Develop')

            self.x_path_element_webdriver_wait(page_elements.interview['comment_2'])
            self.xpath.send_keys(comment)

            self.x_path_element_webdriver_wait(page_elements.interview['overall_comment'])
            self.xpath.send_keys(comment)

        except Exception as error:
            api_logger.error(error)
