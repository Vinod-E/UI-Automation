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


Object = NewInterviewFlow()
Object.login()
if Object.status_of_login == 'administrator':
    Object.form_on()
    Object.job_configuration()
    Object.form_off()
    Object.schedule_to_interview()
    Object.configuration_output_report()

Object.overall_status()
Object.browser_close()
