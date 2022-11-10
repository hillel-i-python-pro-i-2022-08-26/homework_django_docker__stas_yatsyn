from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home_page/index.html",
        {
            "title": "Home Page",
        },
    )
