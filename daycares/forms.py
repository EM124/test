from django import forms

from .models import Daycare


class DaycareForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    daycare = forms.ChoiceField(choices = [], widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control bootstrap-select', 'checked': False, 'name': 'nothing', 'value': 'nothing'}))
     
    def __init__(self, instance, *args, **kwargs ):
    	super(DaycareForm, self).__init__(*args, **kwargs)
    	if instance is not None:
	    	if instance.admin:
	    	 	self.fields['daycare'].choices = [(x.getName(), x.getName()) for x in Daycare.objects.all()]
	    	elif instance.manager or instance.employee:
	    	 	self.fields['daycare'].choices = [(x.name, x.name) for x in instance.daycare]
	    	else:
	    		pass

class DaycareFormCreation(forms.Form):
	name = forms.CharField(label='Name', widget=forms.TextInput(
		attrs={
		"class":"form-control",
		"placeholder":"name"}))
	identification_number = forms.CharField(label='Identification Number', widget=forms.TextInput(
		attrs={
		"class":"form-control",
		"placeholder":"identification number"}))
	NEQ = forms.CharField(label='NEQ', widget=forms.TextInput(attrs={
		"class":"form-control", 
		"placeholder":"NEQ number"}))
	account_number = forms.CharField(label='Account Number', widget=forms.TextInput(attrs={
		"class":"form-control",
		"placeholder":"account number"}))

	def __init__(self, *args, **kwargs):
		super(DaycareFormCreation, self).__init__(*args, **kwargs)
		self.fields['identification_number'].required = False
		self.fields['NEQ'].required = False
		self.fields['account_number'].required = False