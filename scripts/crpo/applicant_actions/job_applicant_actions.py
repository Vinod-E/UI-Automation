import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.applicant_actions import job_applicants


class JobApplicantActions(job_applicants.JobApplicants):
    def __init__(self):
        super(JobApplicantActions, self).__init__()
