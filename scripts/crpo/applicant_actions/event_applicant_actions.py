import time
import page_elements
import test_data_inputpath
from logger_settings import api_logger
from selenium.webdriver.common.keys import Keys
from scripts.crpo.applicant_actions import event_applicants


class ApplicantActions(event_applicants.ApplicantActions):
    def __init__(self):
        super(ApplicantActions, self).__init__()
        self._applicant_name = 'Sprint{}'.format(self.sprint_version)
        self.attachment = test_data_inputpath.attachments['attachment']

        self.ui_change_applicant_status_action_ae = []
        self.ui_send_sms_ae = []
        self.ui_compose_mail_ae = []
        self.ui_tag_applicant_ae = []
        self.ui_untag_applicant_ae = []
        self.ui_send_registration_link_ae = []
        self.ui_send_admit_card_ae = []
        self.ui_view_registration_link_ae = []
        self.ui_manage_task_ae = []
        self.ui_view_test_status_ae = []
        self.ui_download_resume_ae = []
        self.ui_single_pdf_ae = []
        self.ui_generate_docket_ae = []
        self.ui_compare_id_ae = []
        self.ui_upload_attachment_ae = []
        self.ui_change_business_unit_ae = []
        self.ui_view_applicant_json_ae = []
        self.ui_disable_registration_link_ae = []
        self.ui_enable_registration_link_ae = []
        self.ui_re_registration_link_ae = []

    def event_change_applicant_status(self):
        try:
            self.driver.execute_script("window.scrollTo(0,100);")
            time.sleep(1)
            self.check_box()
            # --------------------------- Change Applicant Status -------------------
            self.applicant_status_change(self.xl_stage_a, self.xl_status_a, self.xl_comment_a)
            self.glowing_messages('Applicant status changed successfully for selected Applicant(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_change_applicant_status_action_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def compose_mail(self):
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
                self.ui_compose_mail_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def send_sms(self):
        try:
            self.message_validation = ''
            # ----------------------------- Compose Mail ---------------------
            self.web_element_click_id(page_elements.applicant_actions['send_sms'])
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Select Template'),
                                             self.xl_sms_template_a)
            self.drop_down_selection()
            self.web_element_click_xpath(page_elements.buttons['send_sms'])
            self.glowing_messages('SMS sent successfully')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_send_sms_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def tag_applicants_to_job_test(self):
        try:
            self.message_validation = ''
            # ----------------------------- Tag applicants ---------------------
            self.web_element_click_id(page_elements.applicant_actions['tag_applicants'])
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Select a JobRole'),
                                             self.event_sprint_version_a)
            self.drop_down_selection()
            time.sleep(1)
            self.web_element_click_xpath(page_elements.grid['test_required'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Select Test'),
                                             self.event_sprint_version_a)
            self.drop_down_selection()
            self.web_element_click_xpath(page_elements.buttons['tag_applicant_event'])
            self.glowing_messages('All Applicant(s) tagged successfully')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_tag_applicant_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def untag_applicant(self):
        try:
            self.message_validation = ''
            self.check_box()
            time.sleep(1)
            # ----------------------------- Untag applicants ---------------------
            self.web_element_click_id(page_elements.applicant_actions['untag_applicants'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Unable to untag candidate, beacuse candidate is moved in the Event and Job')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_untag_applicant_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def registration_link(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Registration Link ---------------------
            self.web_element_click_xpath(page_elements.applicant_actions['registration_link'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Registration-Link successfully sent to applicants(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_send_registration_link_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def admit_card(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Admit Card ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['send_admit_card'])
            self.web_element_click_xpath(page_elements.buttons['ok'])
            self.glowing_messages('Admit-Card successfully sent to applicants(s)')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_send_admit_card_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def view_registration_link(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- View Registration Link ----------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['view_registration_link'])
            self.web_element_click_xpath(page_elements.buttons['copy'])
            self.glowing_messages('Registration link copied')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_view_registration_link_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def manage_task(self):
        try:
            time.sleep(2)
            self.more_actions()
            # ----------------------------- Manage Task ---------------------
            self.web_element_click_xpath(page_elements.applicant_actions['manage_task'])
            time.sleep(4)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.manage_task_validation(self.event_sprint_version_a)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            # -------------------- output report value ----------------
            if self.task_validation_check == 'True':
                self.ui_manage_task_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def view_test_status(self):
        try:
            time.sleep(2)
            self.more_actions()
            # ----------------------------- Test status ---------------------
            self.web_element_click_xpath(page_elements.applicant_actions['view_test_status'])
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['close_pop_details_window'])
            # -------------------- output report value ----------------
            self.ui_view_test_status_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def download_resume(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Download Resume ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['download_resume'])
            self.glowing_messages('Resumes Not found')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_download_resume_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def generate_single_pdf(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Single PDF ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['single_pdf'])
            self.glowing_messages('Your request is being processed, please check the status in Background Task details')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_single_pdf_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def generate_docket(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Generate Docket ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['docket'])
            self.glowing_messages('Your request is being processed, please check the status in Background Task details')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_generate_docket_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def compare_id_card(self):
        try:
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Compare Id card ----------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['compare_id'])
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['close_pop_details_window'])
            # -------------------- output report value ----------------
            self.ui_compare_id_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def upload_attachment(self):
        try:
            self.message_validation = ''
            time.sleep(2)
            self.more_actions()
            # ----------------------------- Upload attachment ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['upload_attachment'])
            self.driver.find_element_by_xpath(page_elements.file['upload_file']).send_keys(self.attachment)
            time.sleep(2)
            self.glowing_messages('File uploaded successfully')
            self.dismiss_message()
            time.sleep(0.5)
            self.web_element_click_xpath(page_elements.buttons['create-save'])
            self.message_validation = ''
            time.sleep(2)
            self.glowing_messages('Attachment Upload Successfully')
            self.dismiss_message()
            self.web_element_click_xpath(page_elements.buttons['close_pop_details_window'])

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_upload_attachment_ae = 'Pass'

        except Exception as e:
            api_logger.error(e)

    def change_business_unit(self):
        try:
            self.message_validation = ''
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Change BU ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['change_bu/re_RL'])
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['create-save'])
            self.glowing_messages('Applicant updated successfully')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_change_business_unit_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def applicant_json(self):
        try:
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Applicant json ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['applicant_json'])
            time.sleep(1)
            self.web_element_click_xpath(page_elements.buttons['close_pop_details_window'])
            # -------------------- output report value ----------------
            self.ui_view_applicant_json_ae = 'Pass'
            time.sleep(2)
        except Exception as e:
            api_logger.error(e)

    def disable_registration_link(self):
        try:
            time.sleep(1)
            self.more_actions()
            # ----------------------------- Disable RL ---------------------
            time.sleep(1)
            self.web_element_click_xpath(page_elements.applicant_actions['disable/enable_registration_link'])

            time.sleep(2)
            self.more_actions()
            self.disable_link_validation()
            # -------------------- output report value ----------------
            if self.disable_link_validation_check == 'True':
                self.ui_disable_registration_link_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def enable_registration_link(self):
        try:
            time.sleep(2)
            self.more_actions()
            # ----------------------------- Enable RL ---------------------
            time.sleep(1)
            self.web_element_click_xpath(page_elements.applicant_actions['disable/enable_registration_link'])

            time.sleep(2)
            self.more_actions()
            self.enable_link_validation(self.event_sprint_version_a)
            # -------------------- output report value ----------------
            if self.enable_link_validation_check == 'True':
                self.ui_enable_registration_link_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def re_registration_link(self):
        try:
            self.message_validation = ''
            time.sleep(2)
            self.applicant_name_search(self._applicant_name, 'Applicant grid')
            self.more_actions()
            # ----------------------------- Change BU ------------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['change_bu/re_RL'])
            self.web_element_send_keys_xpath(page_elements.text_fields['text_field'].format('Reason'),
                                             self.xl_enable_link_a)
            self.xpath.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            self.web_element_send_keys_xpath(page_elements.event_applicant['comment'], self.xl_comment_a)
            self.web_element_click_xpath(page_elements.buttons['send'])
            self.glowing_messages('Re-Registration has been enabled for this user')
            time.sleep(2)
            self.dismiss_message()

            # -------------------- output report value ----------------
            if self.message_validation == 'True':
                self.ui_re_registration_link_ae = 'Pass'
        except Exception as e:
            api_logger.error(e)

    def fill_registration(self):
        try:
            time.sleep(1)
            self.more_actions()
            # ----------------------------- View Registration Link ----------------------------
            self.web_element_click_xpath(page_elements.applicant_actions['view_registration_link'])
            self.web_element_click_xpath(page_elements.event_applicant['open_RL_new_tab'])
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.web_element_click_id(page_elements.microSite['yes'])
            self.web_element_click_id(page_elements.microSite['declaration'])
            self.web_element_click_id(page_elements.microSite['submit'])
            time.sleep(3)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.web_element_click_xpath(page_elements.buttons['done'])
        except Exception as e:
            api_logger.error(e)
