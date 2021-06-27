from django.db import models
from django.contrib.auth.models import AbstractUser

import random

from django.utils import timezone


def random_number():
    return random.randint(1, 100)


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=False)
    random_number = models.IntegerField(default=random_number)

    def get_user_age(self):
        return timezone.now().year - self.birthday.year

    def __str__(self):
        return self.username

