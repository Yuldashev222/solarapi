import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from api.v1.accounts.managers import CustomUserManager
from api.v1.accounts.validators import validate_domain


class CustomUser(AbstractUser):
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    client_domain = models.CharField(max_length=200, unique=True)

    def clean(self):
        super().clean()
        if not self.is_staff and validators.domain(self.client_domain) is not True:
            raise ValidationError({"client_domain": ["Invalid domain"]})

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.client_domain = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
