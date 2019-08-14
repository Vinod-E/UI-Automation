
login = {

    # ------------------------------------------Login details-----------------------------------------------------------
    'tenant_alias_page': '//*[@id="mainBodyElement"]/div[6]/div/div/div[1]/h4',
    'tenant': "alias",
    'next_button': '//*[@id="mainBodyElement"]/div[6]/div/div/form/div[2]/button',
    'username': "loginName",
    'password': '//*[@type="password"]',
    'login_button': '//*[@ng-click="vm.login()"]',
    'login_success': '//*[@id="mainBodyElement"]/div[1]/div/header/div[1]/nav/div/div[3]/span',
    'tenant_screen_text': '//*[@id="mainBodyElement"]/div[6]/div/div/div[1]/h4',
    'page_cant_be_reached': '//*[@id="main-message"]/h1/span',
    'internet_error': '//*[@id="main-message"]/h1/span',
    'wrong_credentials': '//*[@id="mainBodyElement"]/div[1]/div/header/div[3]/div/div'
}

job = {
    # --------------------------------------------Job Role--------------------------------------------------------------
    'job_tab': '//*[@ui-sref="crpo.jobRole"]',

    'create_job_role': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[2]/a',

    'Job_name': '//*[@placeholder="Name"]',

    'upload_job_file': '//*[@type="file"]',

    'job_description': '//*[@id="mainBodyElement"]/div[3]'
                       '/section/div/basic-job/div/div[2]/div[8]/div/wysiwyg-edit/div/div[2]/iframe',

    'job_location': '//*[@placeholder="Location"][@type="text"]',

    'job_hiring_manager': '//*[@placeholder="Hiring Manager"][@type="text"]',

    'job_business_unit': '//*[@placeholder="Business Unit"][@type="text"]',

    'job_openings': 'openings',

    'job_male_diversity': '//*[@placeholder="Male"]',

    'job_female_diversity': '//*[@placeholder="Female"]',

    'job_create_button': '//*[@id="mainBodyElement"]/div[3]/section/div/basic-job/div/div[3]/div/button[2]',

    'job_cancel_button': '//*[@id="mainBodyElement"]/div[3]/section/div/basic-job/div/div[3]/div/button[1]',

    'duplicate_job': '//*[@id="mainBodyElement"]/div[1]/div/header/div[2]/div/div',

    'jobrole_breadcrumbs': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/span',

    'Floating_actions': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/floating-actions/span/span/i',

    # -------------------------------------- Floating actions ---------------------------------------------------------
    'getbyid_menu_selection_process': '//*[@title="Selection Process"]',

    'getbyid_menu_selectionProcess_text_field': '//*[@type="text"][@placeholder="Selection Process"]',

    'getbyid_menu_selectionProcess_save': '//*[@type="button"][@ng-click="vm.tagSelectionProcess();"]',

    'getbyid_menu_feedback_form': '//*[@title="Configure Feedback Form"]',

    'getbyid_menu_edit_job': '//*[@title="Edit"]',

    'getbyid_menu_tag_requirement': '//*[@title="Tag To Requirement"]',

    'getbyid_menu_tag_requirement_field': '//*[@type="text"][@placeholder="Requirements"]',

    'getbyid_menu_tag_requirement_button': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/button[2]',

    'getbyid_menu_untag_requirement': '//*[@title="Untag Requirement"]',

    'getbyid_menu_untag_requirement_ok': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/div[1]',
    # ------------------------------------------------------------------------------------------------------------------

    'getbyid_feedback_form_configure': '//*[@type="text"][@placeholder="Interview Stages"]',

    'getbyid_feedback_from_name_search': '//*[@placeholder="Name like."][@type="text"]',

    'getbyid_feedback_from_search_button': '//*[@ng-click="vm.service.templates.search();"][@type="submit"]',

    'getbyid_feedback_form_use': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]'
                                 '/div/div/interview-templates-search/div/accordian-row-table/table/tbody'
                                 '/tr/td[3]/div/span[1]',

    'Resolution_Strategy': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]'
                           '/div/table/tbody/tr[1]/td[2]/div/label[2]',

    'overall_comment_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]'
                              '/div/table/tbody/tr[2]/td[2]/div/label[1]',

    'interview_reject_comment_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div/'
                                       'div[1]/div[2]/div/table/tbody/tr[3]/td[2]/div/label[1]',

    'getbyid_feedback_save_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]'
                                    '/div/div/div[2]/div/div/button[2]',

    'getbyid_menu_tag_interviewers': '//*[@title="Interviewers"]',

    'getbyid_tag_interviewers': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[1]/div/div/select',

    'interview_panel': '//*[@label="{}"]',

    'add_interviewers_to_table': '//*[@ng-click="vm.addInterviewerToFinalTable()"]',

    'save_interviewers_to_panel': '//*[@type="button"][@ng-click="vm.saveInterviewDetailForJobRole()"]',

    'click_on_screen': '//*[@id="mainBodyElement"]/div[6]/div/div/div[1]/h4',

    # -------------------------------- Job get by id Tabs --------------------------------------------------------------
    'configuration_sub_tab': '//*[@ui-sref="crpo.jobRole.manageJobRole.configurations"]',
    'automation_sub_tab': '//*[@ui-sref="crpo.jobRole.manageJobRole.automations.applicants"]',

    'registration_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72277"]',
    'eligible_check_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72343"]',
    'aptitude_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72355"]',
    'Hr_Interview_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72606"]',
    'hop_stage': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[1]',
    'hop_status': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[2]',
    'ec_on_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/tbody[2]'
                    '/tr[5]/td[5]/div/button',
    'test_automation_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/tbody[3]'
                              '/tr[4]/td[3]/div/button',
    'ready_schedule_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/'
                             'tbody[4]/tr[10]/td[7]/div/button',
    'Hopping_save_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[1]/button',

    'ec_configure': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[1]/div/a',
    'ec_text_field': '//*[@type="text"][@placeholder="Select Eligibility Criteria"]',
    'ec_positive_stage': '//*[@type="text"][@placeholder="Select Stage"]',
    'ec_positive_status': '//*[@type="text"][@placeholder="Select status"]',
    'ec_negative_stage': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[2]/ec-configuration'
                         '/div/div[1]/div/table/tbody/tr/th[4]/ta-dropdown/div/div/input',
    'ec_negative_status': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[2]/ec-configuration/'
                          'div/div[1]/div/table/tbody/tr/th[5]/ta-dropdown/div/div/input',
    'ec_config_save': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[2]/ec-configuration/div/'
                      'div[2]/button[2]',

    'task_configure': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/a',
    'new_task_row': '//*[@title="add row"]',
    'task_stage_status': '//*[@type="text"][@placeholder="Select Stage And Status"]',
    'task_positive_stage_status': '//*[@type="text"][@placeholder="Select Positive Stage - Status"]',
    'task_negative_stage_status': '//*[@type="text"][@placeholder="Select Negative Stage - Status"]',
    'activity_1': '//*[@type="text"][@placeholder="Select Activity"]',
    'Task_selection': '//*[@title="Select Tasks"]',
    'select_all_task': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/'
                       'span/div/div/div[2]/div/button[2]',
    'task_selection_done': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/'
                           'div[2]/div/span/div/div/div[4]/div/a',
    'activity_task_configuration_save': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    # ------------------------------------------------------------------------------------------------------------------

    'job_advance_search': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[1]/div/a[2]',

    'job_search_name_field': "Name",

    'job_search_button': '//*[@id="mainBodyElement"]/div[3]/section/div/div/advance-search/div/div[3]/div/button[2]',

    'job_getbyid': '//*[@id="req-list-view"]/tr/td[4]/a',
}

