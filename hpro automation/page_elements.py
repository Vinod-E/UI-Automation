login = {
    # ------------------------------------------Login details-----------------------------------------------------------
    'tenant_alias_page': '//*[@id="mainBodyElement"]/div[6]/div/div/div[1]/h4',
    'tenant': "alias",
    'next_button': '//*[@id="mainBodyElement"]/div[6]/div/div/form/div[2]/button',
    'username': "loginName",
    'password': '//*[@type="password"]',
    'login_button': '//*[@ng-click="vm.login()"]',
    'login_success': '/html/body/div[1]/div/header/div[1]/nav/div/div[3]/ul/li/a',
    'tenant_screen_text': '//*[@id="mainBodyElement"]/div[6]/div/div/div[1]/h4',
    'page_cant_be_reached': '//*[@id="main-message"]/h1/span',
    'internet_error': '//*[@id="main-message"]/h1/span',
    'wrong_credentials': '//*[@id="mainBodyElement"]/div[1]/div/header/div[3]/div/div',
    'logout': 'crpo-settings-logout',
    'login_back': '//*[@ng-click="vm.backToLogin()"]'
}
setting_modules = {
    'settings': '//*[@ui-sref="crpo.settings"]',
    'interview_module': '//*[@title="Interview Module"]',
    'enable_new_feedback_form': '//*[@ui-sref="crpo.settings.interview.enableNewInterviewFeedbackForm"]',
    'On': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/ui-view/div/div/div/div[2]/div/label[1]',
    'Off': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/ui-view/div/div/div/div[2]/div/label[2]',
}
tabs = {
    # ------------------------------------------Event menu tabs --------------------------------------------------------
    'job_tab': '//*[@ui-sref="crpo.jobRole"]',
    'event_tab': '//*[@ui-sref="crpo.events"]',
    'requirement_tab': '//*[@ui-sref="crpo.requirements"]',
    'assessment_tab': '//*[@ui-sref="crpo.assessment"]',
    'embrace_tab': '//*[@ng-click="vm.invokeOtherApp(value.click)"]',
    'job_configuration_tab': '//*[@ui-sref="crpo.jobRole.manageJobRole.configurations"]',
    'job_automation_tab': '//*[@ui-sref="crpo.jobRole.manageJobRole.automations.applicants"]',
    'job_owners': '//*[@ui-sref="crpo.jobRole.manageJobRole.interviewers"]',
    'job_basic_details': '//*[@ui-sref="crpo.jobRole.manageJobRole.basic"]',
    'req_configuration_tab': '//*[@ng-click="vm.goToConfiguration()"]',
    'req_duplicity_check': '//*[@ui-sref="crpo.requirements.manage.configuration.candidateDuplicity"]',
    'event_configuration_tab': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.configurations"]',
    'event_owner_tab': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.owners"]',
    'more_tabs': '//*[@data-placement="bottom-center"]',
    'embrace_candidate_tab': '/html/body/div[1]/header[2]/div/div/div[2]/div/ul/li[2]/a',
    'event_tracking': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.tracking"]',
    'interview_cancel_request': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.tracking.interviewCancelRequest"]',
}

buttons = {
    # ------------------------------------------ Buttons ---------------------------------------------------------------
    'create': '//*[@ng-click="vm.create();"]',
    'update': '//*[@ng-click="vm.update();"]',
    'create-save': '//*[@ng-click="vm.save();"]',
    'sp-save': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/button[2]',
    'template-search': '//*[@ng-click="vm.service.templates.search();"]',
    'template_save': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/'
                     'div/div[2]/div/div/div[2]/div/div/button[2]',
    'new_template_search': '//*[@ng-click="vm.actionClicked({}{}{})"]',
    'use': '//*[@ng-click="data.actionClicked({}{}{},292)"]',
    'job_ec_save': '//*[@ng-click="vm.saveEcConfig();"]',
    'job_ec_close': '//*[@ng-click="vm.cancel();"]',
    'done': '//*[@ng-click="$hide();"]',
    'job_task_config_save': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    'Hopping_save_button': '//*[@ng-click="vm.saveApplicantAutomationConfig();"]',
    'save_interviewers_to_panel': '//*[@ng-click="vm.saveInterviewDetailForJobRole()"]',
    'job_requirement_tag': '//*[@ng-click="vm.tagJobRoleToRequirement(data.jobRoleId);"]',
    'ok': '//*[@ng-click="data.result=true;$hide();"]',
    'search': '//*[@ng-click="vm.apply();$hide();"]',
    'requirement_create': '//*[@ng-if="!vm.data.requirementId"]',
    'dont_allow': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/div/'
                  'div[2]/ui-view/div/div[1]/div/div[2]/div/label[2]',
    'clone/save': '//*[@type="submit"]',
    'event_create': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[3]/div/button[2]',
    'event_test_save': '//*[@ng-click="vm.tagTestToEvent()"]',
    'update_event_owners': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/section/div[2]/div/'
                           'create-update-event-owners/div/div[2]/div/button[2]',
    'event_upload_candidate_save': '//*[@data-ng-click="vm.consolidateCandidateInfo();"]',
    'status_change_button': '//*[@ng-click="vm.changeCandidateStatus()"]',
    'cancel_confirm': '//*[@ng-click="vm.cancelInterview();"]',
    'cancel_request': '//*[@ng-click="vm.cancelInterviewReq();"]',
    'save_draft': '//*[@ng-click="vm.saveDraft();"]',
    'partial_feedback': '//*[@ng-click="vm.partialSubmitFeedback();"]',
    'agree': '//*[@ng-click="vm.actionClicked({}{}{});"]',
    'submit_feedback': '//*[@ng-click="vm.submitFeedback(vm.isUpdateFeedback);"]',
    'live_schedule_multiple': '//*[@ng-click="vm.openScheduleMultipleModal();"]',
    'live_schedule': '//*[@ng-click="vm.scheduleMultiple();$hide()"]',
    'live_applicant_search': '//*[@ng-click="vm.searchApplicants();"]',
    'new_save_draft': '//*[@ng-if="vm.data.configs.isDraftAllowed"]',
    'new_submit_feedback': '//*[@ng-if="vm.data.configs.isSubmitAllowed"]'
}

