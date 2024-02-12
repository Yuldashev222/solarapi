from django.db import models


class SolarInfo(models.Model):
    mysql_user_id = models.PositiveBigIntegerField()

    json_data = models.TextField()

    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
