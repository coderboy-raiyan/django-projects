from django import forms


class profileInfo(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password")
    file = forms.FileField()
