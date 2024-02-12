import string
import secrets

from django.db import models


class Order(models.Model):
    STATUS = [(0, 'New'), (1, 'Completed'), (2, 'Rejected')]

    order_id = models.PositiveIntegerField()
    mysql_user_id = models.PositiveBigIntegerField()
    solar_info = models.OneToOneField('solarapiinfos.SolarInfo', on_delete=models.CASCADE)

    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.PositiveSmallIntegerField(null=True)
    city = models.CharField(max_length=255, blank=True)
    panel_counts = models.PositiveSmallIntegerField()

    services = models.ManyToManyField('services.Service', blank=True)
    products = models.ManyToManyField('products.Product', blank=True)

    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['order_id', 'mysql_user_id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_unique_order_id(cls):
        while True:
            value = ''.join(secrets.choice(string.digits) for _ in range(5))
            if not Order.objects.filter(order_id=value).exists():
                return value
