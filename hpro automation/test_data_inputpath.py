import config

generic_input_path = config.common_folder_path
crpo_testdata = 'testdata' + config.slash + 'crpo' + config.slash
crpo_reports = 'reports' + config.slash + 'crpo' + config.slash
rpo_testdata = 'testdata' + config.slash + 'rpo' + config.slash
rpo_reports = 'reports' + config.slash + 'rpo' + config.slash
pofu_testdata = 'testdata' + config.slash + 'embrace' + config.slash
pofu_reports = 'reports' + config.slash + 'embrace' + config.slash


crpo_test_data_file = {
    'login_credentials': generic_input_path + 'testdata' + config.slash + 'Login_Details.xls',

    'create_job': generic_input_path + crpo_testdata + 'Job_details.xls',

    'create_requirement': generic_input_path + crpo_testdata + 'requirement_details.xls',

    'clone_test': generic_input_path + crpo_testdata + 'test_details.xls',

    'create_event': generic_input_path + crpo_testdata + 'event_details.xls',

    'old_interview_file': generic_input_path + crpo_testdata + 'Old_interview.xls',

    'new_interview_file': generic_input_path + crpo_testdata + 'New_interview.xls',

    'live_interview_file': generic_input_path + crpo_testdata + 'Live_interview.xls',

    'applicant_action_file': generic_input_path + crpo_testdata + 'Applicants_actions.xls',

    'help_desk': generic_input_path + crpo_testdata + 'Help_desk.xls',

    'create_form': generic_input_path + pofu_testdata + 'create_form.xls'
}

attachments = {
    'attachment': generic_input_path + crpo_testdata + 'job-description.pdf',
    'upload_candidates': generic_input_path + crpo_testdata + 'candidateUpload.xls',
    'query': generic_input_path + crpo_testdata + 'UI_Automation.jpg'
}

output = {
    'output_report': generic_input_path + crpo_reports + 'UI_CRPO_Flow.xls',
    'old_int_report': generic_input_path + crpo_reports + 'UI_Interview_Flow_old.xls',
    'live_int_report': generic_input_path + crpo_reports + 'UI_Interview_Flow_live.xls',
    'new_int_report': generic_input_path + crpo_reports + 'UI_Interview_Flow_new.xls',
    'Applicant_action_output_report': generic_input_path + crpo_reports + 'UI_Applicant_Action_Flow.xls',
    'help_desk_output_report': generic_input_path + crpo_reports + 'UI_Help_Desk_Flow.xls',
    'form_creation_output_report': generic_input_path + pofu_reports + 'UI_form_creation_flow.xls',
}
