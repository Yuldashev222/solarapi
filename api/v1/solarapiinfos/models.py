from django.db import models


class SolarInfo(models.Model):
    client = models.ForeignKey('accounts.CustomUser', on_delete=models.PROTECT)

    customer_latitude = models.FloatField()
    customer_longitude = models.FloatField()

    solar_api_latitude = models.FloatField(null=True)
    solar_api_longitude = models.FloatField(null=True)

    required_quality = models.CharField(max_length=200)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'( {self.customer_latitude} X {self.customer_longitude} )'
