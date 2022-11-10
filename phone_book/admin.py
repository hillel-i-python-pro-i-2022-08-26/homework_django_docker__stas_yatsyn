from django.contrib import admin

from . import models


@admin.register(models.PhoneBook)
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "birthday_date", "is_auto_generated")
    search_fields = (
        "phone",
        "name",
    )
    list_filter = ("is_auto_generated",)
    date_hierarchy = "birthday_date"
    list_per_page = 20
    ordering = (
        "-modified_at",
        "-create_at",
    )
    search_help_text = "Name, Phone or Name + Phone"