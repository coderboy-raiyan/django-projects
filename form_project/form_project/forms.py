from django import forms


class DetailsForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='email')
