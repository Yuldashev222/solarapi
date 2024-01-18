from django.db import models


class SolarPanel(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='')
    energy = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class SolarPanelOrder(models.Model):
    solarPanel = models.ForeignKey(SolarPanel, on_delete=models.PROTECT)
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)


class ExtraProduct(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='')
    price = models.PositiveSmallIntegerField()


class ExtraProductOrder(models.Model):
    extra_product = models.ForeignKey(ExtraProduct, on_delete=models.PROTECT)
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
