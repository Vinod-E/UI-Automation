import os
path = os.getenv("HOME")

generic_input_path = "%s/PythonProjects/UI Automation/" % path


test_data_file = {
    'credentials_file': generic_input_path + 'testdata/Login_Details.xls',

    'create_job': generic_input_path + 'testdata/Job_details.xls',

    'create_requirement': generic_input_path + 'testdata/requirement_details.xls',

    'clone_test': generic_input_path + 'testdata/test_details.xls',

    'create_event': generic_input_path + 'testdata/event_details.xls'
}
