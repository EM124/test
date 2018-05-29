from django import forms

from .models import Worklog


class WorklogForm(forms.Form):
	date = forms.CharField(label="Date", required=True, widget=forms.TextInput(attrs={
		"class":"input-sm form-control",
		"id":"datepicker"
		}))
	hours = forms.DecimalField(label="Hours", max_digits=4,decimal_places=2,required=True, widget=forms.NumberInput(attrs={
		"class":"input-sm form-control",
		"id":"hours"
		}))