from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')

    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)

    token = models.CharField(max_length=50, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
