from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    avatar = models.ImageField(
        upload_to="users/avatars/", null=True, blank=True, verbose_name="avatar"
    )
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="phone"
    )
    country = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="country"
    )
    token = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="token"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
