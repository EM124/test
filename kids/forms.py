from django import forms

from .models import Kid

# class AddressForm(forms.ModelForm):
# 	class Meta:
# 		model = Address
# 		fields = [
# 			'address_line_1',
# 			'address_line_2',
# 			'city',
# 			'country',
# 			'province',
# 			'postal_code'
# 		]
MONTH_CHOICES = (
		(('M', 'Male'), ('F', 'Female'))
	)
class KidForm(forms.Form):

    child_first_name = forms.CharField(label='First Name', required=False, widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"child first name",
            "name": "child_first_name",
			}))
    child_last_name = forms.CharField(label='Full Name', required=False, widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"child last name",
            "name": "child_last_name",
            }))
    gender = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.Select(attrs={
    	"class":"form-control",
        "name": "gender"
    	}))



