import config

generic_input_path = config.common_folder_path


crpo_test_data_file = {
    'login_credentials': generic_input_path + 'testdata/Login_Details.xls',

    'create_job': generic_input_path + 'testdata/Job_details.xls',

    'create_requirement': generic_input_path + 'testdata/requirement_details.xls',

    'clone_test': generic_input_path + 'testdata/test_details.xls',

    'create_event': generic_input_path + 'testdata/event_details.xls',

    'old_interview_file': generic_input_path + 'testdata/Old_interview.xls',

    'interview_output_report': generic_input_path + 'reports/UI_Interview_Flow.xls',

    'New_interview_output_report': generic_input_path + 'reports/UI_New_Interview_Flow.xls',

    'Applicant_action_output_report': generic_input_path + 'reports/UI_Applicant_Action_Flow.xls'
}

attachments = {
    'attachment': generic_input_path + 'testdata/job-description.pdf',
    'upload_candidates': generic_input_path + 'testdata/candidateUpload.xls'
}

output = {
    'output_report': generic_input_path + 'reports/UI_CRPO_Flow.xls',
}
