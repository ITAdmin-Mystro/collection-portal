from django import forms
from .models import RiskManagerDetail

class DateInput(forms.DateInput):
    input_type= 'date'

class RiskManagerForm(forms.ModelForm):
    class Meta:
        model=RiskManagerDetail
        fields=[ "first_name", "last_name", "office_id", "email", "mobile_number", "dob", "is_active",
            "role", "transfer_executives", "transfer_loans"
            ]

        widgets = {'dob' : DateInput()}

# class SMSForm(forms.Form):
#     message = forms.CharField(widget=forms.Textarea)
#     to = forms.CharField(widget=forms.Textarea)

class SMSForm(forms.Form):
    message_type = forms.CharField(max_length=100)
    sr_no = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    loan_product = forms.CharField(max_length=100)
    recepient_contact_no = forms.CharField(widget=forms.Textarea)
    recepient_name = forms.CharField(max_length=100)
    message_template = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


