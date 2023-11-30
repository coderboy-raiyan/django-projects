from django.shortcuts import render

# Create your views here.


def profile(request):
    userData = {
        "name": "Tajkier Haque Raiyan",
        "age": 20,
        "genre": ["coding", "database", "python", "django", "c++"],
        "totalBlogs": 100,
        "followers": 100,
        "following": 10
    }
    return render(request, "blogs/profile.html", userData)
