from django import forms
from django.core.exceptions import ValidationError

from core import settings
from .models import PhoneBook


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birthday_date"].input_formats = settings.DATE_INPUT_FORMATS
        self.fields["birthday_date"].help_text = "format dd.mm.YYYY"
        self.fields["phone"].help_text = "enter your phone number starts with 0..."

    class Meta:
        model = PhoneBook
        fields = ("name", "phone", "birthday_date")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdecimal():
            raise ValidationError("Phone number should be integer only!")
        elif len(phone) != 10:
            raise ValidationError("Phone number not valid. Enter number like usual Ukraine number starts with 0")
        elif not phone.startswith("0"):
            raise ValidationError('Phone number should starts with "0"')
        return phone
