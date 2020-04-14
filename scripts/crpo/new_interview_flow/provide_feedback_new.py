import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.new_interview_flow import schedule_new


class ProvideFeedbackNew(schedule_new.Schedule):
    def __init__(self):
        super(ProvideFeedbackNew, self).__init__()

    def provide_feedback_new(self, comment):
        try:

            self.web_element_click_id(page_elements.grid_actions['provide_feedback'])

            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.web_element_send_keys_xpath(page_elements.new_interview['rating1'], 'Excellent')
            self.web_element_send_keys_xpath(page_elements.new_interview['comment1'], comment)
            self.web_element_send_keys_xpath(page_elements.new_interview['rating2'], 'Good')
            self.web_element_send_keys_xpath(page_elements.new_interview['comment2'], comment)
            self.web_element_send_keys_xpath(page_elements.new_interview['rating3'], 'VeryGood')
            self.web_element_send_keys_xpath(page_elements.new_interview['overall'], comment)

        except Exception as error:
            ui_logger.error(error)
