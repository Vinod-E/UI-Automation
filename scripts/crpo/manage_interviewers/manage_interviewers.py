import time
import page_elements
from logger_settings import ui_logger
from scripts.crpo.manage_interviewers import criteria_configuration


class ManageInterviewers(criteria_configuration.CriteriaConfig):
    def __init__(self):
        super(ManageInterviewers, self).__init__()

        self.panel_skill11_search = ''
        self.skill1_interviewer_status = ''
        self.panel_skill12_search = ''
        self.skill2_interviewer_status = ''

    def skill1_filter(self):
        try:
            self.driver.execute_script("window.scrollTo(0,-200);")
            self.web_element_click_xpath(page_elements.tabs['manage_nominations'])
            time.sleep(0.5)

            self.nomination_validation()
            if self.nomination_validation_check == 'True':
                print('**-------->>> Mail and configuration to invite interviewers successfully')

            time.sleep(0.5)
            self.web_element_send_keys_xpath(page_elements.manage_interviews['panel_search'], self.xl_skill1_mi)

            time.sleep(0.5)
            self.web_element_text_xpath(page_elements.manage_interviews['paging'])
            if '1-1' in self.text_value:
                self.panel_skill11_search = 'Pass'
                print('**-------->>> Panel1 search is working')

            self.web_element_text_xpath(page_elements.title['title'].format('Pending'))
            if self.text_value == 'Pending':
                self.skill1_interviewer_status = 'Pass'
                print('**-------->>> Interviewer1 status verified')

        except Exception as error:
            ui_logger.error(error)

    def skill2_filter(self):
        try:
            time.sleep(1)
            self.web_element_send_keys_xpath(page_elements.manage_interviews['panel_search'], self.xl_skill2_mi)

            self.web_element_text_xpath(page_elements.manage_interviews['paging'])
            if '1-1' in self.text_value:
                self.panel_skill12_search = 'Pass'
                print('**-------->>> Panel2 search is working')

            self.web_element_text_xpath(page_elements.title['title'].format('Pending'))
            if self.text_value == 'Pending':
                self.skill2_interviewer_status = 'Pass'
                print('**-------->>> Interviewer2 status verified')
            time.sleep(1)

        except Exception as error:
            ui_logger.error(error)
