from scripts.crpo import crpo_outfile
import time


class CrpoFlow(crpo_outfile.CrpoOutputFile):

    def __init__(self):
        super(CrpoFlow, self).__init__()

    def login(self):
        self.excel_read()
        self.crpo_login()

    def job_role_creation(self):

        self.job_excel_read()
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
        time.sleep(5)

    def requirement_creation(self):

        self.requirement_excel_read()
        self.create_requirement()
        self.req_configuration_tab()
        time.sleep(5)
        self.req_advance_search()

    def test_creation(self):

        self.test_excel_read()
        self.test_advance_search()
        self.clone_test()

    def event_creation(self):

        self.event_excel_read()
        self.create_event()
        self.event_task_configure()


Object = CrpoFlow()
Object.login()
if Object.status_of_login == 'administrator':
    Object.job_role_creation()
    Object.requirement_creation()
    Object.test_creation()
    Object.event_creation()
    Object.output_report()
    Object.over_status()
    Object.browser_close()
else:
    Object.server_connection_error()
    Object.internet_not_available()
    Object.browser_close()
