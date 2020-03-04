import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.applicant_actions import job_applicants


class JobApplicantActions(job_applicants.JobApplicants):
    def __init__(self):
        super(JobApplicantActions, self).__init__()

        self.ui_change_applicant_status_action_aj = []
        self.ui_compose_mail_aj = []
        self.ui_untag_applicant_aj = []
        self.ui_view_registration_link_aj = []
        self.ui_manage_task_aj = []
        self.ui_view_test_status_aj = []
        self.ui_single_pdf_aj = []
        self.ui_email_mobile_aj = []
        self.ui_send_admit_card_aj = []

    def job_change_applicant_status(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.check_box()
            # --------------------------- Change Applicant Status -------------------
            self.job_applicant_status_change(self.xl_stage_a, self.xl_status_a, self.xl_comment_a)
            self.glowing_messages('Applicant status changed successfully for selected Applicant(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_change_applicant_status_action_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_compose_mail(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.check_box()
            # ----------------------------- Compose Mail ---------------------
            self.web_element_click_id(page_elements.applicant_actions['compose_mail'])
            self.web_element_send_keys_xpath(page_elements.event_applicant['subject'], self.xl_mail_description_a)
            self.web_element_send_keys_xpath(page_elements.event_applicant['description'], self.xl_mail_description_a)
            self.web_element_click_xpath(page_elements.buttons['clone/save'])
            self.glowing_messages('Mail will be send asynchronously')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_compose_mail_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_untag_applicant(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            # ----------------------------- Untag applicants ---------------------
            self.web_element_click_id(page_elements.applicant_actions['untag_applicants'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Unable to untag candidate, beacuse candidate is moved in the Event and Job')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_untag_applicant_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_copy_registration_link(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.check_box()
            # ----------------------------- View Registration Link ----------------------------
            self.web_element_click_id(page_elements.applicant_actions['copy_registration_link'])
            self.web_element_click_xpath(page_elements.buttons['copy'])
            self.glowing_messages('Registration link copied')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_view_registration_link_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_manage_task(self):
        try:
            self.task_validation_check = ''
            time.sleep(2)
            self.job_more_actions()
            # ----------------------------- Manage Task ---------------------
            self.web_element_click_xpath(page_elements.applicant_actions['view_registration_link'])
            time.sleep(4)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.manage_task_validation(self._applicant_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------------------- output report value ----------------
            if self.task_validation_check == 'True':
                self.ui_manage_task_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_view_test_status(self):
        try:
            time.sleep(2)
            self.job_more_actions()
            # ----------------------------- Test status ---------------------
            self.web_element_click_xpath(page_elements.applicant_actions['job_test_status'])
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['close_pop_details_window'])
            # -------------------- output report value ----------------
            self.ui_view_test_status_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_generate_single_pdf(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.job_more_actions()
            # ----------------------------- Single PDF ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['job_single_pdf'])
            self.glowing_messages('Your request is being processed, please check the status in Background Task details')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_single_pdf_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def email_mobile_verification_link(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.job_more_actions()
            # ----------------------------- Single PDF ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['single_pdf'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Email Sent Successfully')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_email_mobile_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def job_admit_card(self):
        try:
            self.message_validation = ''
            time.sleep(2)
            self.job_more_actions()
            # ----------------------------- Change BU ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['job_send_admit_card'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Reason'),
                                             self.xl_reason_admit_card_a)
            self.drop_down_selection()
            self.web_element_send_keys_xpath(page_elements.event_applicant['comment'], self.xl_comment_a)
            self.web_element_click_xpath(page_elements.buttons['send'])
            self.glowing_messages('Admit-Card successfully sent to applicants(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_send_admit_card_aj = 'Pass'
        except Exception as e:
            api_logger.error(e)
