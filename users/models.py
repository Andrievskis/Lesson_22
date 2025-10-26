from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email адрес")
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True, verbose_name="аватар")
    number_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="номер телефона")
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name="страна")

    token = models.CharField(max_length=100, verbose_name="token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
