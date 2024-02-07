from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    mysql_id = models.PositiveBigIntegerField()
    first_name = models.CharField(_('First Name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True)
    email = models.EmailField(_("Email address"), blank=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), null=True, blank=True)
    domain = models.CharField(_("Domain"), max_length=200, unique=True)
    company_name = models.CharField(_("Company name"), max_length=255, blank=True)
    country = models.CharField(_("Country"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    full_address = models.CharField(_("Full address"), max_length=255, blank=True)
    zip_code = models.PositiveSmallIntegerField(_("Zip code"), blank=True, null=True)

    is_active = models.BooleanField(_("Is active"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
