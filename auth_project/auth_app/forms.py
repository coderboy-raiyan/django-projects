from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'required': True}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'required': True}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'required': True}))
    password1 = forms.CharField(
        help_text="", label='Password', widget=forms.PasswordInput)
    username = forms.CharField(
        help_text="")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
