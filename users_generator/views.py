from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from webargs import fields
from webargs.djangoparser import use_args

from users_generator.services.generate_user_info import organize_info


@use_args({"amount": fields.Int(missing=10)}, location="query")
def humans_info(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]
    return render(
        request,
        "users_generator/index.html",
        {
            "title": "Users",
            "info": organize_info(amount=amount),
        },
    )
