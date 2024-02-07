from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=555)
    desc = models.TextField(max_length=1555, blank=True)
    image = models.ImageField(upload_to='products/', null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