text_fields = {
    # ------------------------------------------ Text Fields -----------------------------------------------------------
    'text_field': '//*[@type="text"][@placeholder="{}"]'
}

file = {
    # ------------------------------------------- Files ----------------------------------------------------------------
    'upload_file': '//*[@type="file"]',
    'event_upload_file': '//*[@type="file"][@file-model="vm.uploadedCandidateTemplateFile"]'
}

task_config = {
    'job_task_configure': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/a',
    'event_task_configure': '//*[@ng-click="vm.getTaskConfigurationModal()"]'
}

floating_actions = {
    'floating_actions': '//*[@class="fa fa-angle-right"]',
    'selection_process': '//*[@title="Selection Process"]',
    'feedback_form': '//*[@title="Configure Feedback Form"]',
    'tag_interviewers': '//*[@title="Interviewers"]',
    'tag_requirement': '//*[@title="Tag To Requirement"]',
    'un-tag_requirement': '//*[@title="Untag Requirement"]',
    'job_edit': '//*[@title="Edit"]',
    'clone_assessment': '//*[@title="Clone Assessment"]',
    'event_upload_candidates': '//*[@title="Upload Candidates"]',
    'View_Applicants': '//*[@title="View Candidates"]',
    'manage_task': '//*[@title="Manage Task"]',
    'event_interviews': '//*[@title="View Event Interviews"]',
    'live_interview': '//*[@title="Live Schedule Interviews"]'
}
grid_actions = {
    'reschedule': 'cardlist-view-Reschedule-Interview',
    'cancel_interview': 'cardlist-view-Cancel-Interview',
    'cancel_interview_request': 'cardlist-view-Cancel-Interview Request',
    'provide_feedback': 'cardlist-view-Provide-Interview Feedback',
    'unlock_feedback': 'cardlist-view-Unlock-Interviewer Feedback',
    'view_feedback': 'cardlist-view-View-Feedback History',
    'more_actions': '//*[@id="req-list-view"]/tr/td[2]/span[3]',
}
advance_search = {
    'search': 'cardlist-view-filter',
    'name': 'Name',
    'a_name': 'name',
    'assessment_name': 'testName'
}
grid = {
    'check_box': 'grid_items',
    'all': '//*[@ng-model="vm.isAllSelected"]'
}

change_applicant_status = {
    'Change_applicant_status': '//*[@data-title="Change Applicant Status"]',
    'change_stage': '//*[@ng-model="vm.selectedStage"]',
    'change_status': '//*[@ng-model="vm.selectedStatus"]',
    'comment': '//*[@ng-model="vm.comments"]',
    'Interviewer': '//*[@title="Select Interviewers"]',
    'Interviewer_selection': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[6]/div/div/span/div/div'
                             '/div[2]/div/button[2]/i[1]',
    'Interviewer_selection_done': '//*[@ng-click="$hide();"]',
}

