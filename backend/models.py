from django.db import models
from django.contrib.auth.models import AbstractUser


class RandomNumber(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.number}'
