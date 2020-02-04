import time
import page_elements
from logger_settings import api_logger
from scripts.crpo.old_interview_flow import schedule


class ReSchedule(schedule.Schedule):
    def __init__(self):
        super(ReSchedule, self).__init__()

    def interview_re_schedule(self):
        self.interviewer_login(self.xl_username_int1_o, self.xl_password_int1_o)


