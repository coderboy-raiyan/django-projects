from django.shortcuts import render
from .forms import ContactForm, ContactModelForms
# Create your views here.


def django_forms(request):
    form = ContactForm(request.POST)
    return render(request, 'django_forms.html', {'form': form})


def model_forms(request):
    form = ContactModelForms(request.POST)
    return render(request, 'model_forms.html', {'form': form})
