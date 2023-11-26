from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def courses(request):
    return HttpResponse("This is courses")