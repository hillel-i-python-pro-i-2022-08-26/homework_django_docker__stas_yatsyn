from django.urls import path

from . import views

app_name = "greetings"

urlpatterns = [
    path("", views.greetings, name="index"),
    path("<str:name>", views.greetings, name="index"),
]