getby_details = {
    'getbyid': '//*[@title="{}"]',
    'event_getbyid': '//*[@title="Click to view full details"]',
}
buckets = {
    'Partial_interviews': '//*[@label="Partial Submissions"]',
    'completed_interviews': '//*[@label="Completed"]',
    'cancel_interviews': '//*[@label="Cancelled"]',
    'all_interviews': '//*[@label="All Interviews"]',
    'select_interview_stage': '//*[@label="{}"]'
}
title = {
    'title': '//*[@title="{}"]',
}
job = {
    'description_box': '//*[@id="mainBodyElement"]/div[3]/section/div/'
                       'basic-job/div/div[2]/div[8]/div/wysiwyg-edit/div/div[2]/iframe',
    'location': '//*[@type="text"][@placeholder="Location"]',
    'hiring_manager': '//*[@type="text"][@placeholder="Hiring Manager"]',
    'business_unit': '//*[@type="text"][@placeholder="Business Unit"]',
    'openings': 'openings',
    'max_applicant': 'Max Applicants',
    'male_diversity': '//*[@placeholder="Male"]',
    'female_diversity': '//*[@placeholder="Female"]',
    'job_getbyid': '//*[@title="{}"]',
}

job_config = {
    'template_use': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div/'
                    'interview-templates-search/div/accordian-row-table/table/tbody/tr[1]/td[4]/span/div/div/span[1]',
    'template_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/'
                        'div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div/label[1]',
    'template_reject': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/'
                       'div/table/tbody/tr[3]/td[2]/div/label[1]',
    'ec_configure': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[1]/div/a',
    'ec_negative_stage': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[2]/ec-configuration'
                         '/div/div[1]/div/table/tbody/tr/th[4]/ta-dropdown/div/div/input',
    'ec_negative_status': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/div[3]/div/div[2]/ec-configuration/'
                          'div/div[1]/div/table/tbody/tr/th[5]/ta-dropdown/div/div/input',
    'new_task_row': '//*[@title="add row"]',
    'Task_selection': '//*[@title="Select Tasks"]',
    'select_all_task': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/'
                       'span/div/div/div[2]/div/button[2]',
    'task_selection_done': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/'
                           'div[2]/div/span/div/div/div[4]/div/a',
    'aptitude_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72355"]',
    'hop_stage': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[1]',
    'hop_status': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[2]',
    'eligibility_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72343"]',
    'registration_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72277"]',
    'test_automation_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/tbody[3]'
                              '/tr[4]/td[3]/div/button',
    'ec_on_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/tbody[2]/'
                    'tr[4]/td[5]/div/button',
    'Hr_Interview_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72606"]',
    'ready_schedule_button': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[4]/div/section/div[2]/table/tbody[4]/'
                             'tr[9]/td[8]/div/button',
    'interview_panel': '//*[@label="{}"]',
    'add_interviewers_to_table': '//*[@ng-click="vm.addInterviewerToFinalTable()"]',
}

job_validations = {
    'job_name_breadcumb': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/span',
    'owners': '//*[@ng-if="vm.owners.length"]',
}

requirement = {
    'job_selection_field': '//*[@title="Job Roles"]',
    'particular_job_select': '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div/div[2]/div/div/'
                             'div[2]/div/div/span/div/div/div[2]/div/button[2]',
    'requirement_getbyid': '//*[@title="{}"]',
}

requirement_validations = {
    'requirement_name_breadcumb': '//*[@id="mainBodyElement"]/div[3]/div/div/h3'
}

assessment = {
    'grid_assessment_name': '//*[@title="{}"]',
}

assessment_validation = {
    'assessment_name_breadcrumb': '//*[@id="mainBodyElement"]/div[3]/ui-view/div/h3'
}

event = {
    'job_field': '//*[@title="Job Roles"]',
    'job_selection': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/transcluded-input/div/div'
                     '/div[1]/div[3]/div/div/span/div/div/div[2]/div/button[2]',
    'labels': '//*[@title="Labels"]',
    'label_selection': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[1]/'
                       'transcluded-input/div/div/div[1]/div[6]/div/div/span/div/div/div[2]/div/button[1]/i',
    'ec_enable': '//*[@id="mainBodyElement"]/div[3]/section/div/div/div[2]/div[2]/div/label[1]',
}

event_validation = {
    'get_event_name': '//*[@title="{}"]'
}

