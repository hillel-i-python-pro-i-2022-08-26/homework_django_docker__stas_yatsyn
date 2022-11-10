from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from phone_book.forms import AddUserForm
from phone_book.models import PhoneBook


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = PhoneBook.objects.all()
    return render(
        request,
        "phone_book/index.html",
        {
            "title": "Phone Book",
            "contacts": contacts,
        },
    )


def add_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, "User has been created successfully.")
            return redirect("phone_book:user", pk=contact.pk)
    else:
        form = AddUserForm()
    return render(
        request,
        "phone_book/add_user.html",
        {
            "title": "Add User",
            "form": form,
        },
    )


def search_user_info(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "phone_book/user_search.html",
        {
            "title": "Search User",
        },
    )


def show_user_search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query.startswith("0"):
        contact = PhoneBook.objects.get(phone=query)
    else:
        contact = PhoneBook.objects.get(pk=query)
    return render(
        request,
        "phone_book/user_info.html",
        {
            "title": f"Info of user {contact.name}",
            "contact": contact,
        },
    )


def delete_user(request: HttpRequest, pk: PhoneBook.pk) -> HttpResponse:
    contact = get_object_or_404(PhoneBook, pk=pk)
    contact.delete()
    messages.success(request, f"User {contact.name} deleted.")
    return redirect("phone_book:index")


def update_user_info(request: HttpRequest, pk: PhoneBook.pk) -> HttpResponse | HttpResponseRedirect:
    contact = get_object_or_404(PhoneBook, pk=pk)
    if request.method == "POST":
        form = AddUserForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been updated successfully.")
            return redirect("phone_book:user", pk=pk)
        else:
            form = AddUserForm(instance=contact)
        return render(request, "phone_book/update_user.html", {"title": "Update User", "form": form})


def show_user_info(request: HttpRequest, pk: PhoneBook.pk) -> HttpResponse:
    contact = get_object_or_404(PhoneBook, pk=pk)
    return render(
        request,
        "phone_book/user.html",
        {
            "title": f"Info {contact.name}.",
            "contact": contact,
        },
    )