requirement = {
    # --------------------------------------------- Requirement --------------------------------------------------------
    'requirement_tab': '//*[@ui-sref="crpo.requirements"]',
    'create_requirement': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[2]/a',
    'requirement_name': '//*[@placeholder="Name"]',
    'job_role_selection': '//*[@title="Job Roles"]',
    'job_role_search': '//*[@placeholder="Search"][@type="text"]',
    'job_select': '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div/div[2]/div/div/'
                  'div[2]/div/div/span/div/div/div[2]/div/button[2]',
    'jod_selection_done': '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div/div[2]/div/div[1]/div[2]'
                          '/div/div/span/div/div/div[4]/div',
    'Hiring_track': '//*[@placeholder="Hiring Type"][@type="text"]',
    'college_type': '//*[@placeholder="College Type"][@type="text"]',
    'requirement_create_button': '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div/div[3]/div/button[2]',

    'req_name_breadcrumbs': '//*[@id="mainBodyElement"]/div[3]/div/div/h3',

    'req_config_tab': '//*[@ng-click="vm.goToConfiguration()"]',
    'req_duplicity_check': '//*[@ui-sref="crpo.requirements.manage.configuration.candidateDuplicity"]',
    'req_duplicity_dont_allow': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/div/div[2]/ui-view/div/div[1]'
                                '/div/div[2]/div/label[2]',

    'req_advance_search': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[1]/div/a[2]',
    'req_search_name_field': "Name",
    'req_name_getbyid': '//*[@title="{}"]',
    'req_search_button': '//*[@id="mainBodyElement"]/div[3]/section/div/div/advance-search/div/div[3]/div/button[2]',

}

