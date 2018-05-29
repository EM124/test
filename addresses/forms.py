from django import forms

from .models import Address

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

class AddressForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    address_line_1 = forms.CharField(label='Address Line 1', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"address line 1"}))
    address_line_2 = forms.CharField(label='Address Line 2', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"address line 2"}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"city"}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"country"}))
    province = forms.CharField(label='Province', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"province"}))
    postal_code = forms.CharField(label='Postal Code', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"postal code"}))
    home_phone = forms.CharField(label='Home Phone', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"home phone"}))
    cell_phone = forms.CharField(label='Cell Phone', widget=forms.TextInput(attrs={
            "class":"form-control", 
            "placeholder":"cell phone"}))

