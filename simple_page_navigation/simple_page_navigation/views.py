from django.shortcuts import render

def home(request) : 
    d = {"name" : "Raiyan", "age" : 18, "list" : [1, 2, 3]}
    return render(request, "home.html", d)