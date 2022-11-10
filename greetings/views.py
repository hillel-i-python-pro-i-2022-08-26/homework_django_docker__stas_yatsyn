from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from greetings.services.generate_name import generate_name


def greetings(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = generate_name()
    return render(
        request,
        "greetings/index.html",
        {
            "title": "Greetings",
            "name": name.title(),
        },
    )
