from django.urls import path

from . import views

app_name = "users_generator"

urlpatterns = [
    path("", views.humans_info, name="index"),
    path("<int:number>", views.humans_info, name="index"),
]
