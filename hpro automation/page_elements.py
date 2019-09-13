
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
    'new_getbyid_feedback_from_search_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/'
                                               'div/div/div[2]/div/div/div[2]/div/div[4]/button',

    'getbyid_feedback_form_use': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]'
                                 '/div/div/interview-templates-search/div/accordian-row-table/table/tbody'
                                 '/tr/td[3]/div/span[1]',
    'new_getbyid_feedback_form_use': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/'
                                     'div/div[2]/div/div/div[2]/accordian-row-table/table/tbody/tr[3]/td[3]/div/span',

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
    'event_custom_users': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/section/div[2]/div/'
                          'create-update-event-owners/div/div[1]/div[4]/div/transcluded-input/div/div/div/p/small/a',
    'role': '//*[@placeholder="Role"][@type="text"]',
    'custom_owner_add': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'update_owners': '#mainBodyElement > div.ng-scope.unbranded > div > div:nth-child(3) > '
                     'div.col-sm-12.no-padding.ng-scope > section > div:nth-child(2) > div > '
                     'create-update-event-owners > div > div.col-sm-12.no-padding > div >'
                     ' button.btn.btn-primary.back_btn.ng-scope',
    'Floating_actions': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]'
                        '/section/div[1]/floating-actions/span/span/i',
    'event_upload_candidates': '//*[@title="Upload Candidates"]',
    'event_upload_file': '//*[@type="file"][@file-model="vm.uploadedCandidateTemplateFile"]',
    'event_interviews': '//*[@title="View Event Interviews"]',
    'provide_feedback': '//*[@data-title="Provide Interview Feedback"]',
    'Next_Button': '//*[@data-ng-click="vm.gotoNextState()"]',
    'declare_checkbox': '//*[@type="checkbox"][@ng-click="vm.viewDeclaration();"]',
    'signature': '//*[@type="text"][@ng-model="vm.signature"]',
    'Agree': '//*[@type="button"][@data-ng-click="$hide();vm.isAgreement=true;"]',
    'save_uploads': '//*[@data-ng-click="vm.consolidateCandidateInfo();"]',
    'upload_candidate_count': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/div[2]',
    'close_pop_details_window': '//*[@type="button"][@ng-click="$hide()"]',
    'View_Applicants': '//*[@title="View Candidates"]',
    'applicant_advance_search': '//*[@data-title="Search"]',
    'applicant_name': 'name',
    'applicant_search_button': '//*[@ng-click="vm.apply();$hide();"]',
    'applicant_getbyid': '//*[@title="{}"]',
    'applicant_validate': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/p[1]',
    'applicant_select_checkbox': 'grid_items',
    'Change_applicant_status': '//*[@data-title="Change Applicant Status"]',
    'change_stage': '//*[@ng-model="vm.selectedStage"]',
    'change_status': '//*[@ng-model="vm.selectedStatus"]',
    'Interviewer': '//*[@title="Select Interviewers"]',
    'Interviewer_selection': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[6]/div/div/span/div/div'
                             '/div[2]/div/button[2]/i[1]',
    'Interviewer_selection_done': '//*[@ng-click="$hide();"]',
    'comment': '//*[@ng-model="vm.comments"]',
    'change_button': '//*[@ng-click="vm.changeCandidateStatus()"]',
    'current_status': '//*[@title="{}"]',
    'Event_advance_search': '//*[@data-title="Search"]',
    'event_names': 'Name',
    'event_search_button': '//*[@ng-click="vm.apply();$hide();"]',
    'Click_on_event_name': '//*[@title="Click to view full details"]',
    'manage_task': '//*[@title="Manage Task"]',
    'candidate_details_floating_actions': '//*[@id="mainBodyElement"]/div[3]/div/div[1]'
                                          '/div[2]/floating-actions/span/span/i',
    'task_candidate_name': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[1]/span',
    'total_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[5]',
    'approved_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[4]',
    'pending_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[2]',
    'submitted_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[1]',
    'rejected_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[3]',
    'more_tabs': '//*[@data-placement="bottom-center"]',
    'reschedule': '//*[@data-title="Reschedule Interview"]',
    'reschedule1': '//*[@id="req-list-view"]/tr/td[2]/div/div[3]/div[2]/div/div[2]',
    'reschedule_comment': '//*[@ng-model="vm.comments"]',
    'reschedule_save': '//*[@ng-click="vm.save();"]',
    'tracking_module': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.tracking"]',
    'tracking_request': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.tracking.interviewCancelRequest"]',
    'approve': '//*[@title="Approve Request"]',
    'request_comment': '//*[@ng-model="data.comments"]',
    'request_ok': '//*[@ng-click="data.result=true;$hide();"]'

}

pofu = {
    'POFU_App': '//*[@ng-click="vm.invokeOtherApp(value.click)"]',
    'pofu_candidates_tab': '/html/body/div[1]/header[2]/div/div/div[2]/div/ul/li[2]/a',
    'pofu_candidates_advance_search': '//*[@ng-click="vm.toggleAdvancedSearch()"]',
    'pofu_candi_text_box': '//*[@ng-model="vm.candidateSearchCriteria.CandidatName"]',
    'pofu_search_button': '/html/body/div[2]/div/div[1]/section/div/div/di'
                          'v[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/form/div/div[3]/div[3]/button',
    'submit_behalf_of': '//*[@title="Submit Tasks on Behalf of Candidate"]',
    'task_acceptance': 'testacceprtanceoffer',
    'submit_task': '//*[@data-ng-click="vm.submitForm(false);"]'
}

