from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    STATUS = [(0, 'New'), (2, 'Completed'), (3, 'Rejected')]

    mysql_user_id = models.PositiveBigIntegerField()

    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(null=True)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.PositiveSmallIntegerField(null=True)
    city = models.CharField(max_length=255, blank=True)
    panel_counts = models.PositiveSmallIntegerField()
    service = models.ForeignKey('services.Service', models.SET_NULL, null=True)
    product = models.ForeignKey('products.Product', models.SET_NULL, null=True)

    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS[0][0])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
