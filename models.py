# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AccLedgerEmiSchedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateField(db_column='DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    interest = models.IntegerField(db_column='INTEREST', blank=True, null=True)  # Field name made lowercase.
    principal = models.IntegerField(db_column='PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    principal_cumm = models.IntegerField(db_column='PRINCIPAL_CUMM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acc_ledger_emi_schedule'


class AccountStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    primary_status = models.TextField(db_column='PRIMARY_STATUS', blank=True, null=True)  # Field name made lowercase.
    account_classification = models.TextField(db_column='ACCOUNT_CLASSIFICATION', blank=True, null=True)  # Field name made lowercase.
    effective_date = models.DateField(db_column='EFFECTIVE_DATE', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    creator = models.TextField(db_column='CREATOR', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account_status'


class ActiveAndCloseView0(models.Model):
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    form_status = models.IntegerField(db_column='FORM_STATUS', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_first_name = models.TextField(db_column='AD_APPLICANT_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_surname = models.TextField(db_column='AD_APPLICANT_SURNAME', blank=True, null=True)  # Field name made lowercase.
    ad_application_date = models.DateField(db_column='AD_APPLICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    ad_loan_type = models.TextField(db_column='AD_LOAN_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_contact_no = models.TextField(db_column='AD_I_BI_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    loan_amount_sanctioned = models.DecimalField(db_column='LOAN_AMOUNT_SANCTIONED', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_and_close_view0'


class ActiveLoanShortView0(models.Model):
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    ad_applicant_first_name = models.TextField(db_column='AD_APPLICANT_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_surname = models.TextField(db_column='AD_APPLICANT_SURNAME', blank=True, null=True)  # Field name made lowercase.
    ad_application_date = models.DateField(db_column='AD_APPLICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    ad_loan_type = models.TextField(db_column='AD_LOAN_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_contact_no = models.TextField(db_column='AD_I_BI_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    loan_amount_sanctioned = models.DecimalField(db_column='LOAN_AMOUNT_SANCTIONED', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    balance_loan = models.CharField(db_column='BALANCE_LOAN', max_length=135, blank=True, null=True)  # Field name made lowercase.
    facility_duration = models.CharField(db_column='FACILITY_DURATION', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active_loan_short_view0'


class ActualBooking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='BOOKING_DATE', blank=True, null=True)  # Field name made lowercase.
    int_booking = models.IntegerField(db_column='INT_BOOKING', blank=True, null=True)  # Field name made lowercase.
    int_actual = models.IntegerField(db_column='INT_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    int_reversal = models.IntegerField(db_column='INT_REVERSAL', blank=True, null=True)  # Field name made lowercase.
    int_debt_int = models.IntegerField(db_column='INT_DEBT_INT', blank=True, null=True)  # Field name made lowercase.
    princ_booking = models.IntegerField(db_column='PRINC_BOOKING', blank=True, null=True)  # Field name made lowercase.
    princ_actual = models.IntegerField(db_column='PRINC_ACTUAL', blank=True, null=True)  # Field name made lowercase.
    princ_reversal = models.IntegerField(db_column='PRINC_REVERSAL', blank=True, null=True)  # Field name made lowercase.
    princ_debt_princ = models.IntegerField(db_column='PRINC_DEBT_PRINC', blank=True, null=True)  # Field name made lowercase.
    bad_debt = models.IntegerField(db_column='BAD_DEBT', blank=True, null=True)  # Field name made lowercase.
    total_reversal = models.IntegerField(db_column='TOTAL_REVERSAL', blank=True, null=True)  # Field name made lowercase.
    interest_wo = models.IntegerField(db_column='INTEREST_WO', blank=True, null=True)  # Field name made lowercase.
    principal_wo = models.IntegerField(db_column='PRINCIPAL_WO', blank=True, null=True)  # Field name made lowercase.
    total_wo = models.IntegerField(db_column='TOTAL_WO', blank=True, null=True)  # Field name made lowercase.
    outstanding = models.IntegerField(db_column='OUTSTANDING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actual_booking'


class ApplicantDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.TextField(db_column='APP_FORM_ID')  # Field name made lowercase.
    ad_applicant_type = models.TextField(db_column='AD_APPLICANT_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_first_name = models.TextField(db_column='AD_APPLICANT_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_middle_name = models.TextField(db_column='AD_APPLICANT_MIDDLE_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_surname = models.TextField(db_column='AD_APPLICANT_SURNAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_aadhar_no = models.TextField(db_column='AD_APPLICANT_AADHAR_NO', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_pan_no = models.TextField(db_column='AD_APPLICANT_PAN_NO', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_exist_cust = models.TextField(db_column='AD_APPLICANT_EXIST_CUST', blank=True, null=True)  # Field name made lowercase.
    ad_cust_id = models.TextField(db_column='AD_CUST_ID', blank=True, null=True)  # Field name made lowercase.
    ad_loan_type = models.CharField(db_column='AD_LOAN_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_facility_type = models.TextField(db_column='AD_FACILITY_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_security_loan = models.TextField(db_column='AD_SECURITY_LOAN', blank=True, null=True)  # Field name made lowercase.
    ad_isgur_cobor_support = models.TextField(db_column='AD_ISGUR_COBOR_SUPPORT', blank=True, null=True)  # Field name made lowercase.
    ad_sourcing_channel = models.TextField(db_column='AD_SOURCING_CHANNEL', blank=True, null=True)  # Field name made lowercase.
    ad_sourcing_branch = models.TextField(db_column='AD_SOURCING_BRANCH', blank=True, null=True)  # Field name made lowercase.
    ad_region_name = models.TextField(db_column='AD_REGION_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_branch_name = models.TextField(db_column='AD_BRANCH_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_rm_name = models.TextField(db_column='AD_RM_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_application_date = models.DateField(db_column='AD_APPLICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    ad_i_dob = models.TextField(db_column='AD_I_DOB', blank=True, null=True)  # Field name made lowercase.
    ad_i_marital_status = models.TextField(db_column='AD_I_MARITAL_STATUS', blank=True, null=True)  # Field name made lowercase.
    ad_i_gender = models.TextField(db_column='AD_I_GENDER', blank=True, null=True)  # Field name made lowercase.
    ad_i_no_of_dependents = models.TextField(db_column='AD_I_NO_OF_DEPENDENTS', blank=True, null=True)  # Field name made lowercase.
    ad_i_nationality = models.TextField(db_column='AD_I_NATIONALITY', blank=True, null=True)  # Field name made lowercase.
    ad_i_highest_level_education = models.TextField(db_column='AD_I_HIGHEST_LEVEL_EDUCATION', blank=True, null=True)  # Field name made lowercase.
    ad_i_education_degree = models.TextField(db_column='AD_I_EDUCATION_DEGREE', blank=True, null=True)  # Field name made lowercase.
    ad_i_insti_university_name = models.TextField(db_column='AD_I_INSTI_UNIVERSITY_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_i_insti_university_rating = models.TextField(db_column='AD_I_INSTI_UNIVERSITY_RATING', blank=True, null=True)  # Field name made lowercase.
    ad_i_fa_ma_sp_name = models.TextField(db_column='AD_I_FA_MA_SP_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_i_relship_applicant = models.TextField(db_column='AD_I_RELSHIP_APPLICANT', blank=True, null=True)  # Field name made lowercase.
    ad_i_fa_ma_sp_pan_no = models.TextField(db_column='AD_I_FA_MA_SP_PAN_NO', blank=True, null=True)  # Field name made lowercase.
    ad_i_fa_ma_sp_aadhaar = models.TextField(db_column='AD_I_FA_MA_SP_AADHAAR', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_yrs_buss_operation = models.TextField(db_column='AD_I_BI_YRS_BUSS_OPERATION', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_buss_cosnt_type = models.TextField(db_column='AD_I_BI_BUSS_COSNT_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_industry_type = models.TextField(db_column='AD_I_BI_INDUSTRY_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_desc_of_buss = models.TextField(db_column='AD_I_BI_DESC_OF_BUSS', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_buss_address = models.TextField(db_column='AD_I_BI_BUSS_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_state = models.TextField(db_column='AD_I_BI_STATE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_city = models.TextField(db_column='AD_I_BI_CITY', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_pincode = models.TextField(db_column='AD_I_BI_PINCODE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_comm_premise = models.TextField(db_column='AD_I_BI_COMM_PREMISE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_yrs_ope_from_add = models.TextField(db_column='AD_I_BI_YRS_OPE_FROM_ADD', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_resi_add = models.TextField(db_column='AD_I_BI_BO_RESI_ADD', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_diff_residence_add = models.TextField(db_column='AD_I_BI_BO_DIFF_RESIDENCE_ADD', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_state = models.TextField(db_column='AD_I_BI_BO_STATE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_city = models.TextField(db_column='AD_I_BI_BO_CITY', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_pincode = models.TextField(db_column='AD_I_BI_BO_PINCODE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_co_comm_add = models.TextField(db_column='AD_I_BI_CO_COMM_ADD', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_co_diff_comm_add = models.TextField(db_column='AD_I_BI_CO_DIFF_COMM_ADD', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_co_state = models.TextField(db_column='AD_I_BI_CO_STATE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_co_city = models.TextField(db_column='AD_I_BI_CO_CITY', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_co_pincode = models.TextField(db_column='AD_I_BI_CO_PINCODE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_bo_runs_buss_owned_prop = models.TextField(db_column='AD_I_BI_BO_RUNS_BUSS_OWNED_PROP', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_which_is_prop = models.TextField(db_column='AD_I_BI_WHICH_IS_PROP', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_prop_dtls_buss_run = models.TextField(db_column='AD_I_BI_PROP_DTLS_BUSS_RUN', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_contact_no = models.TextField(db_column='AD_I_BI_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_email_id = models.TextField(db_column='AD_I_BI_EMAIL_ID', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_alt_contact_no = models.TextField(db_column='AD_I_BI_ALT_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_stay_address = models.TextField(db_column='AD_I_BI_STAY_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_prop_details = models.TextField(db_column='AD_I_BI_PROP_DETAILS', blank=True, null=True)  # Field name made lowercase.
    oc_app_od_const_firm = models.CharField(db_column='OC_APP_OD_CONST_FIRM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_company_name = models.CharField(db_column='OC_APP_OD_COMPANY_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_type_industry = models.CharField(db_column='OC_APP_OD_TYPE_INDUSTRY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_nature_co_buss = models.CharField(db_column='OC_APP_OD_NATURE_CO_BUSS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_nature_emp = models.CharField(db_column='OC_APP_OD_NATURE_EMP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_yrs_curr_comp = models.CharField(db_column='OC_APP_OD_YRS_CURR_COMP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_office_add = models.CharField(db_column='OC_APP_OD_OFFICE_ADD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_state = models.CharField(db_column='OC_APP_OD_STATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_city = models.CharField(db_column='OC_APP_OD_CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_pincode = models.CharField(db_column='OC_APP_OD_PINCODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    oc_app_od_designation = models.CharField(db_column='OC_APP_OD_DESIGNATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ad_is_this_loan_renewal = models.CharField(db_column='AD_IS_THIS_LOAN_RENEWAL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ad_isgur_cobor_available = models.CharField(db_column='AD_ISGUR_COBOR_AVAILABLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bd_prior_work_experience = models.TextField(db_column='BD_PRIOR_WORK_EXPERIENCE', blank=True, null=True)  # Field name made lowercase.
    bd_type_of_industry = models.TextField(db_column='BD_TYPE_OF_INDUSTRY', blank=True, null=True)  # Field name made lowercase.
    ad_name_of_company = models.TextField(db_column='AD_NAME_OF_COMPANY', blank=True, null=True)  # Field name made lowercase.
    ad_i_app_od_company_name = models.TextField(db_column='AD_I_APP_OD_COMPANY_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_i_app_od_const_firm = models.TextField(db_column='AD_I_APP_OD_CONST_FIRM', blank=True, null=True)  # Field name made lowercase.
    ad_i_app_od_type_industry = models.TextField(db_column='AD_I_APP_OD_TYPE_INDUSTRY', blank=True, null=True)  # Field name made lowercase.
    ad_i_app_od_nature_co_buss = models.TextField(db_column='AD_I_APP_OD_NATURE_CO_BUSS', blank=True, null=True)  # Field name made lowercase.
    login_sm = models.CharField(db_column='LOGIN_SM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ad_gps_full_address = models.TextField(db_column='AD_GPS_FULL_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    ad_gps_city = models.TextField(db_column='AD_GPS_CITY', blank=True, null=True)  # Field name made lowercase.
    ad_gps_pincode = models.TextField(db_column='AD_GPS_PINCODE', blank=True, null=True)  # Field name made lowercase.
    ad_gps_state = models.TextField(db_column='AD_GPS_STATE', blank=True, null=True)  # Field name made lowercase.
    ad_i_bank_stmt = models.TextField(db_column='AD_I_BANK_STMT', blank=True, null=True)  # Field name made lowercase.
    ad_mobile_info = models.TextField(db_column='AD_MOBILE_INFO', blank=True, null=True)  # Field name made lowercase.
    ad_mobile_version = models.TextField(db_column='AD_MOBILE_VERSION', blank=True, null=True)  # Field name made lowercase.
    ui_flag = models.TextField(db_column='UI_FLAG', blank=True, null=True)  # Field name made lowercase.
    ad_i_dd_narration = models.TextField(db_column='AD_I_DD_NARRATION', blank=True, null=True)  # Field name made lowercase.
    ad_i_dd_type = models.TextField(db_column='AD_I_DD_TYPE', blank=True, null=True)  # Field name made lowercase.
    ad_i_dd_reason = models.TextField(db_column='AD_I_DD_REASON', blank=True, null=True)  # Field name made lowercase.
    ad_reference = models.TextField(db_column='AD_REFERENCE', blank=True, null=True)  # Field name made lowercase.
    analyst_name = models.TextField(db_column='ANALYST_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_aadhar_face_match_score = models.TextField(db_column='AD_AADHAR_FACE_MATCH_SCORE', blank=True, null=True)  # Field name made lowercase.
    ad_pan_face_match_score = models.TextField(db_column='AD_PAN_FACE_MATCH_SCORE', blank=True, null=True)  # Field name made lowercase.
    ad_aadhar_uid_face_match_score = models.TextField(db_column='AD_AADHAR_UID_FACE_MATCH_SCORE', blank=True, null=True)  # Field name made lowercase.
    ad_vkyc = models.TextField(db_column='AD_VKYC', blank=True, null=True)  # Field name made lowercase.
    ad_i_name_extarcted = models.TextField(db_column='AD_I_NAME_EXTARCTED', blank=True, null=True)  # Field name made lowercase.
    ad_salary_income_bank = models.TextField(db_column='AD_SALARY_INCOME_BANK', blank=True, null=True)  # Field name made lowercase.
    ad_vitals_remarks = models.TextField(db_column='AD_VITALS_REMARKS', blank=True, null=True)  # Field name made lowercase.
    auth_salary_slip = models.TextField(db_column='AUTH_SALARY_SLIP', blank=True, null=True)  # Field name made lowercase.
    ad_esign = models.TextField(db_column='AD_ESIGN', blank=True, null=True)  # Field name made lowercase.
    ad_nach = models.TextField(db_column='AD_NACH', blank=True, null=True)  # Field name made lowercase.
    ad_nominee_name = models.TextField(db_column='AD_NOMINEE_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_nominee_relationship = models.TextField(db_column='AD_NOMINEE_RELATIONSHIP', blank=True, null=True)  # Field name made lowercase.
    ad_pendencies = models.TextField(db_column='AD_PENDENCIES', blank=True, null=True)  # Field name made lowercase.
    ad_first_name_pan = models.TextField(db_column='AD_FIRST_NAME_PAN', blank=True, null=True)  # Field name made lowercase.
    ad_last_name_pan = models.TextField(db_column='AD_LAST_NAME_PAN', blank=True, null=True)  # Field name made lowercase.
    ad_last_updated_pan = models.TextField(db_column='AD_LAST_UPDATED_PAN', blank=True, null=True)  # Field name made lowercase.
    ad_middle_name_pan = models.TextField(db_column='AD_MIDDLE_NAME_PAN', blank=True, null=True)  # Field name made lowercase.
    ad_pan_no = models.TextField(db_column='AD_PAN_NO', blank=True, null=True)  # Field name made lowercase.
    ad_pan_status = models.TextField(db_column='AD_PAN_STATUS', blank=True, null=True)  # Field name made lowercase.
    ad_title_pan = models.TextField(db_column='AD_TITLE_PAN', blank=True, null=True)  # Field name made lowercase.
    ad_recent_add = models.IntegerField(db_column='AD_RECENT_ADD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_details'


class ApplicantDetailsLoanClosure(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bal_unpaid_interest = models.IntegerField(db_column='BAL_UNPAID_INTEREST', blank=True, null=True)  # Field name made lowercase.
    bal_unpaid_principal = models.IntegerField(db_column='BAL_UNPAID_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    bal_unpaid_bc = models.IntegerField(db_column='BAL_UNPAID_BC', blank=True, null=True)  # Field name made lowercase.
    bal_unpaid_penal_int = models.IntegerField(db_column='BAL_UNPAID_PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    bal_legal_fees = models.IntegerField(db_column='BAL_LEGAL_FEES', blank=True, null=True)  # Field name made lowercase.
    bal_other_charges = models.IntegerField(db_column='BAL_OTHER_CHARGES', blank=True, null=True)  # Field name made lowercase.
    dis_unapid_int = models.IntegerField(db_column='DIS_UNAPID_INT', blank=True, null=True)  # Field name made lowercase.
    dis_unpaid_principal = models.IntegerField(db_column='DIS_UNPAID_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    dis_unpaid_bc = models.IntegerField(db_column='DIS_UNPAID_BC', blank=True, null=True)  # Field name made lowercase.
    dis_unpaid_penal_int = models.IntegerField(db_column='DIS_UNPAID_PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    dis_legal_fees = models.IntegerField(db_column='DIS_LEGAL_FEES', blank=True, null=True)  # Field name made lowercase.
    dis_other_charges = models.IntegerField(db_column='DIS_OTHER_CHARGES', blank=True, null=True)  # Field name made lowercase.
    writeoff_unpaid_int = models.IntegerField(db_column='WRITEOFF_UNPAID_INT', blank=True, null=True)  # Field name made lowercase.
    writeoff_unpaid_principal = models.IntegerField(db_column='WRITEOFF_UNPAID_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    writeoff_unpaid_bc = models.IntegerField(db_column='WRITEOFF_UNPAID_BC', blank=True, null=True)  # Field name made lowercase.
    writeoff_unpaid_penal_int = models.IntegerField(db_column='WRITEOFF_UNPAID_PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    writeoff_legal_fees = models.IntegerField(db_column='WRITEOFF_LEGAL_FEES', blank=True, null=True)  # Field name made lowercase.
    writeoff_other_charges = models.IntegerField(db_column='WRITEOFF_OTHER_CHARGES', blank=True, null=True)  # Field name made lowercase.
    sett_unpaid_interser = models.IntegerField(db_column='SETT_UNPAID_INTERSER', blank=True, null=True)  # Field name made lowercase.
    sett_unpaid_principal = models.IntegerField(db_column='SETT_UNPAID_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    sett_unpaid_bc = models.IntegerField(db_column='SETT_UNPAID_BC', blank=True, null=True)  # Field name made lowercase.
    sett_unpaid_penal_int = models.IntegerField(db_column='SETT_UNPAID_PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    sett_legal_fee = models.IntegerField(db_column='SETT_LEGAL_FEE', blank=True, null=True)  # Field name made lowercase.
    sett_other_charges = models.IntegerField(db_column='SETT_OTHER_CHARGES', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    writeoff_loan_date = models.DateTimeField(db_column='WRITEOFF_LOAN_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.TextField(db_column='APPROVED_BY', blank=True, null=True)  # Field name made lowercase.
    approval_date = models.DateField(db_column='APPROVAL_DATE', blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='BOOKING_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_details_loan_closure'


class ApplicantDetailsMicro(models.Model):
    id = models.AutoField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', unique=True, max_length=100)  # Field name made lowercase.
    app_type = models.TextField(db_column='APP_TYPE', blank=True, null=True)  # Field name made lowercase.
    app_type_id = models.TextField(db_column='APP_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    ad_i_ref_emp_avai = models.TextField(db_column='AD_I_REF_EMP_AVAI', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_present_occ = models.TextField(db_column='AD_I_OD_PRESENT_OCC', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_const_firm = models.TextField(db_column='AD_I_OD_CONST_FIRM', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_company_name = models.TextField(db_column='AD_I_OD_COMPANY_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_type_industry = models.TextField(db_column='AD_I_OD_TYPE_INDUSTRY', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_nature_co_buss = models.TextField(db_column='AD_I_OD_NATURE_CO_BUSS', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_nature_emp = models.TextField(db_column='AD_I_OD_NATURE_EMP', blank=True, null=True)  # Field name made lowercase.
    ad_i_od_yrs_curr_comp = models.CharField(db_column='AD_I_OD_YRS_CURR_COMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_od_off_id_submitted = models.CharField(db_column='AD_I_OD_OFF_ID_SUBMITTED', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_buss_yrs_ope = models.CharField(db_column='AD_I_BI_BUSS_YRS_OPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_constitution_type = models.CharField(db_column='AD_I_CONSTITUTION_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_nature_of_businees = models.CharField(db_column='AD_I_NATURE_OF_BUSINEES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_type_industry_own_buss = models.CharField(db_column='AD_I_TYPE_INDUSTRY_OWN_BUSS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_own_nature_of_industry = models.CharField(db_column='AD_I_OWN_NATURE_OF_INDUSTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_own_desc_buss = models.CharField(db_column='AD_I_OWN_DESC_BUSS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_nat_pro = models.CharField(db_column='AD_I_SELFEMP_NAT_PRO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_desc_pro = models.CharField(db_column='AD_I_SELFEMP_DESC_PRO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_desc_what_pro = models.CharField(db_column='AD_I_SELFEMP_DESC_WHAT_PRO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_curr_pro = models.IntegerField(db_column='AD_I_SELFEMP_CURR_PRO', blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_how_many = models.IntegerField(db_column='AD_I_SELFEMP_HOW_MANY', blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_comm_pre = models.CharField(db_column='AD_I_SELFEMP_COMM_PRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_selfemp_add_buss = models.CharField(db_column='AD_I_SELFEMP_ADD_BUSS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_borstud_loan_req = models.CharField(db_column='AD_I_BORSTUD_LOAN_REQ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_borstud_type_course = models.CharField(db_column='AD_I_BORSTUD_TYPE_COURSE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_workexp = models.CharField(db_column='AD_I_PASTEMP_WORKEXP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_type_indus = models.TextField(db_column='AD_I_PASTEMP_TYPE_INDUS', blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_name_comp = models.CharField(db_column='AD_I_PASTEMP_NAME_COMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_off_add = models.CharField(db_column='AD_I_PASTEMP_OFF_ADD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_state = models.CharField(db_column='AD_I_PASTEMP_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_city = models.CharField(db_column='AD_I_PASTEMP_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_pincode = models.CharField(db_column='AD_I_PASTEMP_PINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_borr_resi_add = models.CharField(db_column='AD_I_PASTEMP_BORR_RESI_ADD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_add = models.CharField(db_column='AD_I_PASTEMP_RESI_ADD', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_state = models.CharField(db_column='AD_I_PASTEMP_RESI_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_city = models.CharField(db_column='AD_I_PASTEMP_RESI_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_pincode = models.CharField(db_column='AD_I_PASTEMP_RESI_PINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_borr_propno = models.CharField(db_column='AD_I_PASTEMP_RESI_BORR_PROPNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_contact_no = models.CharField(db_column='AD_I_PASTEMP_RESI_CONTACT_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_email_no = models.CharField(db_column='AD_I_PASTEMP_RESI_EMAIL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_resi_alt_contact_no = models.CharField(db_column='AD_I_PASTEMP_RESI_ALT_CONTACT_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_comm_add = models.CharField(db_column='AD_I_PASTEMP_COMM_ADD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_comm_add_one = models.CharField(db_column='AD_I_PASTEMP_COMM_ADD_ONE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_comm_add_sate = models.CharField(db_column='AD_I_PASTEMP_COMM_ADD_SATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_comm_add_city = models.CharField(db_column='AD_I_PASTEMP_COMM_ADD_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_pastemp_comm_add_pincode = models.CharField(db_column='AD_I_PASTEMP_COMM_ADD_PINCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_id_id_proof_doc_pan = models.CharField(db_column='AD_I_ID_ID_PROOF_DOC_PAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_credt_ck_cibil_score = models.CharField(db_column='AD_I_CREDT_CK_CIBIL_SCORE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_othr_demo_asset_home_status = models.CharField(db_column='AD_I_OTHR_DEMO_ASSET_HOME_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_loan_amount = models.CharField(db_column='AD_I_CRD_LOAN_AMOUNT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_end_use_funds = models.CharField(db_column='AD_I_CRD_END_USE_FUNDS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_disbursement_type = models.CharField(db_column='AD_I_CRD_DISBURSEMENT_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_mulple_tranches = models.CharField(db_column='AD_I_CRD_MULPLE_TRANCHES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_mode_disburs = models.CharField(db_column='AD_I_CRD_MODE_DISBURS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_disburs_favor = models.CharField(db_column='AD_I_CRD_DISBURS_FAVOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_bank_name = models.CharField(db_column='AD_I_CRD_BANK_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_no_digit_bank_account_no = models.CharField(db_column='AD_I_CRD_NO_DIGIT_BANK_ACCOUNT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_bank_account_no = models.CharField(db_column='AD_I_CRD_BANK_ACCOUNT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_ifsc_code = models.CharField(db_column='AD_I_CRD_IFSC_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_branch_name = models.CharField(db_column='AD_I_CRD_BRANCH_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ad_i_crd_branch_city = models.CharField(db_column='AD_I_CRD_BRANCH_CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_details_micro'


class ApplicantIndividual(models.Model):
    id = models.AutoField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', unique=True, max_length=30)  # Field name made lowercase.
    app_type_id = models.CharField(db_column='APP_TYPE_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_curr_yrs = models.CharField(db_column='AF_IND_CURR_YRS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_late_mnth = models.CharField(db_column='AF_IND_PICK_MNTH_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_pre_mnth_one = models.CharField(db_column='AF_IND_PICK_MNTH_PRE_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_pre_mnth_two = models.CharField(db_column='AF_IND_PICK_MNTH_PRE_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_prj_an_no_one = models.CharField(db_column='AF_IND_PRJ_AN_NO_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_prj_an_no_two = models.CharField(db_column='AF_IND_PRJ_AN_NO_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_pre_mnth_three = models.CharField(db_column='AF_IND_PICK_MNTH_PRE_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_pre_mnth_four = models.CharField(db_column='AF_IND_PICK_MNTH_PRE_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_pick_mnth_pre_mnth_five = models.CharField(db_column='AF_IND_PICK_MNTH_PRE_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_inc_late_mnth = models.CharField(db_column='AF_IND_TOTAL_INC_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prv_mnth_one = models.CharField(db_column='AF_IND_TOTAL_PRV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prv_mnth_two = models.CharField(db_column='AF_IND_TOTAL_PRV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prj_an_late_mnth_one = models.CharField(db_column='AF_IND_TOTAL_PRJ_AN_LATE_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prj_an_late_mnth_two = models.CharField(db_column='AF_IND_TOTAL_PRJ_AN_LATE_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prv_mnth_three = models.CharField(db_column='AF_IND_TOTAL_PRV_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prv_mnth_four = models.CharField(db_column='AF_IND_TOTAL_PRV_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_total_prv_mnth_five = models.CharField(db_column='AF_IND_TOTAL_PRV_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_exp_late_mnth = models.CharField(db_column='AF_IND_EXP_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_exp_prv_mnth_one = models.CharField(db_column='AF_IND_EXP_PRV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_exp_prv_mnth_two = models.CharField(db_column='AF_IND_EXP_PRV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_exp_proj_annl_one = models.CharField(db_column='AF_IND_EXP_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_exp_proj_annl_two = models.CharField(db_column='AF_IND_EXP_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_late_mnth = models.CharField(db_column='AF_IND_COST_SOLD_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_prev_one = models.CharField(db_column='AF_IND_COST_SOLD_PREV_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_prev_two = models.CharField(db_column='AF_IND_COST_SOLD_PREV_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_proj_annl_one = models.CharField(db_column='AF_IND_COST_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_proj_annl_two = models.CharField(db_column='AF_IND_COST_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_prev_three = models.CharField(db_column='AF_IND_COST_SOLD_PREV_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_prev_four = models.CharField(db_column='AF_IND_COST_SOLD_PREV_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cost_sold_prev_five = models.CharField(db_column='AF_IND_COST_SOLD_PREV_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_adm_over_late_mnth = models.CharField(db_column='AF_IND_ADM_OVER_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_adm_over_prv_mnth_one = models.CharField(db_column='AF_IND_ADM_OVER_PRV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_adm_over_prv_mnth_two = models.CharField(db_column='AF_IND_ADM_OVER_PRV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_adm_proj_annl_one = models.CharField(db_column='AF_IND_ADM_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_adm_proj_annl_two = models.CharField(db_column='AF_IND_ADM_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_other_late_mnth = models.CharField(db_column='AF_IND_OTHER_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_other_prv_mnth_one = models.CharField(db_column='AF_IND_OTHER_PRV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_other_prv_mnth_two = models.CharField(db_column='AF_IND_OTHER_PRV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_other_proj_annl_one = models.CharField(db_column='AF_IND_OTHER_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_proj_annl_no_two = models.CharField(db_column='AF_IND_PROJ_ANNL_NO_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_opert_exp_late_mnth = models.CharField(db_column='AF_IND_OPERT_EXP_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_opert_prev_mnth_one = models.CharField(db_column='AF_IND_OPERT_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_opert_prev_mnth_two = models.CharField(db_column='AF_IND_OPERT_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_opert_proj_annul_one = models.CharField(db_column='AF_IND_OPERT_PROJ_ANNUL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_opert_proj_annual_two = models.CharField(db_column='AF_IND_OPERT_PROJ_ANNUAL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_deprt_late_mnth = models.CharField(db_column='AF_IND_DEPRT_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_deprt_prev_mnth_one = models.CharField(db_column='AF_IND_DEPRT_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_deprt_prev_mnth_two = models.CharField(db_column='AF_IND_DEPRT_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_deprt_proj_annul_one = models.CharField(db_column='AF_IND_DEPRT_PROJ_ANNUL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_deprt_proj_annul_two = models.CharField(db_column='AF_IND_DEPRT_PROJ_ANNUL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_late_mnth = models.CharField(db_column='AF_IND_FINACE_COST_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_prev_mnth_one = models.CharField(db_column='AF_IND_FINACE_COST_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_prev_mnth_two = models.CharField(db_column='AF_IND_FINACE_COST_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_prev_mnth_three = models.CharField(db_column='AF_IND_FINACE_COST_PREV_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_prev_mnth_four = models.CharField(db_column='AF_IND_FINACE_COST_PREV_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_cost_prev_mnth_five = models.CharField(db_column='AF_IND_FINACE_COST_PREV_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_proj_annl_one = models.CharField(db_column='AF_IND_FINACE_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_finace_proj_annl_two = models.CharField(db_column='AF_IND_FINACE_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_late_mnth = models.CharField(db_column='AF_IND_EBIDTA_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_prev_mnth_one = models.CharField(db_column='AF_IND_EBIDTA_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_prev_mnth_two = models.CharField(db_column='AF_IND_EBIDTA_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_prev_mnth_three = models.CharField(db_column='AF_IND_EBIDTA_PREV_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_prev_mnth_four = models.CharField(db_column='AF_IND_EBIDTA_PREV_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_prev_mnth_five = models.CharField(db_column='AF_IND_EBIDTA_PREV_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_proj_annl_one = models.CharField(db_column='AF_IND_EBIDTA_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_ebidta_proj_annl_two = models.CharField(db_column='AF_IND_EBIDTA_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_late_month = models.CharField(db_column='AF_IND_NET_LATE_MONTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_prev_month_one = models.CharField(db_column='AF_IND_NET_PREV_MONTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_prev_month_two = models.CharField(db_column='AF_IND_NET_PREV_MONTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_proj_annl_no_one = models.CharField(db_column='AF_IND_NET_PROJ_ANNL_NO_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_proj_annl_no_two = models.CharField(db_column='AF_IND_NET_PROJ_ANNL_NO_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_late_mnth = models.CharField(db_column='AF_IND_TAX_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_prev_mnth_one = models.CharField(db_column='AF_IND_TAX_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_prev_mnth_two = models.CharField(db_column='AF_IND_TAX_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_prev_mnth_three = models.CharField(db_column='AF_IND_TAX_PREV_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_prev_mnth_four = models.CharField(db_column='AF_IND_TAX_PREV_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_prev_mnth_five = models.CharField(db_column='AF_IND_TAX_PREV_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_proj_annl_one = models.CharField(db_column='AF_IND_TAX_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_tax_proj_annl_two = models.CharField(db_column='AF_IND_TAX_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_profit_late_mnth = models.CharField(db_column='AF_IND_NET_PROFIT_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_profit_prev_mnth_one = models.CharField(db_column='AF_IND_NET_PROFIT_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_profit_prev_mnth_two = models.CharField(db_column='AF_IND_NET_PROFIT_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_profit_proj_annl_one = models.CharField(db_column='AF_IND_NET_PROFIT_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_net_profit_proj_annl_two = models.CharField(db_column='AF_IND_NET_PROFIT_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cash_profit_late_mnth = models.CharField(db_column='AF_IND_CASH_PROFIT_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cash_profit_prev_mnth_one = models.CharField(db_column='AF_IND_CASH_PROFIT_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cash_profit_prev_mnth_two = models.CharField(db_column='AF_IND_CASH_PROFIT_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cash_profit_proj_annl_one = models.CharField(db_column='AF_IND_CASH_PROFIT_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_cash_profit_proj_annl_two = models.CharField(db_column='AF_IND_CASH_PROFIT_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_late_mnth = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_prev_mnth_one = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PREV_MNTH_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_prev_mnth_two = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PREV_MNTH_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_prev_mnth_three = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PREV_MNTH_THREE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_prev_mnth_four = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PREV_MNTH_FOUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_prev_mnth_five = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PREV_MNTH_FIVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_proj_annl_one = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PROJ_ANNL_ONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_loan_pri_instl_proj_annl_two = models.CharField(db_column='AF_IND_LOAN_PRI_INSTL_PROJ_ANNL_TWO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_late_mnth = models.CharField(db_column='AF_IND_DEBT_SER_COV_LATE_MNTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_prev_mnth_one = models.CharField(db_column='AF_IND_DEBT_SER_COV_PREV_MNTH_ONE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_prev_mnth_two = models.CharField(db_column='AF_IND_DEBT_SER_COV_PREV_MNTH_TWO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_prev_mnth_three = models.CharField(db_column='AF_IND_DEBT_SER_COV_PREV_MNTH_THREE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_prev_mnth_four = models.CharField(db_column='AF_IND_DEBT_SER_COV_PREV_MNTH_FOUR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_prev_mnth_five = models.CharField(db_column='AF_IND_DEBT_SER_COV_PREV_MNTH_FIVE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_proj_annl_one = models.CharField(db_column='AF_IND_DEBT_SER_COV_PROJ_ANNL_ONE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    af_ind_debt_ser_cov_proj_annl_two = models.CharField(db_column='AF_IND_DEBT_SER_COV_PROJ_ANNL_TWO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    business_individual_prev2 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV2', blank=True, null=True)  # Field name made lowercase.
    business_individual_prev1 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV1', blank=True, null=True)  # Field name made lowercase.
    business_individual_current = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_CURRENT', blank=True, null=True)  # Field name made lowercase.
    business_individual_proj1 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PROJ1', blank=True, null=True)  # Field name made lowercase.
    business_individual_proj2 = models.DecimalField(db_column='BUSINESS_INDIVIDUAL_PROJ2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    business_individual_prev3 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV3', blank=True, null=True)  # Field name made lowercase.
    business_individual_prev4 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV4', blank=True, null=True)  # Field name made lowercase.
    business_individual_prev5 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV5', blank=True, null=True)  # Field name made lowercase.
    business_individual_prev6 = models.BigIntegerField(db_column='BUSINESS_INDIVIDUAL_PREV6', blank=True, null=True)  # Field name made lowercase.
    other_individual_prev2 = models.BigIntegerField(db_column='OTHER_INDIVIDUAL_PREV2', blank=True, null=True)  # Field name made lowercase.
    other_individual_prev1 = models.BigIntegerField(db_column='OTHER_INDIVIDUAL_PREV1', blank=True, null=True)  # Field name made lowercase.
    other_individual_current = models.BigIntegerField(db_column='OTHER_INDIVIDUAL_CURRENT', blank=True, null=True)  # Field name made lowercase.
    other_individual_proj1 = models.BigIntegerField(db_column='OTHER_INDIVIDUAL_PROJ1', blank=True, null=True)  # Field name made lowercase.
    other_individual_proj2 = models.DecimalField(db_column='OTHER_INDIVIDUAL_PROJ2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev1 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev2 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev3 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev4 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV4', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev5 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    household_income_prev6 = models.DecimalField(db_column='HOUSEHOLD_INCOME_PREV6', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev1 = models.DecimalField(db_column='OTHER_INCOME_PREV1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev2 = models.DecimalField(db_column='OTHER_INCOME_PREV2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev3 = models.DecimalField(db_column='OTHER_INCOME_PREV3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev4 = models.DecimalField(db_column='OTHER_INCOME_PREV4', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev5 = models.DecimalField(db_column='OTHER_INCOME_PREV5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other_income_prev6 = models.DecimalField(db_column='OTHER_INCOME_PREV6', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp1 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp2 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp3 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp4 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP4', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp5 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_oper_exp6 = models.DecimalField(db_column='AF_IND_BUSS_OPER_EXP6', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent1 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent2 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent3 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent4 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT4', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent5 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_a_rent6 = models.DecimalField(db_column='AF_IND_BUSS_A_RENT6', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity1 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity2 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity3 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity4 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY4', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity5 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_b_electricity6 = models.DecimalField(db_column='AF_IND_BUSS_B_ELECTRICITY6', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel1 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL1', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel2 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL2', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel3 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL3', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel4 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL4', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel5 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL5', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_c_fuel6 = models.BigIntegerField(db_column='AF_IND_BUSS_C_FUEL6', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal1 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL1', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal2 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL2', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal3 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL3', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal4 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL4', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal5 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL5', blank=True, null=True)  # Field name made lowercase.
    af_ind_buss_d_staff_sal6 = models.BigIntegerField(db_column='AF_IND_BUSS_D_STAFF_SAL6', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others1 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS1', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others2 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS2', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others3 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS3', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others4 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS4', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others5 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS5', blank=True, null=True)  # Field name made lowercase.
    af_ind_all_others6 = models.BigIntegerField(db_column='AF_IND_ALL_OTHERS6', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp1 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP1', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp2 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP2', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp3 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP3', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp4 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP4', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp5 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP5', blank=True, null=True)  # Field name made lowercase.
    af_ind_household_exp6 = models.BigIntegerField(db_column='AF_IND_HOUSEHOLD_EXP6', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens1 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS1', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens2 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS2', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens3 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS3', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens4 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS4', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens5 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS5', blank=True, null=True)  # Field name made lowercase.
    af_ind_oper_expens6 = models.BigIntegerField(db_column='AF_IND_OPER_EXPENS6', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_one = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_ONE', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_two = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_TWO', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_three = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_THREE', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_four = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_FOUR', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_five = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_FIVE', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov1 = models.BigIntegerField(db_column='AF_IND_MNT_PROV1', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov2 = models.BigIntegerField(db_column='AF_IND_MNT_PROV2', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov3 = models.BigIntegerField(db_column='AF_IND_MNT_PROV3', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov4 = models.BigIntegerField(db_column='AF_IND_MNT_PROV4', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov5 = models.BigIntegerField(db_column='AF_IND_MNT_PROV5', blank=True, null=True)  # Field name made lowercase.
    af_ind_mnt_prov6 = models.BigIntegerField(db_column='AF_IND_MNT_PROV6', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_one = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_ONE', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_two = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_TWO', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_three = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_THREE', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_four = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_FOUR', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_five = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_FIVE', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_hand_six = models.BigIntegerField(db_column='AF_IND_NET_CASH_HAND_SIX', blank=True, null=True)  # Field name made lowercase.
    af_ind_net_cash_in_hand_six = models.BigIntegerField(db_column='AF_IND_NET_CASH_IN_HAND_SIX', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    business_individual_extracted_prev1 = models.CharField(db_column='BUSINESS_INDIVIDUAL_EXTRACTED_PREV1', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_individual'


class ApplicantPaymentSchedule(models.Model):
    id = models.AutoField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=30)  # Field name made lowercase.
    emi_date = models.DateField(db_column='EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    loan_op_bal = models.IntegerField(db_column='LOAN_OP_BAL', blank=True, null=True)  # Field name made lowercase.
    principal_repayment = models.IntegerField(db_column='PRINCIPAL_REPAYMENT', blank=True, null=True)  # Field name made lowercase.
    int_payment = models.IntegerField(db_column='INT_PAYMENT', blank=True, null=True)  # Field name made lowercase.
    emi_amount = models.IntegerField(db_column='EMI_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    penal_interest = models.IntegerField(db_column='PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    loan_cl_bal = models.IntegerField(db_column='LOAN_CL_BAL', blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    emi_collected = models.IntegerField(db_column='EMI_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    extra_payment = models.IntegerField(db_column='EXTRA_PAYMENT', blank=True, null=True)  # Field name made lowercase.
    dpd = models.IntegerField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    penal_int_collected = models.IntegerField(db_column='PENAL_INT_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    penal_int_collec_date = models.DateField(db_column='PENAL_INT_COLLEC_DATE', blank=True, null=True)  # Field name made lowercase.
    collected_by = models.CharField(db_column='COLLECTED_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    disbursement = models.IntegerField(db_column='DISBURSEMENT', blank=True, null=True)  # Field name made lowercase.
    true_balance = models.IntegerField(db_column='TRUE_BALANCE', blank=True, null=True)  # Field name made lowercase.
    closing_date = models.DateField(db_column='CLOSING_DATE', blank=True, null=True)  # Field name made lowercase.
    actual_emi_collected = models.CharField(db_column='ACTUAL_EMI_COLLECTED', max_length=45, blank=True, null=True)  # Field name made lowercase.
    penal_int_collection_method = models.CharField(db_column='PENAL_INT_COLLECTION_METHOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bounce_charges = models.IntegerField(db_column='BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_collected = models.IntegerField(db_column='BOUNCE_CHARGES_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_collection_date = models.DateField(db_column='BOUNCE_CHARGES_COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_collection_method = models.CharField(db_column='BOUNCE_CHARGES_COLLECTION_METHOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    penal_interest_inc_gst = models.IntegerField(db_column='PENAL_INTEREST_INC_GST', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_inc_gst = models.IntegerField(db_column='BOUNCE_CHARGES_INC_GST', blank=True, null=True)  # Field name made lowercase.
    emi_collection_time = models.TimeField(db_column='EMI_COLLECTION_TIME', blank=True, null=True)  # Field name made lowercase.
    carry_forward_amount = models.IntegerField(db_column='CARRY_FORWARD_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_payment_schedule'


class ApplicantPaymentScheduleBreakup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emi_date = models.DateField(db_column='EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    emi_overdue = models.FloatField(db_column='EMI_OVERDUE', blank=True, null=True)  # Field name made lowercase.
    penal_interest = models.FloatField(db_column='PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    gst_penal_interest = models.FloatField(db_column='GST_PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    emi_collected = models.FloatField(db_column='EMI_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    other_charges = models.FloatField(db_column='OTHER_CHARGES', blank=True, null=True)  # Field name made lowercase.
    other_charges_type = models.CharField(db_column='OTHER_CHARGES_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    other_gst_component = models.FloatField(db_column='OTHER_GST_COMPONENT', blank=True, null=True)  # Field name made lowercase.
    cash_collected = models.FloatField(db_column='CASH_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    interest_paid = models.IntegerField(db_column='INTEREST_PAID', blank=True, null=True)  # Field name made lowercase.
    principal_paid = models.IntegerField(db_column='PRINCIPAL_PAID', blank=True, null=True)  # Field name made lowercase.
    interest_arrears = models.IntegerField(db_column='INTEREST_ARREARS', blank=True, null=True)  # Field name made lowercase.
    principal_arrears = models.IntegerField(db_column='PRINCIPAL_ARREARS', blank=True, null=True)  # Field name made lowercase.
    bounce_charges = models.IntegerField(db_column='BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    gst_bc = models.IntegerField(db_column='GST_BC', blank=True, null=True)  # Field name made lowercase.
    surplus = models.IntegerField(db_column='SURPLUS', blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    int_cur_month = models.IntegerField(db_column='INT_CUR_MONTH', blank=True, null=True)  # Field name made lowercase.
    prepayment_flag = models.CharField(db_column='PREPAYMENT_FLAG', max_length=45, blank=True, null=True)  # Field name made lowercase.
    advance_emi = models.CharField(db_column='ADVANCE_EMI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    excess_collected = models.CharField(db_column='EXCESS_COLLECTED', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_payment_schedule_breakup'


class ApplicantPaymentScheduleDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emi_date = models.DateField(db_column='EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    op_bal = models.IntegerField(db_column='OP_BAL', blank=True, null=True)  # Field name made lowercase.
    emi_due = models.IntegerField(db_column='EMI_DUE', blank=True, null=True)  # Field name made lowercase.
    cl_bal = models.IntegerField(db_column='CL_BAL', blank=True, null=True)  # Field name made lowercase.
    paid_amt = models.IntegerField(db_column='PAID_AMT', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    unpaid_emi = models.IntegerField(db_column='UNPAID_EMI', blank=True, null=True)  # Field name made lowercase.
    unpaid_total = models.IntegerField(db_column='UNPAID_TOTAL', blank=True, null=True)  # Field name made lowercase.
    ia_op = models.IntegerField(db_column='IA_OP', blank=True, null=True)  # Field name made lowercase.
    ia_add = models.IntegerField(db_column='IA_ADD', blank=True, null=True)  # Field name made lowercase.
    ia_paid = models.IntegerField(db_column='IA_PAID', blank=True, null=True)  # Field name made lowercase.
    ia_cl = models.IntegerField(db_column='IA_CL', blank=True, null=True)  # Field name made lowercase.
    pa_op = models.IntegerField(db_column='PA_OP', blank=True, null=True)  # Field name made lowercase.
    pa_add = models.IntegerField(db_column='PA_ADD', blank=True, null=True)  # Field name made lowercase.
    pa_paid = models.IntegerField(db_column='PA_PAID', blank=True, null=True)  # Field name made lowercase.
    pa_cl = models.IntegerField(db_column='PA_CL', blank=True, null=True)  # Field name made lowercase.
    interest_due = models.IntegerField(db_column='INTEREST_DUE', blank=True, null=True)  # Field name made lowercase.
    interest_paid = models.IntegerField(db_column='INTEREST_PAID', blank=True, null=True)  # Field name made lowercase.
    principal_due = models.IntegerField(db_column='PRINCIPAL_DUE', blank=True, null=True)  # Field name made lowercase.
    principal_paid = models.IntegerField(db_column='PRINCIPAL_PAID', blank=True, null=True)  # Field name made lowercase.
    short_amt = models.IntegerField(db_column='SHORT_AMT', blank=True, null=True)  # Field name made lowercase.
    surplus = models.IntegerField(db_column='SURPLUS', blank=True, null=True)  # Field name made lowercase.
    dpd = models.IntegerField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    pi_op = models.IntegerField(db_column='PI_OP', blank=True, null=True)  # Field name made lowercase.
    pi_add = models.IntegerField(db_column='PI_ADD', blank=True, null=True)  # Field name made lowercase.
    pi_paid = models.IntegerField(db_column='PI_PAID', blank=True, null=True)  # Field name made lowercase.
    pi_cl = models.IntegerField(db_column='PI_CL', blank=True, null=True)  # Field name made lowercase.
    bc_flag = models.IntegerField(db_column='BC_FLAG', blank=True, null=True)  # Field name made lowercase.
    bc_op = models.IntegerField(db_column='BC_OP', blank=True, null=True)  # Field name made lowercase.
    bc_add = models.IntegerField(db_column='BC_ADD', blank=True, null=True)  # Field name made lowercase.
    bc_paid = models.IntegerField(db_column='BC_PAID', blank=True, null=True)  # Field name made lowercase.
    bc_cl = models.IntegerField(db_column='BC_CL', blank=True, null=True)  # Field name made lowercase.
    emi_due_cumm = models.IntegerField(db_column='EMI_DUE_CUMM', blank=True, null=True)  # Field name made lowercase.
    total_due = models.IntegerField(db_column='TOTAL_DUE', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    interest_current_month = models.IntegerField(db_column='INTEREST_CURRENT_MONTH', blank=True, null=True)  # Field name made lowercase.
    interest_current_month_paid = models.IntegerField(db_column='INTEREST_CURRENT_MONTH_PAID', blank=True, null=True)  # Field name made lowercase.
    month_end_date = models.DateField(db_column='MONTH_END_DATE', blank=True, null=True)  # Field name made lowercase.
    max_days = models.IntegerField(db_column='MAX_DAYS', blank=True, null=True)  # Field name made lowercase.
    current_month_days = models.IntegerField(db_column='CURRENT_MONTH_DAYS', blank=True, null=True)  # Field name made lowercase.
    applicable_days = models.IntegerField(db_column='APPLICABLE_DAYS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applicant_payment_schedule_details'


class AssignStatus(models.Model):
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status_emi_date = models.DateField(db_column='STATUS_EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    account_class_status = models.IntegerField(db_column='ACCOUNT_CLASS_STATUS', blank=True, null=True)  # Field name made lowercase.
    dpd_classification = models.CharField(db_column='DPD_CLASSIFICATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reason_for_change = models.CharField(db_column='REASON_FOR_CHANGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emi_date_format = models.DateField(db_column='EMI_DATE_FORMAT', blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='BOOKING_DATE', blank=True, null=True)  # Field name made lowercase.
    modified_code = models.CharField(db_column='MODIFIED_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modified_status = models.CharField(db_column='MODIFIED_STATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modified_class = models.CharField(db_column='MODIFIED_CLASS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sys_status = models.CharField(db_column='SYS_STATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sys_code = models.CharField(db_column='SYS_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sys_class = models.CharField(db_column='SYS_CLASS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sys_date = models.DateField(db_column='SYS_DATE', blank=True, null=True)  # Field name made lowercase.
    active_close_flag = models.IntegerField(db_column='ACTIVE_CLOSE_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assign_status'


class CloseCase0(models.Model):
    sanction_id = models.CharField(db_column='SANCTION_ID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    form_status = models.IntegerField(db_column='FORM_STATUS', blank=True, null=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_first_name = models.TextField(db_column='AD_APPLICANT_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_surname = models.TextField(db_column='AD_APPLICANT_SURNAME', blank=True, null=True)  # Field name made lowercase.
    ld_loan_amt_req = models.CharField(db_column='LD_LOAN_AMT_REQ', max_length=90, blank=True, null=True)  # Field name made lowercase.
    ad_applicant_pan_no = models.TextField(db_column='AD_APPLICANT_PAN_NO', blank=True, null=True)  # Field name made lowercase.
    ad_applicant_aadhar_no = models.TextField(db_column='AD_APPLICANT_AADHAR_NO', blank=True, null=True)  # Field name made lowercase.
    ld_loan_tenur = models.CharField(db_column='LD_LOAN_TENUR', max_length=90, blank=True, null=True)  # Field name made lowercase.
    loan_product_id = models.CharField(db_column='LOAN_PRODUCT_ID', max_length=75, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    loan_id = models.CharField(db_column='LOAN_ID', max_length=300, blank=True, null=True)  # Field name made lowercase.
    sanction_limit = models.CharField(db_column='SANCTION_LIMIT', max_length=75, blank=True, null=True)  # Field name made lowercase.
    loan_sanction_date = models.DateTimeField(db_column='LOAN_SANCTION_DATE', blank=True, null=True)  # Field name made lowercase.
    total_amount_disburse = models.DecimalField(db_column='TOTAL_AMOUNT_DISBURSE', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rate_of_interest = models.FloatField(db_column='RATE_OF_INTEREST', blank=True, null=True)  # Field name made lowercase.
    loan_tenure_in_months = models.CharField(db_column='LOAN_TENURE_IN_MONTHS', max_length=75, blank=True, null=True)  # Field name made lowercase.
    upload_sanction_letter = models.CharField(db_column='UPLOAD_SANCTION_LETTER', max_length=75, blank=True, null=True)  # Field name made lowercase.
    is_document_executed = models.IntegerField(db_column='IS_DOCUMENT_EXECUTED', blank=True, null=True)  # Field name made lowercase.
    processing_fee = models.DecimalField(db_column='PROCESSING_FEE', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    facility_type = models.CharField(db_column='FACILITY_TYPE', max_length=75, blank=True, null=True)  # Field name made lowercase.
    security_package = models.CharField(db_column='SECURITY_PACKAGE', max_length=75, blank=True, null=True)  # Field name made lowercase.
    master_notification_history = models.CharField(db_column='MASTER_NOTIFICATION_HISTORY', max_length=75, blank=True, null=True)  # Field name made lowercase.
    bp_id = models.CharField(db_column='BP_ID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sm_id = models.CharField(db_column='SM_ID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    agency_id = models.CharField(db_column='AGENCY_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    agent_id = models.CharField(db_column='AGENT_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    lodger_id = models.CharField(db_column='LODGER_ID', max_length=90, blank=True, null=True)  # Field name made lowercase.
    loan_amount_sanctioned = models.DecimalField(db_column='LOAN_AMOUNT_SANCTIONED', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    processing_fee_rs = models.DecimalField(db_column='PROCESSING_FEE_RS', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    amount_repaid = models.DecimalField(db_column='AMOUNT_REPAID', max_digits=14, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    balance_loan = models.CharField(db_column='BALANCE_LOAN', max_length=135, blank=True, null=True)  # Field name made lowercase.
    ad_i_bi_contact_no = models.TextField(db_column='AD_I_BI_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    ad_loan_type = models.TextField(db_column='AD_LOAN_TYPE', blank=True, null=True)  # Field name made lowercase.
    sum_int_payment = models.DecimalField(db_column='SUM_INT_PAYMENT', max_digits=33, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'close_case0'


class ControlSetting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    financial_year = models.CharField(db_column='FINANCIAL_YEAR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fy_start_date = models.DateField(db_column='FY_START_DATE', blank=True, null=True)  # Field name made lowercase.
    fy_end_date = models.DateField(db_column='FY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    gst_processing_fee = models.TextField(db_column='GST_PROCESSING_FEE', blank=True, null=True)  # Field name made lowercase.
    gst_bounce_charges = models.TextField(db_column='GST_BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    gst_penal_interest = models.TextField(db_column='GST_PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    sma_class_days = models.TextField(db_column='SMA_CLASS_DAYS', blank=True, null=True)  # Field name made lowercase.
    npa_class_days = models.TextField(db_column='NPA_CLASS_DAYS', blank=True, null=True)  # Field name made lowercase.
    sub_class_days = models.TextField(db_column='SUB_CLASS_DAYS', blank=True, null=True)  # Field name made lowercase.
    dbt_class_days = models.TextField(db_column='DBT_CLASS_DAYS', blank=True, null=True)  # Field name made lowercase.
    interest_accrual_stop_days = models.TextField(db_column='INTEREST_ACCRUAL_STOP_DAYS', blank=True, null=True)  # Field name made lowercase.
    product_code = models.TextField(db_column='PRODUCT_CODE', blank=True, null=True)  # Field name made lowercase.
    upto_50k = models.TextField(db_column='UPTO_50K', blank=True, null=True)  # Field name made lowercase.
    from_50k_1l = models.TextField(db_column='FROM_50K_1L', blank=True, null=True)  # Field name made lowercase.
    above_1l = models.TextField(db_column='ABOVE_1L', blank=True, null=True)  # Field name made lowercase.
    stamp_duty = models.TextField(db_column='STAMP_DUTY', blank=True, null=True)  # Field name made lowercase.
    admin_charges = models.TextField(db_column='ADMIN_CHARGES', blank=True, null=True)  # Field name made lowercase.
    commitment_fees = models.TextField(db_column='COMMITMENT_FEES', blank=True, null=True)  # Field name made lowercase.
    penal_interest = models.TextField(db_column='PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    prepayment_penalty = models.TextField(db_column='PREPAYMENT_PENALTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'control_setting'


class DataAccstatChart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    st_value = models.IntegerField(db_column='ST_VALUE', blank=True, null=True)  # Field name made lowercase.
    st_count = models.IntegerField(db_column='ST_COUNT', blank=True, null=True)  # Field name made lowercase.
    npa_value = models.IntegerField(db_column='NPA_VALUE', blank=True, null=True)  # Field name made lowercase.
    npa_count = models.IntegerField(db_column='NPA_COUNT', blank=True, null=True)  # Field name made lowercase.
    fin_year = models.CharField(db_column='FIN_YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_accstat_chart'


class DataBwChart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    regular_val = models.IntegerField(db_column='REGULAR_VAL', blank=True, null=True)  # Field name made lowercase.
    regualar_count = models.IntegerField(db_column='REGUALAR_COUNT', blank=True, null=True)  # Field name made lowercase.
    m0_val = models.IntegerField(db_column='M0_VAL', blank=True, null=True)  # Field name made lowercase.
    m0_count = models.IntegerField(db_column='M0_COUNT', blank=True, null=True)  # Field name made lowercase.
    unpaid_val = models.IntegerField(db_column='UNPAID_VAL', blank=True, null=True)  # Field name made lowercase.
    unpaid_count = models.IntegerField(db_column='UNPAID_COUNT', blank=True, null=True)  # Field name made lowercase.
    m1_val = models.IntegerField(db_column='M1_VAL', blank=True, null=True)  # Field name made lowercase.
    m1_count = models.IntegerField(db_column='M1_COUNT', blank=True, null=True)  # Field name made lowercase.
    m2_val = models.IntegerField(db_column='M2_VAL', blank=True, null=True)  # Field name made lowercase.
    m2_count = models.IntegerField(db_column='M2_COUNT', blank=True, null=True)  # Field name made lowercase.
    sma_1_val = models.IntegerField(db_column='SMA_1_VAL', blank=True, null=True)  # Field name made lowercase.
    sma_1_count = models.IntegerField(db_column='SMA_1_COUNT', blank=True, null=True)  # Field name made lowercase.
    sma_2_val = models.IntegerField(db_column='SMA_2_VAL', blank=True, null=True)  # Field name made lowercase.
    sma_2_count = models.IntegerField(db_column='SMA_2_COUNT', blank=True, null=True)  # Field name made lowercase.
    sma_3_val = models.IntegerField(db_column='SMA_3_VAL', blank=True, null=True)  # Field name made lowercase.
    sma_3_count = models.IntegerField(db_column='SMA_3_COUNT', blank=True, null=True)  # Field name made lowercase.
    npa_val = models.IntegerField(db_column='NPA_VAL', blank=True, null=True)  # Field name made lowercase.
    npa_count = models.IntegerField(db_column='NPA_COUNT', blank=True, null=True)  # Field name made lowercase.
    fin_year = models.CharField(db_column='FIN_YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    active_outs = models.IntegerField(db_column='ACTIVE_OUTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_bw_chart'


class EmiCollectionTemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emi_date = models.DateField(db_column='EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    prepay_flag = models.CharField(db_column='PREPAY_FLAG', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_collection_temp'


class EmiControlParam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rate_pm_m3 = models.TextField(db_column='RATE_PM_M3', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_m3 = models.TextField(db_column='BOUNCE_CHARGES_M3', blank=True, null=True)  # Field name made lowercase.
    penal_interest_m3 = models.TextField(db_column='PENAL_INTEREST_M3', blank=True, null=True)  # Field name made lowercase.
    instalments_m3 = models.TextField(db_column='INSTALMENTS_M3', blank=True, null=True)  # Field name made lowercase.
    rate_pm_m4 = models.TextField(db_column='RATE_PM_M4', blank=True, null=True)  # Field name made lowercase.
    bounce_charges_m4 = models.TextField(db_column='BOUNCE_CHARGES_M4', blank=True, null=True)  # Field name made lowercase.
    penal_interest_m4 = models.TextField(db_column='PENAL_INTEREST_M4', blank=True, null=True)  # Field name made lowercase.
    instalments_m4 = models.TextField(db_column='INSTALMENTS_M4', blank=True, null=True)  # Field name made lowercase.
    threshold = models.TextField(db_column='THRESHOLD', blank=True, null=True)  # Field name made lowercase.
    npa_classification_days = models.TextField(db_column='NPA_CLASSIFICATION_DAYS', blank=True, null=True)  # Field name made lowercase.
    gst_rates_fees = models.TextField(db_column='GST_RATES_FEES', blank=True, null=True)  # Field name made lowercase.
    gst_rates_bounce_charges = models.TextField(db_column='GST_RATES_BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    gst_rates_interest = models.TextField(db_column='GST_RATES_INTEREST', blank=True, null=True)  # Field name made lowercase.
    gst_rates_penal_interest = models.TextField(db_column='GST_RATES_PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    foreclosure_param = models.TextField(db_column='FORECLOSURE_PARAM', blank=True, null=True)  # Field name made lowercase.
    end_period_reversal = models.TextField(db_column='END_PERIOD_REVERSAL', blank=True, null=True)  # Field name made lowercase.
    account_closure_status = models.CharField(db_column='ACCOUNT_CLOSURE_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.
    sma_classification_days = models.CharField(db_column='SMA_CLASSIFICATION_DAYS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    restructuring_month = models.CharField(db_column='RESTRUCTURING_MONTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    restructuring_emi = models.CharField(db_column='RESTRUCTURING_EMI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    restructuring_date = models.DateField(db_column='RESTRUCTURING_DATE', blank=True, null=True)  # Field name made lowercase.
    restructuring_reason = models.TextField(db_column='RESTRUCTURING_REASON', blank=True, null=True)  # Field name made lowercase.
    reason_m3 = models.TextField(db_column='REASON_M3', blank=True, null=True)  # Field name made lowercase.
    reason_m4 = models.TextField(db_column='REASON_M4', blank=True, null=True)  # Field name made lowercase.
    classification_reason = models.TextField(db_column='CLASSIFICATION_REASON', blank=True, null=True)  # Field name made lowercase.
    prepayment_flag = models.CharField(db_column='PREPAYMENT_FLAG', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_control_param'


class EmiIncomeAccounting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    borrower_account_date = models.DateField(db_column='BORROWER_ACCOUNT_DATE', blank=True, null=True)  # Field name made lowercase.
    borrower_account_dr = models.TextField(db_column='BORROWER_ACCOUNT_DR', blank=True, null=True)  # Field name made lowercase.
    borrower_account_coll_date = models.DateField(db_column='BORROWER_ACCOUNT_COLL_DATE', blank=True, null=True)  # Field name made lowercase.
    borrower_account_cr = models.TextField(db_column='BORROWER_ACCOUNT_CR', blank=True, null=True)  # Field name made lowercase.
    interest_income_cr = models.TextField(db_column='INTEREST_INCOME_CR', blank=True, null=True)  # Field name made lowercase.
    interest_income_dr = models.TextField(db_column='INTEREST_INCOME_DR', blank=True, null=True)  # Field name made lowercase.
    interest_receivable_cr = models.TextField(db_column='INTEREST_RECEIVABLE_CR', blank=True, null=True)  # Field name made lowercase.
    interest_receivable_dr = models.TextField(db_column='INTEREST_RECEIVABLE_DR', blank=True, null=True)  # Field name made lowercase.
    interest_receivable_dr_date = models.DateField(db_column='INTEREST_RECEIVABLE_DR_DATE', blank=True, null=True)  # Field name made lowercase.
    interest_receivable_balance = models.TextField(db_column='INTEREST_RECEIVABLE_BALANCE', blank=True, null=True)  # Field name made lowercase.
    overdue_interest_cr = models.TextField(db_column='OVERDUE_INTEREST_CR', blank=True, null=True)  # Field name made lowercase.
    overdue_interest_dr = models.TextField(db_column='OVERDUE_INTEREST_DR', blank=True, null=True)  # Field name made lowercase.
    overdue_interest_balance = models.TextField(db_column='OVERDUE_INTEREST_BALANCE', blank=True, null=True)  # Field name made lowercase.
    income_suspense_cr = models.TextField(db_column='INCOME_SUSPENSE_CR', blank=True, null=True)  # Field name made lowercase.
    income_suspense_dr = models.TextField(db_column='INCOME_SUSPENSE_DR', blank=True, null=True)  # Field name made lowercase.
    income_suspense_balance = models.TextField(db_column='INCOME_SUSPENSE_BALANCE', blank=True, null=True)  # Field name made lowercase.
    income_suspense_debit_date = models.DateField(db_column='INCOME_SUSPENSE_DEBIT_DATE', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    int_income_debit_dr_date = models.DateField(db_column='INT_INCOME_DEBIT_DR_DATE', blank=True, null=True)  # Field name made lowercase.
    int_income_remarks = models.TextField(db_column='INT_INCOME_REMARKS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    activity_date = models.DateField(db_column='ACTIVITY_DATE', blank=True, null=True)  # Field name made lowercase.
    unrealised_income = models.TextField(db_column='UNREALISED_INCOME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_income_accounting'


class EmiMaxComp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    max_date = models.DateField(db_column='MAX_DATE', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.
    approver = models.TextField(db_column='APPROVER', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_max_comp'


class EmiOgTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emi_date = models.DateField(db_column='EMI_DATE', blank=True, null=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    op_bal = models.TextField(db_column='OP_BAL', blank=True, null=True)  # Field name made lowercase.
    emi_due = models.TextField(db_column='EMI_DUE', blank=True, null=True)  # Field name made lowercase.
    full_emi_due = models.TextField(db_column='FULL_EMI_DUE', blank=True, null=True)  # Field name made lowercase.
    principal_due = models.TextField(db_column='PRINCIPAL_DUE', blank=True, null=True)  # Field name made lowercase.
    int_due = models.TextField(db_column='INT_DUE', blank=True, null=True)  # Field name made lowercase.
    cl_bal = models.TextField(db_column='CL_BAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_og_table'


class EmiRecalculation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emi_reduction = models.TextField(db_column='EMI_REDUCTION', blank=True, null=True)  # Field name made lowercase.
    applicable_colsing_bal = models.TextField(db_column='APPLICABLE_COLSING_BAL', blank=True, null=True)  # Field name made lowercase.
    emi_start_date = models.DateField(db_column='EMI_START_DATE', blank=True, null=True)  # Field name made lowercase.
    emi_end_date = models.DateField(db_column='EMI_END_DATE', blank=True, null=True)  # Field name made lowercase.
    residual_month = models.TextField(db_column='RESIDUAL_MONTH', blank=True, null=True)  # Field name made lowercase.
    roi = models.CharField(db_column='ROI', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    month_provided = models.TextField(db_column='MONTH_PROVIDED', blank=True, null=True)  # Field name made lowercase.
    revised_emi = models.TextField(db_column='REVISED_EMI', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.TextField(db_column='APPROVED_BY', blank=True, null=True)  # Field name made lowercase.
    approved_date = models.DateField(db_column='APPROVED_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emi_recalculation'


class FormTracker(models.Model):
    id = models.AutoField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', unique=True, max_length=30)  # Field name made lowercase.
    agency_id = models.CharField(db_column='AGENCY_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    agent_id = models.CharField(db_column='AGENT_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lodger_id = models.CharField(db_column='LODGER_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sanction_id = models.CharField(db_column='SANCTION_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loan_id = models.CharField(db_column='LOAN_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    applied_for_cust_code = models.CharField(db_column='APPLIED_FOR_CUST_CODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    form_status = models.IntegerField(db_column='FORM_STATUS', blank=True, null=True)  # Field name made lowercase.
    loan_account_class = models.IntegerField(db_column='LOAN_ACCOUNT_CLASS', blank=True, null=True)  # Field name made lowercase.
    loan_closure_date = models.DateField(db_column='LOAN_CLOSURE_DATE', blank=True, null=True)  # Field name made lowercase.
    loan_account_status = models.CharField(db_column='LOAN_ACCOUNT_STATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    profile_id = models.CharField(db_column='PROFILE_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    co_owner_id = models.CharField(db_column='CO_OWNER_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    co_app_indi_count = models.IntegerField(db_column='CO_APP_INDI_COUNT', blank=True, null=True)  # Field name made lowercase.
    co_app_corp_count = models.IntegerField(db_column='CO_APP_CORP_COUNT', blank=True, null=True)  # Field name made lowercase.
    loan_amount = models.CharField(db_column='LOAN_AMOUNT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_document_executed = models.IntegerField(db_column='IS_DOCUMENT_EXECUTED', blank=True, null=True)  # Field name made lowercase.
    loan_details_status = models.IntegerField(db_column='LOAN_DETAILS_STATUS', blank=True, null=True)  # Field name made lowercase.
    collection_agent_id = models.CharField(db_column='COLLECTION_AGENT_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    update_at = models.DateTimeField(db_column='UPDATE_AT', blank=True, null=True)  # Field name made lowercase.
    app_fb_id = models.CharField(db_column='APP_FB_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    unread_flag = models.CharField(db_column='UNREAD_FLAG', max_length=45, blank=True, null=True)  # Field name made lowercase.
    auto_category = models.IntegerField(db_column='AUTO_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    lms_status = models.IntegerField(db_column='LMS_STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_tracker'


class IncomeAccounting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accrual_date = models.DateField(db_column='ACCRUAL_DATE', blank=True, null=True)  # Field name made lowercase.
    accrual_dr = models.IntegerField(db_column='ACCRUAL_DR', blank=True, null=True)  # Field name made lowercase.
    cash_date = models.DateField(db_column='CASH_DATE', blank=True, null=True)  # Field name made lowercase.
    cash_cr = models.IntegerField(db_column='CASH_CR', blank=True, null=True)  # Field name made lowercase.
    int_income_cr = models.IntegerField(db_column='INT_INCOME_CR', blank=True, null=True)  # Field name made lowercase.
    int_income_dr = models.IntegerField(db_column='INT_INCOME_DR', blank=True, null=True)  # Field name made lowercase.
    int_rec_cr = models.IntegerField(db_column='INT_REC_CR', blank=True, null=True)  # Field name made lowercase.
    int_rec_dr = models.IntegerField(db_column='INT_REC_DR', blank=True, null=True)  # Field name made lowercase.
    int_rec_dr_date = models.DateField(db_column='INT_REC_DR_DATE', blank=True, null=True)  # Field name made lowercase.
    int_rec_balance = models.IntegerField(db_column='INT_REC_BALANCE', blank=True, null=True)  # Field name made lowercase.
    overdue_int_cr = models.IntegerField(db_column='OVERDUE_INT_CR', blank=True, null=True)  # Field name made lowercase.
    overdue_int_dr = models.IntegerField(db_column='OVERDUE_INT_DR', blank=True, null=True)  # Field name made lowercase.
    overdue_int_balance = models.IntegerField(db_column='OVERDUE_INT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    income_suspense_cr = models.IntegerField(db_column='INCOME_SUSPENSE_CR', blank=True, null=True)  # Field name made lowercase.
    income_suspense_dr = models.IntegerField(db_column='INCOME_SUSPENSE_DR', blank=True, null=True)  # Field name made lowercase.
    income_suspense_dr_date = models.DateField(db_column='INCOME_SUSPENSE_DR_DATE', blank=True, null=True)  # Field name made lowercase.
    income_suspense_balance = models.IntegerField(db_column='INCOME_SUSPENSE_BALANCE', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'income_accounting'


class IncomeBookingScheduled(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='BOOKING_DATE', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateField(db_column='DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    bal_interest = models.IntegerField(db_column='BAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    bal_principal = models.IntegerField(db_column='BAL_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    bal_pf = models.IntegerField(db_column='BAL_PF', blank=True, null=True)  # Field name made lowercase.
    bal_gst_pf = models.IntegerField(db_column='BAL_GST_PF', blank=True, null=True)  # Field name made lowercase.
    bal_sd_ad = models.IntegerField(db_column='BAL_SD_AD', blank=True, null=True)  # Field name made lowercase.
    bal_cf = models.IntegerField(db_column='BAL_CF', blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    last_collection_date = models.DateField(db_column='LAST_COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    dpd = models.IntegerField(db_column='DPD', blank=True, null=True)  # Field name made lowercase.
    paid_interest = models.IntegerField(db_column='PAID_INTEREST', blank=True, null=True)  # Field name made lowercase.
    paid_principal = models.IntegerField(db_column='PAID_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    paid_fee = models.IntegerField(db_column='PAID_FEE', blank=True, null=True)  # Field name made lowercase.
    paid_fee_gst = models.IntegerField(db_column='PAID_FEE_GST', blank=True, null=True)  # Field name made lowercase.
    penal_int = models.IntegerField(db_column='PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    gross_bc = models.IntegerField(db_column='GROSS_BC', blank=True, null=True)  # Field name made lowercase.
    gst_bc = models.IntegerField(db_column='GST_BC', blank=True, null=True)  # Field name made lowercase.
    net_bc = models.IntegerField(db_column='NET_BC', blank=True, null=True)  # Field name made lowercase.
    npa_flag = models.IntegerField(db_column='NPA_FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'income_booking_scheduled'


class LoanDetails(models.Model):
    id = models.AutoField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', unique=True, max_length=30)  # Field name made lowercase.
    ld_loan_amt_req = models.CharField(db_column='LD_LOAN_AMT_REQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_inter_pay_freq = models.CharField(db_column='LD_INTER_PAY_FREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_princi_repay = models.CharField(db_column='LD_PRINCI_REPAY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_princi_inst_freq = models.CharField(db_column='LD_PRINCI_INST_FREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_expect_loan_strt_date = models.DateTimeField(db_column='LD_EXPECT_LOAN_STRT_DATE', blank=True, null=True)  # Field name made lowercase.
    ld_loan_mature_date = models.DateTimeField(db_column='LD_LOAN_MATURE_DATE', blank=True, null=True)  # Field name made lowercase.
    ld_emi_amt = models.CharField(db_column='LD_EMI_AMT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_pre_pay_penel = models.CharField(db_column='LD_PRE_PAY_PENEL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_process_fee = models.IntegerField(db_column='LD_PROCESS_FEE', blank=True, null=True)  # Field name made lowercase.
    ld_recurr_fee = models.CharField(db_column='LD_RECURR_FEE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_recurr_fee_frq = models.CharField(db_column='LD_RECURR_FEE_FRQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ld_loan_start_day = models.IntegerField(db_column='LD_LOAN_START_DAY', blank=True, null=True)  # Field name made lowercase.
    ld_dpd_relax = models.IntegerField(db_column='LD_DPD_RELAX', blank=True, null=True)  # Field name made lowercase.
    loan_agreement_date = models.DateTimeField(db_column='LOAN_AGREEMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    loan_amount_sanctioned = models.DecimalField(db_column='LOAN_AMOUNT_SANCTIONED', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rate_of_interest = models.FloatField(db_column='RATE_OF_INTEREST', blank=True, null=True)  # Field name made lowercase.
    loan_tenure_in_months = models.CharField(db_column='LOAN_TENURE_IN_MONTHS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    loan_sanction_date = models.DateTimeField(db_column='LOAN_SANCTION_DATE', blank=True, null=True)  # Field name made lowercase.
    processing_fee_precen = models.CharField(db_column='PROCESSING_FEE_PRECEN', max_length=25, blank=True, null=True)  # Field name made lowercase.
    loan_product_type = models.CharField(db_column='LOAN_PRODUCT_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sanction_limit = models.CharField(db_column='SANCTION_LIMIT', max_length=25, blank=True, null=True)  # Field name made lowercase.
    facility_type = models.CharField(db_column='FACILITY_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    interest_reset_frequency = models.CharField(db_column='INTEREST_RESET_FREQUENCY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    loan_structure = models.CharField(db_column='LOAN_STRUCTURE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    principal_moratorium_in_month = models.CharField(db_column='PRINCIPAL_MORATORIUM_IN_MONTH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    no_of_instalments = models.CharField(db_column='NO_OF_INSTALMENTS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    security_package = models.CharField(db_column='SECURITY_PACKAGE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    total_amount_disburse = models.DecimalField(db_column='TOTAL_AMOUNT_DISBURSE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    adjust_amount = models.DecimalField(db_column='ADJUST_AMOUNT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount_repaid = models.DecimalField(db_column='AMOUNT_REPAID', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    facility_duration = models.CharField(db_column='FACILITY_DURATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pre_payment_penalty = models.DecimalField(db_column='PRE_PAYMENT_PENALTY', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    date_of_first_disbursement = models.DateTimeField(db_column='DATE_OF_FIRST_DISBURSEMENT', blank=True, null=True)  # Field name made lowercase.
    ld_yield_to_matu = models.CharField(db_column='LD_YIELD_TO_MATU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ld_bp_channel_dis_cost = models.DecimalField(db_column='LD_BP_CHANNEL_DIS_COST', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    loan_misc_securities = models.CharField(db_column='LOAN_MISC_SECURITIES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rate_of_interest_m = models.FloatField(db_column='RATE_OF_INTEREST_M', blank=True, null=True)  # Field name made lowercase.
    processing_fee_rs = models.DecimalField(db_column='PROCESSING_FEE_RS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gst = models.DecimalField(db_column='GST', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    stamp_duty = models.DecimalField(db_column='STAMP_DUTY', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    courier_charges = models.DecimalField(db_column='COURIER_CHARGES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pre_payment_penalty_percentage = models.CharField(db_column='PRE_PAYMENT_PENALTY_PERCENTAGE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insurance_applicable = models.CharField(db_column='INSURANCE_APPLICABLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ld_insurance_cost = models.CharField(db_column='LD_INSURANCE_COST', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_interest_cost = models.FloatField(db_column='TOTAL_INTEREST_COST', blank=True, null=True)  # Field name made lowercase.
    emi_payment_id = models.FloatField(db_column='EMI_PAYMENT_ID', blank=True, null=True)  # Field name made lowercase.
    ad_security_loan = models.TextField(db_column='AD_SECURITY_LOAN', blank=True, null=True)  # Field name made lowercase.
    ld_loan_tenur = models.CharField(db_column='LD_LOAN_TENUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loan_account_id = models.TextField(db_column='LOAN_ACCOUNT_ID', blank=True, null=True)  # Field name made lowercase.
    account_status = models.TextField(db_column='ACCOUNT_STATUS', blank=True, null=True)  # Field name made lowercase.
    active_closed_flag = models.IntegerField(db_column='ACTIVE_CLOSED_FLAG', blank=True, null=True)  # Field name made lowercase.
    balance_loan = models.IntegerField(db_column='BALANCE_LOAN', blank=True, null=True)  # Field name made lowercase.
    loan_product_id = models.CharField(db_column='LOAN_PRODUCT_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    created_by_emp = models.CharField(db_column='CREATED_BY_EMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ld_loan_id = models.CharField(db_column='LD_LOAN_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ld_tran_id = models.CharField(db_column='LD_TRAN_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ld_disb_verified = models.IntegerField(db_column='LD_DISB_VERIFIED', blank=True, null=True)  # Field name made lowercase.
    ld_disb_status = models.CharField(db_column='LD_DISB_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loan_details'


class LoanPrepayment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prepayment_amt = models.IntegerField(db_column='PREPAYMENT_AMT', blank=True, null=True)  # Field name made lowercase.
    bounce_charges = models.IntegerField(db_column='BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    total_prepayment = models.IntegerField(db_column='TOTAL_PREPAYMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loan_prepayment'


class NachStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    umrnno = models.TextField(db_column='UMRNNO', blank=True, null=True)  # Field name made lowercase.
    system_status = models.TextField(db_column='SYSTEM_STATUS', blank=True, null=True)  # Field name made lowercase.
    reasonname = models.TextField(db_column='REASONNAME', blank=True, null=True)  # Field name made lowercase.
    debtor_customer_reference_no = models.TextField(db_column='DEBTOR_CUSTOMER_REFERENCE_NO', blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.TextField(db_column='PAYMENTTYPE', blank=True, null=True)  # Field name made lowercase.
    debtoraccountno = models.TextField(db_column='DEBTORACCOUNTNO', blank=True, null=True)  # Field name made lowercase.
    debitorbankname = models.TextField(db_column='DEBITORBANKNAME', blank=True, null=True)  # Field name made lowercase.
    debtorbankcode = models.TextField(db_column='DEBTORBANKCODE', blank=True, null=True)  # Field name made lowercase.
    debtorname = models.TextField(db_column='DEBTORNAME', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.TextField(db_column='CREDITORNAME', blank=True, null=True)  # Field name made lowercase.
    frequency = models.TextField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='ENDDATE', blank=True, null=True)  # Field name made lowercase.
    mandate_initiated_business_date = models.DateField(db_column='MANDATE_INITIATED_BUSINESS_DATE', blank=True, null=True)  # Field name made lowercase.
    sponsor_checker_approval_date = models.DateField(db_column='SPONSOR_CHECKER_APPROVAL_DATE', blank=True, null=True)  # Field name made lowercase.
    mandate_creation_date = models.DateField(db_column='MANDATE_CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    mandate_acceptance_date = models.DateField(db_column='MANDATE_ACCEPTANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    creditorutilitycode = models.TextField(db_column='CREDITORUTILITYCODE', blank=True, null=True)  # Field name made lowercase.
    pro_date = models.DateField(db_column='PRO_DATE', blank=True, null=True)  # Field name made lowercase.
    lot = models.IntegerField(db_column='LOT', blank=True, null=True)  # Field name made lowercase.
    srno = models.IntegerField(db_column='SRNO', blank=True, null=True)  # Field name made lowercase.
    client_cod = models.IntegerField(db_column='CLIENT_COD', blank=True, null=True)  # Field name made lowercase.
    old_umrn = models.TextField(db_column='OLD_UMRN', blank=True, null=True)  # Field name made lowercase.
    nach_date = models.DateField(db_column='NACH_DATE', blank=True, null=True)  # Field name made lowercase.
    sp_bkcode = models.TextField(db_column='SP_BKCODE', blank=True, null=True)  # Field name made lowercase.
    action = models.TextField(db_column='ACTION', blank=True, null=True)  # Field name made lowercase.
    ac_type = models.TextField(db_column='AC_TYPE', blank=True, null=True)  # Field name made lowercase.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase.
    pickup_loc = models.TextField(db_column='PICKUP_LOC', blank=True, null=True)  # Field name made lowercase.
    inward_date = models.DateField(db_column='INWARD_DATE', blank=True, null=True)  # Field name made lowercase.
    sp_bank = models.TextField(db_column='SP_BANK', blank=True, null=True)  # Field name made lowercase.
    scheme = models.TextField(db_column='SCHEME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nach_status'


class PostLoanClosure(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.TextField(db_column='APP_FORM_ID', blank=True, null=True)  # Field name made lowercase.
    collected_from = models.TextField(db_column='COLLECTED_FROM', blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='COLLECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    payment_method = models.TextField(db_column='PAYMENT_METHOD', blank=True, null=True)  # Field name made lowercase.
    adjustment_loan_disb = models.TextField(db_column='ADJUSTMENT_LOAN_DISB', blank=True, null=True)  # Field name made lowercase.
    destination_bank_name = models.TextField(db_column='DESTINATION_BANK_NAME', blank=True, null=True)  # Field name made lowercase.
    total_bal_due = models.TextField(db_column='TOTAL_BAL_DUE', blank=True, null=True)  # Field name made lowercase.
    amount_collected = models.TextField(db_column='AMOUNT_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    interest_income = models.TextField(db_column='INTEREST_INCOME', blank=True, null=True)  # Field name made lowercase.
    principal_collection = models.TextField(db_column='PRINCIPAL_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    bounce_charges = models.TextField(db_column='BOUNCE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    penal_interest = models.TextField(db_column='PENAL_INTEREST', blank=True, null=True)  # Field name made lowercase.
    payment_for = models.TextField(db_column='PAYMENT_FOR', blank=True, null=True)  # Field name made lowercase.
    loan_closure_amout_collected = models.TextField(db_column='LOAN_CLOSURE_AMOUT_COLLECTED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.TextField(db_column='APPROVED_BY', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    creation_date = models.DateField(db_column='CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    updation_date = models.DateField(db_column='UPDATION_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post_loan_closure'


class PreDisbActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    app_form_id = models.CharField(db_column='APP_FORM_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cust_bank_details_verify = models.TextField(db_column='CUST_BANK_DETAILS_VERIFY', blank=True, null=True)  # Field name made lowercase.
    mcpl_bank_name = models.TextField(db_column='MCPL_BANK_NAME', blank=True, null=True)  # Field name made lowercase.
    mcpl_acc_no = models.TextField(db_column='MCPL_ACC_NO', blank=True, null=True)  # Field name made lowercase.
    dedupe_check = models.TextField(db_column='DEDUPE_CHECK', blank=True, null=True)  # Field name made lowercase.
    prev_unpaid_charges = models.TextField(db_column='PREV_UNPAID_CHARGES', blank=True, null=True)  # Field name made lowercase.
    prev_recovery_from_disbursement = models.TextField(db_column='PREV_RECOVERY_FROM_DISBURSEMENT', blank=True, null=True)  # Field name made lowercase.
    prev_balance_after_recovery = models.TextField(db_column='PREV_BALANCE_AFTER_RECOVERY', blank=True, null=True)  # Field name made lowercase.
    prev_app_ids = models.TextField(db_column='PREV_APP_IDS', blank=True, null=True)  # Field name made lowercase.
    prev_int_income = models.TextField(db_column='PREV_INT_INCOME', blank=True, null=True)  # Field name made lowercase.
    prev_pirncipal_collection = models.TextField(db_column='PREV_PIRNCIPAL_COLLECTION', blank=True, null=True)  # Field name made lowercase.
    prev_bc = models.TextField(db_column='PREV_BC', blank=True, null=True)  # Field name made lowercase.
    prev_penal_int = models.TextField(db_column='PREV_PENAL_INT', blank=True, null=True)  # Field name made lowercase.
    prev_booking_month = models.DateField(db_column='PREV_BOOKING_MONTH', blank=True, null=True)  # Field name made lowercase.
    run_loan_bal = models.TextField(db_column='RUN_LOAN_BAL', blank=True, null=True)  # Field name made lowercase.
    run_recovery_from_disbursement = models.TextField(db_column='RUN_RECOVERY_FROM_DISBURSEMENT', blank=True, null=True)  # Field name made lowercase.
    run_balance_after_recovery = models.TextField(db_column='RUN_BALANCE_AFTER_RECOVERY', blank=True, null=True)  # Field name made lowercase.
    run_payment_for = models.TextField(db_column='RUN_PAYMENT_FOR', blank=True, null=True)  # Field name made lowercase.
    run_app_ids = models.TextField(db_column='RUN_APP_IDS', blank=True, null=True)  # Field name made lowercase.
    run_total_recovery = models.TextField(db_column='RUN_TOTAL_RECOVERY', blank=True, null=True)  # Field name made lowercase.
    final_net_avail = models.TextField(db_column='FINAL_NET_AVAIL', blank=True, null=True)  # Field name made lowercase.
    final_less_recoveries = models.TextField(db_column='FINAL_LESS_RECOVERIES', blank=True, null=True)  # Field name made lowercase.
    final_disbursement_to_customer = models.TextField(db_column='FINAL_DISBURSEMENT_TO_CUSTOMER', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.TextField(db_column='APPROVED_BY', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_disb_activity'


class UserRegMst(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login_id = models.CharField(db_column='LOGIN_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_type = models.IntegerField(db_column='REG_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_country_code = models.CharField(db_column='USER_COUNTRY_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_mobile_no = models.IntegerField(db_column='USER_MOBILE_NO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_reg_mst'



class RiskManagerDetail(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    office_id = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.CharField(max_length=20, blank=True, null=True)
    transfer_executives = models.CharField(max_length=20, blank=True, null=True)
    transfer_loans = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'risk_manager_detail'


class BroadcastResponse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    api_status = models.TextField(db_column='API_STATUS', blank=True, null=True)  # Field name made lowercase.
    sms_id = models.TextField(db_column='SMS_ID', blank=True, null=True)  # Field name made lowercase.
    customid = models.TextField(db_column='CUSTOMID', blank=True, null=True)  # Field name made lowercase.
    customid1 = models.TextField(db_column='CUSTOMID1', blank=True, null=True)  # Field name made lowercase.
    customid2 = models.TextField(db_column='CUSTOMID2', blank=True, null=True)  # Field name made lowercase.
    mobile = models.TextField(db_column='MOBILE', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broadcast_response'

    
class BroadcastDetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sr_no = models.TextField(db_column='SR_NO', blank=True, null=True)  # Field name made lowercase.
    message_type = models.TextField(db_column='MESSAGE_TYPE', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    loan_product = models.TextField(db_column='LOAN_PRODUCT', blank=True, null=True)  # Field name made lowercase.
    recepient_name = models.TextField(db_column='RECEPIENT_NAME', blank=True, null=True)  # Field name made lowercase.
    recepient_contact_no = models.TextField(db_column='RECEPIENT_CONTACT_NO', blank=True, null=True)  # Field name made lowercase.
    message_template = models.TextField(db_column='MESSAGE_TEMPLATE', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broadcast_details'
