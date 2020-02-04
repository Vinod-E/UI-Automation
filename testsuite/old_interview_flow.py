from scripts.crpo.old_interview_flow import re_schedule


class OldInterviewFlow(re_schedule.ReSchedule):
    def __init__(self):
        super(OldInterviewFlow, self).__init__()

        # ------------- Login session ------------------------
        self.crpo_login()

    def schedule_re_schedule(self):
        print("***== Schedule / Re-Schedule ==***")
        self.interview_schedule()
        self.interview_re_schedule()


ob = OldInterviewFlow()
ob.schedule_re_schedule()
