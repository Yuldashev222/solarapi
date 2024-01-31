from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    STATUS = ((1, 'new'), (2, 'process'), (3, 'cancelled'), (4, 'success'))

    solar_info = models.ForeignKey('solarapiinfos.SolarInfo', on_delete=models.PROTECT)
    solar_panel = models.ForeignKey('services.SolarPanel', on_delete=models.PROTECT, null=True)
    extra_product = models.ForeignKey('services.ExtraProduct', on_delete=models.PROTECT, null=True)

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True, blank=True)
    city = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255, blank=True)
    zip_code = models.PositiveSmallIntegerField(null=True)
    panel_counts = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS[0][0])

    def __str__(self):
        return self.full_name
