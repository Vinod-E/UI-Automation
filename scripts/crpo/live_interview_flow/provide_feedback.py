import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.common import button_click
from scripts.crpo.live_interview_flow import live_interview_excel


class ProvideFeedback(live_interview_excel.LiveInterviewExcelRead):
    def __init__(self):
        super(ProvideFeedback, self).__init__()

    def live_provide_feedback(self, decision, comment):
        try:
            time.sleep(1)
            self.web_element_click_xpath(page_elements.live_interview['provide_feedback'])

            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.web_element_click_xpath(decision)
            self.web_element_send_keys_xpath(page_elements.interview['rating_1'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_1'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['rating_2'], 'Develop')
            self.web_element_send_keys_xpath(page_elements.interview['comment_2'], comment)
            self.web_element_send_keys_xpath(page_elements.interview['overall_comment'], comment)

            if self.is_behalf_int == 1:
                button_click.all_buttons(self, self.xl_int1_name[0])
                button_click.all_buttons(self, self.xl_int2_name[0])

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
