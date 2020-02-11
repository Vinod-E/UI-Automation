import datetime
from scripts.crpo.old_interview_flow import submit_feedback_old


class OldInterviewFlow(submit_feedback_old.SubmittedFeedback):
    def __init__(self):
        super(OldInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def schedule_re_schedule(self):
        print('<<<<<<<<<<<<<<<<<<<<<<< Schedule / Re-Schedule >>>>>>>>>>>>>>>>>>>>>>>>>>')
        self.interview_schedule()
        self.interview_re_schedule()

    def cancel_interviews(self):
        print('<<<<<<<<<<<<<<<<<<<<< Cancel / Cancellation Request >>>>>>>>>>>>>>>>>>>>>>')
        self.cancel_interview()
        self.interview_schedule()
        self.cancel_interview_request()
        self.cancel_request_acceptance()

    def provide_feedback_flow(self):
        print('<<<<<<<<<<<<<<<<<<<<<<< Draft / Partial / Feedback >>>>>>>>>>>>>>>>>>>>>>')
        self.interview_schedule()
        self.save_as_draft_old()
        self.partial_feedback()
        self.submitted_feedback()
        print("Run completed at:: " + str(datetime.datetime.now()))


ob = OldInterviewFlow()
ob.schedule_re_schedule()
ob.cancel_interviews()
ob.provide_feedback_flow()
