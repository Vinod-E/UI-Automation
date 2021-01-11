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
    'login_back': '//*[@ng-click="vm.backToLogin()"]',
    'candidate_login_success': '//*[@ng-bind="vm.candidateInfo.CandidateName"]'
}
embrace_login = {
    'next_button': '//*[@ng-click="vm.getTenantConfiguration(vm.tenantAlias);$hide();"]',
    'username': "username",
    'password': 'new-password',
    'login_success': '/html/body/div[1]/header[2]/div/div/div[2]/div/div/div[1]/span[1]',
    'tenant_alias_page': '/html/body/div[5]/div/div/div[1]/h4'
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
    'job_owners': '//*[@ui-sref="crpo.jobRole.details.interviewers"]',
    'job_configuration_tab': '//*[@ui-sref="crpo.jobRole.details.configurations"]',
    'job_automation_tab': '//*[@ui-sref="crpo.jobRole.details.automations.applicants"]',
    'req_configuration_tab': '//*[@ng-click="vm.goToConfiguration()"]',
    'req_duplicity_check': '//*[@ui-sref="crpo.requirements.details.configuration.candidateDuplicity"]',
    'req_query_config': '//*[@ui-sref="crpo.requirements.details.configuration.queryConfiguration"]',
    'event_configuration_tab': '//*[@ui-sref="crpo.events.details.configurations"]',
    'event_owner_tab': '//*[@ui-sref="crpo.events.details.owners"]',
    'more_tabs': '//*[@data-placement="bottom-center"]',
    'embrace_candidate_tab': '/html/body/div[1]/header[2]/div/div/div[2]/div/ul/li[2]/a',
    'event_tracking': '//*[@ui-sref="crpo.events.details.tracking"]',
    'help_desk_tab': '//*[@ui-sref="candidate.helpdesk.faq"]',
    'raise_query_tab': '//*[@ui-sref="candidate.helpdesk.raiseQuery"]',
    'manage_nominations': '//*[@ui-sref="crpo.events.interviewers.nominations"]',
    'nomination_tab': '//*[@ui-sref="crpo.nominations"]'
}

buttons = {
    # ------------------------------------------ Buttons ---------------------------------------------------------------
    'common_button': "//button[text()='{}']",
    'all_buttons': "//*[text()='{}']",
    'click_button': '//*[@ng-click="vm.actionClicked({}{}{});"]',
    'button_click': '//*[@ng-click="vm.actionClicked({}{}{})"]',

    'create': '//*[@ng-click="vm.create();"]',
    'template-search': '//*[@ng-click="vm.service.templates.search();"]',
    'live_applicant_search': '//*[@ng-click="vm.searchApplicants();"]',
    'Search_interviewers': '//*[@ng-click="criterion.searchInterviewers()"]',
    'save_invite_int': '//*[@ng-click="vm.validateAndSave()"]',
    'send_mail': '//*[@ng-click="vm.sendMailToAll()"]',
    'clear_refresh': '//*[@ng-click="vm.refreshList()"]',
    'save': '//*[@ng-click="vm.save();"]',
    'Save_draft': '//*[@ng-click="vm.saveDraft();"]',
    'partial_submission': '//*[@ng-click="vm.partialSubmitFeedback();"]'
}

text_fields = {
    # ------------------------------------------ Text Fields -----------------------------------------------------------
    'text_field': '//*[@type="text"][@placeholder="{}"]',
    'text_number': '//*[@type="number"][@placeholder="{}"]',
    'place_holder': '//*[@placeholder="{}"]'
}

file = {
    # ------------------------------------------- Files ----------------------------------------------------------------
    'upload_file': '//*[@type="file"]',
    'event_upload_file': '//*[@type="file"][@file-model="vm.uploadedCandidateTemplateFile"]'
}

