from django import forms


class PayrollForm(forms.Form):
	date = forms.CharField(label="Date", required=True, widget=forms.TextInput(attrs={
		"class":"form-control",
		"id":"datepicker",
		"placeholder": "start date"
		}))
	date2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
		"class":"form-control",
		"id":"datepicker2",
		"placeholder": "end date"
		}))