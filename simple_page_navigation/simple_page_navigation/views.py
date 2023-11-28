from django.shortcuts import render


def home(request):
    d = {
        "name": "Raiyan", "age": 17, "list": [1, 2, 3],
        "courses": [
            {"id": 1, "name": "python", "fee": 5000},
            {"id": 2, "name": "c++", "fee": 15000},
            {"id": 3, "name": "Javascript", "fee": 7000}
        ]
    }
    return render(request, "home.html", d)
