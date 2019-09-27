from scripts.crpo.Output import Applicant_actions_output


class ApplicantActionsFlow(Applicant_actions_output.ApplicantActionOutput):

    def __init__(self):
        self.last_version_number = raw_input('Last Version number :: ')
        super(ApplicantActionsFlow, self).__init__()

    def all_excels(self):
        self.excel_read()

    def login_crpo(self):
        self.crpo_login()

    def event_applicant_actions(self):
        self.event_advance_search()
        self.event_get_by_id()
        self.event_applicants()
        self.change_applicant_status()
        self.candidate_get_by_id('Shortlisted')
        self.compose_mail()
        self.candidate_tab(self.last_version_number)
        self.applicant_advance_search(self.last_version_number)


Actions = ApplicantActionsFlow()
# --------------- Login ---------------
Actions.all_excels()
Actions.login_crpo()

if Actions.status_of_login == 'administrator':

    # ---------- Event Applicants -----------------
    Actions.event_applicant_actions()
    Actions.event_applicant_action_report()

    # --------- Overall test cases status -----------
    Actions.overall_status()

else:
    Actions.server_connection_error()
    Actions.internet_not_available()
    Actions.browser_close()