test = {
    'assessment_tab': '//*[@ui-sref="crpo.assessment"]',
    'assess_advance_search': '//*[@data-title="Search"]',
    'assessment_name': 'testName',
    'assess_search_button': '//*[@id="mainBodyElement"]/div[3]/section/div/div/advance-search/div/div[3]/div/button[2]',
    'grid_test_name': '//*[@title="{}"]',
    'more_actions': '//*[@id="req-list-view"]/tr/td[2]/span[3]',
    'clone_test_action': '//*[@id="req-list-view"]/tr/td[2]/div/div[3]/div[13]/div',
    'from_date': '//*[@placeholder="From"][@type="text"]',
    'to_date': '//*[@placeholder="To"][@type="text"]',
    'clone/save': '//*[@type="submit"]'
}

event = {
    'event_tab': '//*[@ui-sref="crpo.events"]',
    'refresh': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[1]/div/a[1]',
    'new_event_button': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[1]/div[2]/a',
    'event_name': '//*[@placeholder="Name"][@type="text"]',
    'event_req_name': '//*[@placeholder="Requirement"][@type="text"]',
    'event_job_name_field': '//*[@title="Job Roles"]',
    'event_job_name_text': '//*[@placeholder="Search"][@type="text"][@title="Type here to search"]',
    'event_job_selection': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/transcluded-input/div/div'
                           '/div[1]/div[3]/div/div/span/div/div/div[2]/div/button[2]',
    'selection_done': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/transcluded-input/div/div/'
                      'div[1]/div[3]/div/div/span/div/div/div[4]/div/a',
    'from_date': '//*[@placeholder="From"][@type="text"]',
    'to_date': '//*[@placeholder="To"][@type="text"]',
    'slot': '//*[@placeholder="Slot"][@type="text"]',
    'event_manager': '//*[@placeholder="Event Manager"][@type="text"]',
    'college': '//*[@placeholder="College"][@type="text"]',
    'ec_enable': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[2]/div/label[1]',
    'create_event_button': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[3]/div/button[2]',

    'grid_event_name': '//*[@title="{}"]',
    'event_config_tab': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.configurations"]',
    'event_task_configure': '//*[@ng-click="vm.getTaskConfigurationModal()"]',
    'task_config_job': '//*[@placeholder="Select Job Role"][@type="text"]',
    'task_search_in_configure': '//*[@placeholder="Search"][@type="text"][@title="Type here to search"]',
    'task_stage_status': '//*[@type="text"][@placeholder="Select Stage And Status"]',
    'task_positive_stage_status': '//*[@type="text"][@placeholder="Select Positive Stage - Status"]',
    'task_negative_stage_status': '//*[@type="text"][@placeholder="Select Negative Stage - Status"]',

    'Event_test_configure': '//*[@ng-click="vm.configure()"]',
    'test_jobrole': '//*[@placeholder="Job Role"][@type="text"]',
    'test_stage': '//*[@placeholder="Stage"][@type="text"]',
    'test_name': '//*[@placeholder="Test"][@type="text"]',
    'test_active': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/div/div[5]/div/label[1]',
    'test_save': '//*[@ng-click="vm.tagTestToEvent()"]',

    'event_owner_tab': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.owners"]',
    'event_owner_edit': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.manageOwners"]',
    'event_interviewer_add': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'event_custom_users': '#mainBodyElement > div.ng-scope.unbranded > div > div:nth-child(3) > div.'
                          'col-sm-12.no-padding.ng-scope > section > div:nth-child(2) > div > '
                          'create-update-event-owners > div > div.row > div:nth-child(4) > div > '
                          'transcluded-input > div > div > div > p > small > a',
    'role': '//*[@placeholder="Role"][@type="text"]',
    'custom_owner_add': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'update_owners': '#mainBodyElement > div.ng-scope.unbranded > div > div:nth-child(3) > '
                     'div.col-sm-12.no-padding.ng-scope > section > div:nth-child(2) > div > '
                     'create-update-event-owners > div > div.col-sm-12.no-padding > div >'
                     ' button.btn.btn-primary.back_btn.ng-scope'

}
