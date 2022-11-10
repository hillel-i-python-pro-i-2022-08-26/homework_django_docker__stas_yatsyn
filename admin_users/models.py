from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Admin User"
