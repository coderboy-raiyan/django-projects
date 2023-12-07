from django import forms
from .models import ContactModel

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    birth_date = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    date = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'date'}))


class ContactModelForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
