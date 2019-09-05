import provide_feedback
import page_elements
import config
import time
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys


class UpdateFeedback(provide_feedback.OldProvideFeedback):
    def __init__(self):
        super(UpdateFeedback, self).__init__()

    def unlock_feedback(self):
        try:
           pass
        except exceptions.NoSuchElementException as error:
            print error
