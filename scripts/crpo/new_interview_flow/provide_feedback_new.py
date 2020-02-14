import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.new_interview_flow import schedule_new


class ProvideFeedbackNew(schedule_new.Schedule):
    def __init__(self):
        super(ProvideFeedbackNew, self).__init__()

    def provide_feedback_new(self, comment):
        try:

            self.id_element_webdriver_wait(page_elements.grid_actions['provide_feedback'])
            self.id.click()

            time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.x_path_element_webdriver_wait(page_elements.new_interview['rating1'])
            self.xpath.send_keys('Excellent')

            self.x_path_element_webdriver_wait(page_elements.new_interview['comment1'])
            self.xpath.send_keys(comment)

            self.x_path_element_webdriver_wait(page_elements.new_interview['rating2'])
            self.xpath.send_keys('Good')

            self.x_path_element_webdriver_wait(page_elements.new_interview['comment2'])
            self.xpath.send_keys(comment)

            self.x_path_element_webdriver_wait(page_elements.new_interview['rating3'])
            self.xpath.send_keys('VeryGood')

            self.x_path_element_webdriver_wait(page_elements.new_interview['overall'])
            self.xpath.send_keys(comment)

        except Exception as error:
            api_logger.error(error)
