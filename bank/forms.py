from django import forms

class BankForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    bank_title = forms.CharField(label='Bank Title', widget=forms.TextInput(attrs={
            "class":"form-control bank_title", 
            "placeholder":"bank title",
            'style':'margin-bottom: 20px'}))
    checking_amount = forms.DecimalField(label='Checking Amount', widget=forms.NumberInput(attrs={
            "class":"form-control checking_amount", 
            "placeholder":"checking amount",
            'style':'margin-bottom: 20px'}))
    credit_amount	= forms.DecimalField(label='Credit Amount', widget=forms.NumberInput(attrs={
            "class":"form-control credit_amount", 
            "placeholder":"credit amount",
            'style':'margin-bottom: 20px'}))
    
    def __init__(self, *args, **kwargs):
        super(BankForm, self).__init__(*args, **kwargs)