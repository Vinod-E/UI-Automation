from scripts.crpo.old_interview_flow import cancel_interview_old


class OldInterviewFlow(cancel_interview_old.CancelInterview):
    def __init__(self):
        super(OldInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def schedule_re_schedule(self):
        print("***== Schedule / Re-Schedule ==***")
        self.interview_schedule()
        self.interview_re_schedule()

    def cancel_interviews(self):
        print("***== Cancel / Cancellation Request ==***")
        self.cancel_interview()


ob = OldInterviewFlow()
ob.schedule_re_schedule()
ob.cancel_interviews()
