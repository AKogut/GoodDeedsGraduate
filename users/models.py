from contextvars import Token

from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=20, default="Anonymous", null=False)
    last_name = models.CharField(max_length=40, default="Anonymous", null=False)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def token(self):
        return Token.objects.create(user=self)

    def __str__(self):
        return self.email