event_config = {
    'Event_test_configure': '//*[@ng-click="vm.configure()"]',
    'test_active': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/div/div[5]/div/label[1]',
    'task_is_config': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/section/div[2]/div/section/div[2]'
                      '/div/div[1]/div/div[2]/view-task-configurations/div/div[1]/accordian-row-table/table/tbody/tr/'
                      'td[4]/span/span',
    'test_is_config': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/section/div[2]/div/section/div[1]/'
                      'div/div/div/div[2]/accordian-row-table/table/tbody/tr/td[3]/span/span',
    'event_owner_edit': '//*[@ui-sref="crpo.events.manageEvent.eventDetails.manageOwners"]',
    'event_interviewer_add': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'Next_Button': '//*[@data-ng-click="vm.gotoNextState()"]',
    'declare_checkbox': '//*[@type="checkbox"][@ng-model="vm.isAgreement"]',
    'signature': '//*[@type="text"][@ng-model="vm.signature"]',
    'Agree': '//*[@type="button"][@data-ng-click="$hide();vm.isAgreement=true;"]',
    'edit_candidate_details': '//*[@title="Edit"]',
    'upload_candidate_name': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/form/div[1]/div/input',
    'upload_candidate_usn': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/form/div[9]/div/input',
    'upload_candidate_email': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/form/div[3]/div/input',
    'details_save': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/button[2]',
    'upload_candidate_count': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/div[2]',
    'close_pop_details_window': '//*[@type="button"][@ng-click="$hide()"]',
    'click_on_event': '//*[@title="Click to view full details"]',
}

event_applicant = {
    'applicant_getbyid': '//*[@title="{}"]',
    'applicant_validation': '//*[@title="{}"]',
    'Interviewer': '//*[@title="Select Interviewers"]',
    'task_candidate_name': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[1]/span',
}

embrace = {
    'embrace_app': '//*[@ng-click="vm.invokeOtherApp(value.click)"]',
    'candidates_advance_search': '//*[@ng-click="vm.toggleAdvancedSearch()"]',
    'candidate_text_box': '//*[@ng-model="vm.candidateSearchCriteria.CandidatName"]',
    'search_button': '/html/body/div[2]/div/div[1]/section/div/div/div[1]/div/div/div/div/'
                          'div[1]/div[2]/div[2]/div/div[1]/form/div/div[3]/div[3]/button',
    'submit_behalf_of': '//*[@title="Submit Tasks on Behalf of Candidate"]',
    'task_acceptance': 'testacceprtanceoffer',
    'submit_task': '//*[@data-ng-click="vm.submitForm(false);"]',
    'total_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[5]',
    'approved_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[4]',
    'pending_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[2]',
    'submitted_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[1]',
    'rejected_tasks': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[3]/div[1]/div/div[3]',
}
interview = {
    'comments': '//*[@ng-model="vm.comments"]',
    'comment': '//*[@ng-model="vm.comment"]',
    'approve': '//*[@title="{}"]',
    'c_r_comment': '//*[@ng-model="data.comments"]',
    'maybe': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]',
    'shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]',
    'rating_1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                'accordian-row-table/table/tbody/tr[2]/td/div/div[1]/select',
    'rating_2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                'accordian-row-table/table/tbody/tr[4]/td/div/div[1]/select',
    'comment_1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                 'accordian-row-table/table/tbody/tr[2]/td/div/div[2]/div/textarea',
    'comment_2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                 'accordian-row-table/table/tbody/tr[4]/td/div/div[2]/div/textarea',
    'overall_comment': '//*[@ng-model="vm.finalTranscript"]',
    'feedback_form_validation_agree': '//*[@id="mainBodyElement"]/div[6]/div/div/div[3]/div/button[2]',
    'updated_decision': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                        'accordian-row-table[1]/table/tbody/tr[1]/td[4]/span',
    'updated_feedback': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/'
                        'accordian-row-table[1]/table/tbody/tr[1]/td[3]/span'
}
live_interview = {
    'validate': '//*[@class="col-sm-8 ellipsis_text ng-binding"]',
    'int1_select': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/inline-multi-select/label[1]/input',
    'int2_select': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/inline-multi-select/label[2]/input',
    'provide_feedback': '//*[@ng-click="data.onGiveFeedbackClick(rowKey);"]',
    'down': '//*[@class="fa fa-chevron-down"]',
    'shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[1]',
    'feedback_int1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[4]/div[2]/div[1]/div[1]/'
                     'inline-multi-select/label[1]/input',
    'feedback_int2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[4]/div[2]/div[1]/div[1]/'
                     'inline-multi-select/label[2]/input'
}

new_interview = {
    'rating1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
               '/div[1]/div[1]/div/div[1]/div/select',
    'comment1': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
                '/div[1]/div[1]/div/div[2]/div/auto-grow-textarea/textarea',
    'rating2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
               '/div[1]/div[2]/div/div[1]/div/select',
    'comment2': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
                '/div[1]/div[2]/div/div[2]/div/auto-grow-textarea/textarea',
    'rating3': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
               '/div[1]/div[3]/div/div/div/select',
    'overall': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[2]/div/div/section[2]'
               '/div[2]/div/div/div/div/div[3]/auto-grow-textarea/textarea',
    'no_interviews': '//*[@data-ng-if="options.title"]'
}