settings = {
    'settings_icon': '//*[@id="mainBodyElement"]/div[1]/div/header/div[1]/nav/div/div[3]/a/i',
    'settings': '//*[@ui-sref="crpo.settings"]',
    'Interview_module': '//*[@title="Interview Module"]',
    'new_interview_feedback_form': '//*[@ui-sref="crpo.settings.interview.enableNewInterviewFeedbackForm"]',
    'on': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div/ui-view/div/div/div/div[2]/div/label[1]',
    'off': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div/ui-view/div/div/div/div[2]/div/label[2]'
}

feedback = {
    'more': '//*[@data-trigger="click"]',
    'cancel_1': '//*[@id="req-list-view"]/tr/td[2]/div/div[3]/div[3]/div/div[2]',

    'cancel': '//*[@data-title="Cancel Interview"]',
    'cancel_confirm': '//*[@ng-click="vm.cancelInterview();"]',
    'cancel_request': '//*[@data-title="Cancel Interview Request"]',
    'cancel_request_reason': '//*[@type="text"][@placeholder="Reason"]',
    'comment': '//*[@ng-model="vm.comment"]',
    'cancel_request_save': '//*[@ng-click="vm.cancelInterviewReq();"]',
    'maybe': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]',
    'shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]',
    'save_draft': '//*[@ng-click="vm.saveDraft();"]',

    'rating_1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                'accordian-row-table/table/tbody/tr[2]/td/div/div[1]/select',
    'comment_1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                 'accordian-row-table/table/tbody/tr[2]/td/div/div[2]/div/textarea',
    'rating_2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                'accordian-row-table/table/tbody/tr[4]/td/div/div[1]/select',
    'comment_2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                 'accordian-row-table/table/tbody/tr[4]/td/div/div[2]/div/textarea',
    'overall': '//*[@ng-model="vm.finalTranscript"]',
    'partial_feedback': '//*[@ng-click="vm.partialSubmitFeedback();"]',

    'feedback_form_validation_agree': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    'submit_feedback': '//*[@ng-click="vm.submitFeedback(vm.isUpdateFeedback);"]',
    'Interview_bucket': '//*[@ng-model="vm.config.selectedEntityType"]',
    'review_feedback': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
}

unlock = {
    'All_my_interviews': '//*[@ng-model="vm.config.selectedDropdownValue"]',
    'unlock_action': '//*[@data-title="Unlock Interviewer Feedback"]',
    'all_interviewers': '//*[@ng-model="vm.isAllSelected"]',
    'unlock_feedback_button': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    'comment': '//*[@ng-model="data.comments"]',
    'ok': '//*[@ng-click="data.result=true;$hide();"]'

}

update = {
    'shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]'
}

new_feedback = {
    'overall': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
               '/div[2]/div/div/div/div/div[2]/auto-grow-textarea/textarea',
    'duration': '//*[@ng-model="vm.data.interviewForm.overallSection.duration"]',
    'save_as_draft': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/button[2]',

    'Q1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]/div[1]/div[1]/div/div[1]/div/select',
    'Q1_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]/'
                  'div[1]/div[1]/div/div[2]/div/auto-grow-textarea/textarea',
    'Q2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]/div[1]/div[2]/div/div[1]/div/select',
    'Q2_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]/div[1]/div[2]'
                  '/div/div[2]/div/auto-grow-textarea/textarea',
    'Q3': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]/div[1]/div[3]/div/div/div/select',
    'maybe': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/di'
             'v/section/div[2]/div/div/div/div/div[1]/div/div[3]',
    'submit_feedback': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/button[1]',
    
    'u_Q1_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section/'
                    'div[1]/div[1]/div/div[2]/div/auto-grow-textarea/textarea',
    'u_Q2_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section'
                    '/div[1]/div[2]/div/div[2]/div/auto-grow-textarea/textarea',
    'shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section'
                 '/div[2]/div/div/div/div/div[1]/div/div[1]',
    'u_overall': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section'
                 '/div[2]/div/div/div/div/div[2]/auto-grow-textarea/textarea',
    'update_feedback': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/button',

}

live_interview = {
    'live_interview_action': '//*[@title="Live Schedule Interviews"]',
    'select_stage': '//*[@ng-model="vm.selectedInterviewStage"]',
    'candidate_name': '//*[@ng-model="vm.inputCandidateName"]',
    'search_button': '//*[@ng-click="vm.searchApplicants();"]',
    'select_search_candidates': '//*[@ng-model="vm.isAllSelected"]',
    'schedule': '//*[@ng-click="vm.openScheduleMultipleModal();"]',
    'scheduled': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    'details': '//*[@id="mainBodyElement"]/div[3]/div/div/div[2]/accordian-row-table/table/tbody/tr/td[7]',
    'provide_feedback': '//*[@ng-click="data.onGiveFeedbackClick(rowKey);"]'
}