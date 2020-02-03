import xlrd
import test_data_inputpath
from scripts.crpo.assessment import clone_assessment


class EventExcelRead(clone_assessment.CloneAssessment):
    def __init__(self):
        super(EventExcelRead, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_event'])
        if self.login_server == 'betaams':
            self.event_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams':
            self.event_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.event_sheet1 = workbook.sheet_by_index(1)

        # ------------ Candidate file reader ------------
        workbook1 = xlrd.open_workbook(test_data_inputpath.attachments['upload_candidates'])
        self.upload_sheet = workbook1.sheet_by_index(0)

        # --------------- Value initialization ----------------
        self.xl_event_name = []
        self.xl_req_name = []
        self.xl_job_name = []
        self.xl_slot = []
        self.xl_em = []
        self.xl_college = []
        self.xl_stage_status = []
        self.xl_positive_stage_status_Event = []
        self.xl_activity = []
        self.xl_task1 = []
        self.xl_task2 = []
        self.xl_task3 = []
        self.xl_task4 = []
        self.xl_event_test_name = []
        self.xl_event_test_stage = []
        self.xl_hopping_positive_status = []
        self.xl_hopping_negative_status = []
        self.xl_change_applicant_stage = []
        self.xl_change_applicant_status = []
        self.xl_change_status_comment = []
        self.xl_upload_candidate_name = []
        self.xl_call_back_status = []
        self.xl_total_tasks = []
        self.xl_completed_tasks = []
        self.xl_pending_tasks = []
        self.xl_submitted_tasks = []
        self.xl_rejected_tasks = []

        self.event_sprint_version = []
        self.job_name_sprint_version = []
        self.req_name_sprint_version = []
        self.event_test_sprint_version = []

        self.hopping_positive_status = ""
        self.change_applicant_status = ""
        self.call_back_status = ""
        self.total_tasks = ""
        self.completed_tasks = ""
        self.pending_tasks = ""
        self.submitted_tasks = ""
        self.rejected_tasks = ""

        # ------------- Iterate Excel sheet------------------------
        self.event_excel_read()

    def event_excel_read(self):
        # --------------------------------------candidate details-------------------------------------------------------
        for i in range(1, self.upload_sheet.nrows):
            number = i  # Counting number of rows
            rows = self.upload_sheet.row_values(number)

            if rows[0]:
                self.xl_upload_candidate_name.append(rows[0])
            for s in self.xl_upload_candidate_name:
                self.event_sprint_version = s
        # --------------------------------------Event details-----------------------------------------------------------
        for i in range(1, self.event_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.event_sheet1.row_values(number)

            if rows[0]:
                self.xl_event_name.append(rows[0])
            if rows[1]:
                self.xl_req_name.append(rows[1])
            if rows[2]:
                self.xl_job_name.append(str(rows[2]))
            if rows[3]:
                self.xl_slot.append(str(rows[3]))
            if rows[4]:
                self.xl_em.append(str(rows[4]))
            if rows[5]:
                self.xl_college.append(str(rows[5]))
            if rows[6]:
                self.xl_stage_status.append(str(rows[6]))
            if rows[7]:
                self.xl_positive_stage_status_Event.append(str(rows[7]))
            if rows[8]:
                self.xl_activity.append(str(rows[8]))
            if rows[9]:
                self.xl_task1.append(str(rows[9]))
            if rows[10]:
                self.xl_task3.append(str(rows[10]))
            if rows[11]:
                self.xl_task2.append(str(rows[11]))
            if rows[12]:
                self.xl_task4.append(str(rows[12]))
            if rows[13]:
                self.xl_event_test_name.append(str(rows[13]))
            if rows[14]:
                self.xl_event_test_stage.append(str(rows[14]))
            if rows[15]:
                self.xl_hopping_positive_status.append(str(rows[15]))
            if rows[16]:
                self.xl_hopping_negative_status.append(str(rows[16]))
            if rows[17]:
                self.xl_change_applicant_stage.append(str(rows[17]))
            if rows[18]:
                self.xl_change_applicant_status.append(str(rows[18]))
            if rows[19]:
                self.xl_change_status_comment.append(str(rows[19]))
            if rows[20]:
                self.xl_call_back_status.append(str(rows[20]))
            if rows[21]:
                self.xl_total_tasks.append(int(rows[21]))
            if rows[22]:
                self.xl_completed_tasks.append(int(rows[22]))
            if rows[23]:
                self.xl_pending_tasks.append(int(rows[23]))
            if rows[24]:
                self.xl_submitted_tasks.append(int(rows[24]))
            if rows[25]:
                self.xl_rejected_tasks.append(int(rows[25]))

            for j in self.xl_event_name:
                event_name = j
                self.event_sprint_version = event_name.format(self.sprint_version)

            for k in self.xl_req_name:
                req_name = k
                self.req_name_sprint_version = req_name.format(self.sprint_version)

            for m in self.xl_job_name:
                job_name = m
                self.job_name_sprint_version = job_name.format(self.sprint_version)

            for v in self.xl_event_test_name:
                test_name = v
                self.event_test_sprint_version = test_name.format(self.sprint_version)

            for x in self.xl_hopping_positive_status:
                self.hopping_positive_status = x
            for y in self.xl_change_applicant_status:
                self.change_applicant_status = y
            for z in self.xl_call_back_status:
                self.call_back_status = z
            for a in self.xl_total_tasks:
                self.total_tasks = a
            for b in self.xl_pending_tasks:
                self.pending_tasks = b
            for c in self.xl_completed_tasks:
                self.completed_tasks = c
            for d in self.xl_submitted_tasks:
                self.submitted_tasks = d
            for e in self.xl_rejected_tasks:
                self.rejected_tasks = e
