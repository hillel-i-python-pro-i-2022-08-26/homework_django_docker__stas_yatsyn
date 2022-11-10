import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def get_session_info(request: WSGIRequest | HttpRequest) -> HttpResponse:
    session = request.session
    if not session.session_key:
        session.save()

    # Set_session_info__start
    time_of_visit = session.get("time_of_visit", datetime.datetime.now())
    count_of_visits = session.get("count", 0)
    # Set_session_info__stop

    count_of_visits += 1
    session["count"] = count_of_visits

    return render(
        request,
        "session_app/session_view.html",
        {
            "title": "Session Info",
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "session_time": time_of_visit,
        },
    )
