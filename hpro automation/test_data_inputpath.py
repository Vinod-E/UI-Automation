import os
path = os.getenv("HOME")

generic_input_path = "%s/hirepro_automation/UI-Automation/" % path


crpo_test_data_file = {
    'credentials_file': generic_input_path + 'testdata/Login_Details.xls',

    'create_job': generic_input_path + 'testdata/Job_details.xls',

    'create_requirement': generic_input_path + 'testdata/requirement_details.xls',

    'clone_test': generic_input_path + 'testdata/test_details.xls',

    'create_event': generic_input_path + 'testdata/event_details.xls',

    'output_report': generic_input_path + 'reports/UI_CRPO_Flow.xls'
}
