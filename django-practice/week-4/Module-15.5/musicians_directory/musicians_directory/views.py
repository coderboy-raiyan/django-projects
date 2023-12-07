from django.shortcuts import render
from musician_app.models import Album


def home(request):
    data = Album.objects.all()
    print(data[0].musician.phone_number)
    return render(request, 'home.html', {'data': data})
