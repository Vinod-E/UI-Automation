from scripts.crpo.Output import Applicant_actions_output


class ApplicantActionsFlow(Applicant_actions_output.ApplicantActionOutput):

    def __init__(self):
        self.last_version_number = raw_input('Last Version number :: ')
        super(ApplicantActionsFlow, self).__init__()
        self.new_candidate_name = self.sprint_version
        self.old_candidate_name = 'Sprint_{}'.format(self.last_version_number)

    def all_excels(self):
        self.excel_read()

    def login_crpo(self):
        self.crpo_login()

    def candidates_tab(self):
        self.candidate_tab(self.old_candidate_name)
        self.candidate_tag_to_event()

    def event_applicant_actions(self):
        self.event_advance_search()
        self.event_get_by_id()

        self.event_applicants(self.new_candidate_name)
        self.event_change_applicant_status()
        self.candidate_get_by_id('Shortlisted')

        self.event_compose_mail()

        self.event_send_sms()
        self.reset_applicant_search()

        self.tag_to_job(self.last_version_number)
        self.candidate_get_by_id(self.old_candidate_name)


Actions = ApplicantActionsFlow()
# --------------- Login ---------------
Actions.all_excels()
Actions.login_crpo()

if Actions.status_of_login == 'administrator':

    # ----------- Candidates -------------------
    Actions.candidates_tab()
    Actions.candidate_tab_report()

    # ---------- Event Applicants -----------------
    Actions.event_applicant_actions()
    Actions.event_applicant_action_report()

    # --------- Overall test cases status -----------
    Actions.overall_status()

else:
    Actions.server_connection_error()
    Actions.internet_not_available()
    Actions.browser_close()