floating_actions = {
    'floating_actions': '//*[@class="fa fa-caret-down"]',
    'selection_process': 'Jobrole-Details-Selection-Process',
    'feedback_form': 'Jobrole-Details-Configure-Feedback-Form',
    'tag_interviewers': 'Jobrole-Details-Interviewers',
    'job_edit': 'Jobrole-Details-Edit',
    'tag_requirement': 'Jobrole-Details-Tag-To-Requirement',
    'un-tag_requirement': 'Jobrole-Details-Untag-Requirement',
    'clone_assessment': 'Assessment-Details-Clone-Assessment',
    'event_upload_candidates': 'Event-Details-Upload-Candidates',
    'View_Applicants': 'Event-Details-View-Candidates',
    'live_interview': 'Event-Details-Live-Schedule-Interviews',
    'manage_interviewers': 'Event-Details-Manage-Interviewers',
    'Quick_interview': 'Event-Details-Quick-Interview-Schedule-',
    'event_interviews': 'Event-Details-View-Event-Interviews',
    'Configure_slots': 'Event-Details-Configure-Interview-Slots',
    'interview_lobby': 'Event-Details-View-Interview-Lobby',
    'view_interview_panel': 'Event-Details-View-Interview-Panel'
}
grid = {
    'check_box': 'grid_items',
    'all': '//*[@ng-model="vm.isAllSelected"]',
    'test_required': '//*[@ng-model="vm.isTestRequaredForTag"]',
}
grid_actions = {
    'reschedule': 'cardlist-view-Reschedule-Interview',
    'cancel_interview': 'cardlist-view-Cancel-Interview',
    'cancel_interview_request': 'cardlist-view-Cancel-Interview Request',
    'provide_feedback': 'cardlist-view-Provide-Interview Feedback',
    'unlock_feedback': 'cardlist-view-Unlock-Interviewer Feedback',
    'view_feedback': 'cardlist-view-View-Feedback History',
    'refresh': 'cardlist-view-refresh'
}
applicant_actions = {
    'actions': "//div[text()='{}']",
    'more_actions': '//*[@id="req-list-view"]/tr/td[2]/span[3]',
    'job_more_actions': '//*[@id="req-list-view"]/tr/td[2]/span[4]/a',
    'Change_applicant_status': 'cardlist-view-Change-Applicant Status',
    'job_Change_applicant_status': 'cardlist-view-Change-Applicant(s) Status',
    'compose_mail': 'cardlist-view-Compose-Mail',
    'send_sms': 'cardlist-view-Send-SMS',
    'tag_applicants': 'cardlist-view-Tag-Applicant(s) to Job/Test',
    'untag_applicants': 'cardlist-view-Untag-Applicant(s)',
    'copy_registration_link': 'cardlist-view-Copy-Registration Link',
}
advance_search = {
    'search': 'cardlist-view-filter',
    'name': 'Name',
    'a_name': 'name',
    'assessment_name': 'testName',
    'job_applicant_name': 'CandidateName'
}
change_applicant_status = {
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
    'tooltip': '//*[@bs-tooltip="{}"]'
}
multi_selection_box = {
    'moveSelectedItemsRight': '//*[@data-ng-click="vm.moveSelectedItemsRight();"]',
    'moveAllItemsRight': '//*[@data-ng-click="vm.moveAllItemsRight();"]',
    'moveSelectedItemsLeft': '//*[@data-ng-click="vm.moveSelectedItemsLeft();"]',
    'moveAllItemsLeft': '//*[@data-ng-click="vm.moveAllItemsLeft();"]',
}
glowing_messages = {
    'notifier': '//*[@class="growl-message ng-binding"]',
    'dismiss': '//*[@data-dismiss="alert"]'
}
validations = {
    'task_candidate_name': '//*[@id="mainBodyElement"]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[1]/span[1]',
}
microSite = {
    'micro_site_campus_details': '//*[@id="campusform"]/div/div[1]/div/h4',
    'micro_site_page_closed': '//*[@id="index_contentdiv"]/div/span',
    'yes': 'lbl_terms_yes',
    'declaration': 'declaration',
    'submit': 'registerbtndiv'
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
    'interview_panel': '//*[@label="{}"]',
    'add_interviewers_to_table': '//*[@ng-click="vm.addInterviewerToFinalTable()"]',
    'owners_number': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[1]/p',
    'ec_configure': '//*[@ng-click="vm.actionClicked({}{}{})"]'.format("'", 'configureEC', "'"),
    'ec_negative_stage': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[3]/div[2]/'
                         'ec-configuration/div/div[1]/div[1]/table/tbody/tr/th[4]/ta-dropdown/div/div/input',
    'ec_negative_status': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[3]/div[2]/'
                          'ec-configuration/div/div[1]/div[1]/table/tbody/tr/th[5]/ta-dropdown/div/div/input',
    'task_configure': '//*[@ng-click="vm.actionClicked({}{}{})"]'.format("'", 'configureTask', "'"),
    'new_task_row': '//*[@title="add row"]',
    'Task_selection': '//*[@title="Select Tasks"]',
    'select_all_task': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/'
                       'span/div/div/div[2]/div/button[2]',
    'task_selection_done': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/'
                           'div[2]/div/span/div/div/div[4]/div/a',
    'template_comment': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view'
                        '/div/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[2]/td[2]/div/label[1]',
    'template_reject': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view'
                       '/div/div/div[2]/div/div/div[1]/div/div/table/tbody/tr[3]/td[2]/div/label[1]',

    'hop_stage': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[1]',
    'hop_status': '//*[@id="mainBodyElement"]/div[5]/div[2]/select[2]',
    'registration_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72277"]',
    'aptitude_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72355"]',
    'eligibility_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72343"]',
    'Hr_Interview_stage_hop': '//*[@title="Set stage and status to hop to"][@data-content="72606"]',

    'test_automation_button': '//*[@id="main-table"]/tbody[3]/tr[4]/td[2]/div/switch-toggle/label/span',
    'ec_on_button': '//*[@id="main-table"]/tbody[2]/tr[4]/td[4]/div/switch-toggle/label/span',
    'ready_schedule_button': '//*[@id="main-table"]/tbody[4]/tr[9]/td[7]/div/switch-toggle/label/span',
}

requirement = {
    'job_selection_field': '//*[@title="Job Roles"]',
}

