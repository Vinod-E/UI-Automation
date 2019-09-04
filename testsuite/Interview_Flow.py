from scripts.crpo import Interview_output


class InterviewFlow(Interview_output.InterviewOutputFile):

    def __init__(self):
        super(InterviewFlow, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

    def schedule_re_schedule(self):
        print "***== Schedule / Re-Schedule ==***"
        self.old_interview_excel_read()
        self.event_applicant_schedule()
        self.re_schedule()

    def cancel_request_cancel(self):
        print "***== Cancel / Cancellation Request ==***"
        self.cancel_interview()
        self.schedule_again()
        self.cancel_interview_request()
        self.cancel_request_acceptance()

    def provide_feedback_flow(self):
        print "***== Interview Flow ==***"
        self.interviewer_login()
        self.provide_feedback()


Object = InterviewFlow()
# --------------- Login ---------------
Object.login()
if Object.status_of_login == 'administrator':

    Object.schedule_re_schedule()
    Object.cancel_request_cancel()
    Object.int1_output_report()
    Object.int2_output_report()
    Object.admin_output_report()

    Object.provide_feedback_flow()
    Object.provide_feedback_output_report()

Object.overall_status()
