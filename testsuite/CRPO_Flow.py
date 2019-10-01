from scripts.crpo.Output import crpo_outfile
import time


class CrpoFlow(crpo_outfile.CrpoOutputFile):

    def __init__(self):
        self.New_email_id = raw_input("Email ID :: ")
        super(CrpoFlow, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

    def all_excels(self):
        self.job_excel_read()
        self.requirement_excel_read()
        self.test_excel_read()
        self.event_excel_read()

    def job_role_creation(self):

        self.create_job_role()
        self.selection_process()
        self.feedback_form()
        self.ec_configurations_tab()
        self.task_configurations_tab()
        self.job_automation()
        time.sleep(5)
        self.tag_interview_panel()
        self.tag_requirement()
        time.sleep(5)
        self.un_tag_requirement()
        self.edit_job()
        self.job_advance_search()

    def requirement_creation(self):

        time.sleep(5)
        self.create_requirement()
        time.sleep(2)
        self.req_configuration_tab()
        time.sleep(5)
        self.req_advance_search()

    def test_creation(self):

        self.test_advance_search()
        self.clone_test()

    def event_creation(self):

        # self.create_event()
        time.sleep(5)
        # self.event_task_configure()
        # self.event_test_configure()
        # self.event_owner_configure()
        self.upload_candidates_to_event(self.New_email_id)
        self.view_upload_candidates()
        self.event_change_applicant_status()
        # ------------ Task Assignment ---------------
        self.task_assignment()
        # ------------ Embrace/Pofu app ---------------
        self.pofu_app()
        self.candidate_status()


Object = CrpoFlow()
# --------------- Login ---------------
Object.login()
Object.all_excels()
if Object.status_of_login == 'administrator':

    # ---------- Job creation -----------------
    # Object.job_role_creation()
    # Object.job_output_report()
    # Object.driver.switch_to.window(Object.driver.window_handles[1])
    # Object.driver.close()
    # Object.driver.switch_to.window(Object.driver.window_handles[0])

    # ---------- Req creation -----------------
    # Object.requirement_creation()
    # Object.requirement_output_report()

    # ---------- Test creation -----------------
    # Object.test_creation()
    # Object.test_output_report()

    # ---------- Event creation -----------------
    Object.event_creation()
    Object.event_output_report()
    Object.task_assign_output_report()
    Object.browser_close()

    # --------- Overall test cases status -----------
    Object.overall_status()

else:
    Object.server_connection_error()
    Object.internet_not_available()
    Object.browser_close()
