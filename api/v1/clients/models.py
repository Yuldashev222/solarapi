from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from api.v1.clients.managers import CustomUserManager


class Client(AbstractUser):
    username = None
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mysql_user_id']

    email = models.EmailField(_('email address'), unique=True)
    mysql_user_id = models.PositiveBigIntegerField(unique=True)
