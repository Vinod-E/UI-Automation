import config
from logger_settings import api_logger


def screen_shot(self, image_name):
    try:
        self.driver.save_screenshot(config.image_config['screen_shot'].format(image_name))
    except Exception as image_error:
        api_logger.error(image_error)
