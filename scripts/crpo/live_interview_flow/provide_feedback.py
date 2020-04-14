import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.live_interview_flow import live_interview_excel


class ProvideFeedback(live_interview_excel.LiveInterviewExcelRead):
    def __init__(self):
        super(ProvideFeedback, self).__init__()

    def live_provide_feedback(self, decision, comment):
        try:

            self.web_element_click_xpath(page_elements.live_interview['provide_feedback'])

            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.web_element_click_xpath(decision)
            self.web_element_send_keys_xpath(page_elements.interview['rating_1'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_1'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['rating_2'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_2'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['overall_comment'], comment)

        except Exception as error:
            ui_logger.error(error)
