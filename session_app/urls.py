from django.urls import path

from session_app import views

app_name = "session_app"

urlpatterns = [
    path("", views.get_session_info, name="session"),
]
