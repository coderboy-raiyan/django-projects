from django.shortcuts import render

# Create your views here.


def home(request):
    response = render(request, 'home.html')
    response.set_cookie(
        "jwt", "kjaldkjaskdfujoireuiojrwelkrjweoiuwer732894", expires=5)
    return response


def get_cookie(request):
    jwt = request.COOKIES.get('jwt')
    return render(request, 'get_cookie.html', {"cookie": jwt})


def delete_cookie(request):
    response = render(request, "del.html")
    response.delete_cookie("jwt")
    return response