assessment = {
    'grid_assessment_name': '//*[@title="{}"]',
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
    'event_task_configure': '//*[@ng-click="vm.getTaskConfigurationModal()"]',
    'task_is_config': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div[2]/div/div[1]/div/div[2]/'
                      'view-task-configurations/div/div[1]/div/table/tbody/tr/td[5]',
    'event_test_configure': '//*[@ng-click="vm.actionClicked({}{}{})"]'.format("'", 'configure', "'"),
    'test_active': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/div/div[5]/div/label[1]',

    'test_is_config': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view'
                      '/div[1]/div/div[2]/table/tbody/tr/td[4]',
    'declare_checkbox': '//*[@type="checkbox"][@ng-model="vm.isAgreement"]',
    'signature': '//*[@type="text"][@ng-model="vm.signature"]',
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
    'subject': '//*[@ng-model="vm.subject"]',
    'description': '//*[@ng-model="html"]',
    'open_RL_new_tab': '//*[@id="mainBodyElement"]/div[6]/div/div/div[2]/div[2]/a',
    'comment': '//*[@ng-model="vm.comments"]',
    'candidate_id': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[1]/div/div/div[2]/div[2]/p[2]/span[2]'
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
    'Quick_shortlist': '//*[@id="mainBodyElement"]/div[3]/div/div[1]/div[3]/div/div[2]/div/label[2]',
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
mass_interview = {
    'room_name': '//*[@id="mainBodyElement"]/div[3]/div/div[3]/div/'
                 'ui-view/div/div/div[1]/div/div[3]/div/table/tbody/tr/td[2]/b',
    'Interview_Status': '//*[@id="mainBodyElement"]/div[3]/div/div[3]/div/ui-view'
                        '/div/div[5]/div/table/tbody/tr/td[7]/div',
    'interviewer_name': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div/div[1]/div/div/p[1]',
    'lobby_cid': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div/div/p[3]/span[2]',
    'message': '//span[@ng-if="vm.data.message"]',
    'candidate_msg1': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/p[1]',
    'candidate_msg2': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]',
    'candidate_msg3': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/p[1]',
    'candidate_msg4': '/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/p[1]',
    'declare': '//input[@type="checkbox"]',
    'finish_interview': '//*[@id="mainBodyElement"]/div[6]/div/div/div/div[2]/div[1]/button'
}

help_desk = {
    'category': '//span[@title="Query Category"]',
    'user': '//*[@title="Users"]',
    'sla': '//input[@type="number"]',
    'job': '//*[@title="Jobs"]',
    'event': '//*[@title="Events"]',
    'job_users': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/div/'
                 'div[1]/div[2]/div/div/table/tbody/tr/td[3]/div/span/span/span[1]',
    'job_sla': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/'
               'div/div[1]/div[2]/div/div/table/tbody/tr/td[4]/input',
    'event_job': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/'
                 'div/div[1]/div[3]/div/div/table/tbody/tr/td[2]/div/span/span/span[1]',
    'event_users': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/'
                   'div/div[1]/div[3]/div/div/table/tbody/tr/td[4]/div/span/span/span[1]',
    'event_sla': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/div[2]/ui-view/div/div[2]/ui-view/'
                 'div/div[1]/div[3]/div/div/table/tbody/tr/td[5]/input',
    'query_choose': '//*[@ng-change="vm.processQueries();"]',
    'subject': 'Subject',
    'message': '//*[@ng-model="vm.messasge"]',
    'find': '//*[@type="search"][@placeholder="Find"]',
    'open/inprogress/close': '//*[@ng-change="vm.getQueryAssignToMe();"]',
    'total_records': '/html/body/div[2]/div/section/div[1]/div/div/div/div[2]/div/div[2]/'
                     'div/div/div[1]/div/div/div/span[2]'
}

manage_interviews = {
    'add_criteria': '//*[@ng-click="vm.addCriteria()"]',
    'panel2': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
              'transcluded-input/div/div/div/div/div[1]/ta-dropdown/div/div/input',
    'Search_interviewers2': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
                            'transcluded-input/div/div/div[1]/div[1]/div[4]/button',
    'required_int': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
                    'transcluded-input/div/div/div[1]/div[2]/div/div[1]/input',
    'required_nom': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/'
                    'transcluded-input/div/div/div[1]/div[2]/div/div[2]/input',
    'header': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[1]/div[1]/div/div/h5',
    'panel_search': '//*[@ng-model="vm.selectedSearchPanelType"]',
    'paging': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/'
              'section/div[2]/div[1]/div[2]/paging-control/div/div/span',
    'skill_validate': '//*[@id="mainBodyElement"]/div[3]/div/div[2]/section/'
                      'accordian-row-table/table/tbody/tr[2]/td/div/div/div/p[1]',
    'no_invitation_message': '//*[@ng-if="vm.invitations && !vm.invitations.data.length"]',
    'approve': '//*[@id="mainBodyElement"]/div[3]/div/div/div[3]/section/div[2]/div[1]/div[2]/ul/li[1]/a'
}
