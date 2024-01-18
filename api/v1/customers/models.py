from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    client = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    solar_info = models.ForeignKey('solarapiinfos.SolarInfo', on_delete=models.PROTECT)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.PositiveSmallIntegerField()

    joined_at = models.DateTimeField(auto_now_add=True)
