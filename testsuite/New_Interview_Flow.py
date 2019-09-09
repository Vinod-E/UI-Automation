from scripts.crpo import New_interview_output


class NewInterviewFlow(New_interview_output.InterviewOutputFile):
    def __init__(self):
        super(NewInterviewFlow, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

    def form_on(self):
        self.settings_on()

    def job_configuration(self):
        self.jobrole_search()
        self.new_feedback_form()

    def form_off(self):
        self.settings_off()

    def schedule_to_interview(self):
        self.event_applicant_schedule_to_new_form_stage()

    def new_provide_feedback(self):
        self.interviewer_login_details()
        self.login_int1()
        self.new_save_draft_int1()
        self.new_provide_feedback_int1()

        self.login_int2()
        self.new_provide_feedback_int2()

    def new_update_feedback(self):
        self.update_feedback_and_decision()


Object = NewInterviewFlow()
Object.login()
if Object.status_of_login == 'administrator':
    Object.form_on()
    Object.job_configuration()
    Object.form_off()
    Object.schedule_to_interview()
    Object.configuration_output_report()

    Object.new_provide_feedback()
    Object.provide_feedback_output_report()

    Object.new_update_feedback()
    Object.new_update_feedback_output_report()

Object.overall_status()
Object.browser_close()
