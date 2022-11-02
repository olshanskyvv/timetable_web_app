from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    group = models.CharField(max_length=10, verbose_name='Номер группы')

