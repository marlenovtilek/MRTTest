from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
import datetime

# Create your views here.

class User(AbstractUser):
    username = models.CharField("Пользователь",max_length=150,unique=True)
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    phone = models.CharField("Номер телефона", max_length=14, null=True)
    email = models.EmailField("Почта", blank=True, null=True)
    address = models.CharField("Адрес проживания", max_length=256, null=True)
    birthday = models.DateField("Дата рождения", null=True)

    is_staff = models.BooleanField("Персонал", default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)

