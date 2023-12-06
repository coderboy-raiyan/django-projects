from django.shortcuts import render, redirect
from . import models
from .forms import profileInfo
# Create your views here.


def home(request):
    if request.method == "POST":
        form = profileInfo(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./db_app/uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print(form.cleaned_data)
        student = models.Student.objects.all()
        return render(request, './db_app/home.html', {"data": student, "form": form})

    else:
        form = profileInfo()
        student = models.Student.objects.all()
        return render(request, './db_app/home.html', {"data": student, "form": form})


def delete_student(request, roll):
    models.Student.objects.get(pk=roll).delete()
    return redirect("homepage")
