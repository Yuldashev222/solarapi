import validators
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

from api.v1.accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    domain = models.CharField(max_length=200, unique=True)
    company_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255, blank=True)
    zip_code = models.PositiveSmallIntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if not self.is_superuser and validators.domain(self.domain) is not True:
            raise ValidationError({"domain": ["Invalid domain"]})

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.domain = self.email
        else:
            self.domain = ''.join(self.domain.split()).lower()

        super().save(*args, **kwargs)

        if not (self.is_superuser or self.groups.exists()):
            obj, created = Group.objects.get_or_create(name='clients')
            if created:
                obj.permissions.set(Permission.objects.filter(content_type__app_label__in=settings.CLIENT_APPS))
            self.groups.set([obj])

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
