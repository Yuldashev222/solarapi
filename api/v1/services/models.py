from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class SolarPanel(models.Model):
    client = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=500, blank=True)
    energy = models.PositiveSmallIntegerField(help_text='kw')
    price = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='')

    def clean(self):
        if not self.pk and SolarPanel.objects.count() >= settings.CLIENT_MAX_SERVICES:
            raise ValidationError

    def __str__(self):
        return self.name


class ExtraProduct(models.Model):
    client = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    price = models.PositiveSmallIntegerField()

    def clean(self):
        if not self.pk and ExtraProduct.objects.count() >= settings.CLIENT_MAX_SERVICES:
            raise ValidationError('max error')

    def __str__(self):
        return self.name
