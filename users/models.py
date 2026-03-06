from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class GenderChoice(models.Choices):
    male = 'male'
    female = 'female'


class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name="Имя")
    age = models.IntegerField(default=0, verbose_name="Возраст")
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, verbose_name="Гендер")
    password = models.CharField(max_length=50, verbose_name="Пароль")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

