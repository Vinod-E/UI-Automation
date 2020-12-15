import xlrd
import datetime
import test_data_inputpath
from scripts.crpo.common import common_file


class JobExcelRead(common_file.CommonFile):
    def __init__(self):
        self.start_date_time = datetime.datetime.now()
        super(JobExcelRead, self).__init__()

        # ------------- file reader index -------------------
        workbook = xlrd.open_workbook(test_data_inputpath.crpo_test_data_file['create_job'])
        if self.login_server == 'betaams':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'ams' or self.login_server == 'indiaams':
            self.job_sheet1 = workbook.sheet_by_index(0)
        if self.login_server == 'amsin':
            self.job_sheet1 = workbook.sheet_by_index(1)

        # --------------- Value initialization ----------------
        self.xl_job_name = []
        self.xl_job_desc = []
        self.xl_job_loc = []
        self.xl_job_hm = []
        self.xl_job_bu = []
        self.xl_openings = []
        self.xl_male_diversity = []
        self.xl_female_diversity = []
        self.xl_selection_process = []
        self.xl_interview_stage_01 = []
        self.xl_interview_template_01 = []
        self.xl_interview_stage_02 = []
        self.xl_interview_template_02 = []
        self.xl_interview_stage_03 = []
        self.xl_interview_template_03 = []
        self.xl_tag_interviewers = []
        self.xl_eligibility_criteria = []
        self.xl_ec_stage = []
        self.xl_positive_status = []
        self.xl_negative_status = []
        self.xl_assign_stage_status = []
        self.xl_positive_stage_status_job = []
        self.xl_negative_stage_status_job = []
        self.xl_A1 = []
        self.xl_A1_T1 = []
        self.xl_hop_r_stage = []
        self.xl_hop_r_status = []
        self.xl_hop_e_stage = []
        self.xl_hop_e_status = []
        self.xl_hop_a_stage = []
        self.xl_hop_a_status = []
        self.xl_hop_hr_stage = []
        self.xl_hop_hr_status = []
        self.j_description_u = []
        self.xl_tag_req = []

        self.job_name_sprint_version = []
        self.tag_interviewers = ""

        # ------------- Iterate Excel sheet------------------------
        self.job_excel_read()

    def job_excel_read(self):
        for i in range(1, self.job_sheet1.nrows):
            number = i  # Counting number of rows
            rows = self.job_sheet1.row_values(number)

            if rows[0]:
                self.xl_job_name.append(rows[0])
            if rows[1]:
                self.xl_job_desc.append(rows[1])
            if rows[2]:
                self.xl_job_loc.append(rows[2])
            if rows[3]:
                self.xl_job_hm.append(rows[3])
            if rows[4]:
                self.xl_job_bu.append(rows[4])
            if rows[5]:
                self.xl_openings.append(str(int(rows[5])))
            if rows[6]:
                self.xl_male_diversity.append(str(int(rows[6])))
            if rows[7]:
                self.xl_female_diversity.append(str(int(rows[7])))
            if rows[8]:
                self.xl_selection_process.append((rows[8]))
            if rows[9]:
                self.xl_interview_stage_01.append(rows[9])
            if rows[10]:
                self.xl_interview_template_01.append(rows[10])
            if rows[11]:
                self.xl_interview_stage_02.append(rows[11])
            if rows[12]:
                self.xl_interview_template_02.append(rows[12])
            if rows[13]:
                self.xl_interview_stage_03.append(rows[13])
            if rows[14]:
                self.xl_interview_template_03.append(rows[14])
            if rows[15]:
                self.xl_tag_interviewers.append(rows[15])
            if rows[16]:
                self.xl_eligibility_criteria.append(rows[16])
            if rows[17]:
                self.xl_ec_stage.append(rows[17])
            if rows[18]:
                self.xl_positive_status.append(rows[18])
            if rows[19]:
                self.xl_negative_status.append(rows[19])
            if rows[20]:
                self.xl_assign_stage_status.append(rows[20])
            if rows[21]:
                self.xl_positive_stage_status_job.append(rows[21])
            if rows[22]:
                self.xl_negative_stage_status_job.append(rows[22])
            if rows[23]:
                self.xl_A1.append(rows[23])
            if rows[24]:
                self.xl_A1_T1.append(rows[24])
            if rows[25]:
                self.xl_hop_r_stage.append(rows[25])
            if rows[26]:
                self.xl_hop_r_status.append(rows[26])
            if rows[27]:
                self.xl_hop_e_stage.append(rows[27])
            if rows[28]:
                self.xl_hop_e_status.append(rows[28])
            if rows[29]:
                self.xl_hop_a_stage.append(rows[29])
            if rows[30]:
                self.xl_hop_a_status.append(rows[30])
            if rows[31]:
                self.xl_hop_hr_stage.append(rows[31])
            if rows[32]:
                self.xl_hop_hr_status.append(rows[32])
            if rows[33]:
                self.j_description_u.append(rows[33])
            if rows[34]:
                self.xl_tag_req.append(rows[34])

            for j in self.xl_job_name:
                job_name = j
                self.job_name_sprint_version = job_name.format(self.sprint_version)

            for k in self.xl_tag_interviewers:
                interviewers = k
                self.tag_interviewers = interviewers


# ob = JobExcelRead()
# ob.job_excel_read()
