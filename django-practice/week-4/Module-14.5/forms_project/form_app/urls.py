from django.urls import path
from .views import django_forms, model_forms

urlpatterns = [
    path("django_forms/", django_forms, name="django_forms"),
    path("model_forms/", model_forms, name="model_forms")
]
