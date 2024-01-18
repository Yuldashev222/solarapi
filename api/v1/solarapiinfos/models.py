from django.db import models


class SolarInfo(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    required_quality = models.CharField(max_length=200)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
