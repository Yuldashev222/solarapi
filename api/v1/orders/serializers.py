from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.v1.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        exclude = ['mysql_user_id']

    def validate_solar_info(self, solar_info):
        if solar_info.mysql_user_id != int(self.context['view'].client_id):
            raise ValidationError(['solar info not found'])
        return solar_info

    def validate_services(self, services):
        if len(services) > settings.SERVICE_LIMIT:
            raise ValidationError(['Service limit exceeded'])
        for i in services:
            if i.mysql_user_id != int(self.context['view'].client_id):
                raise ValidationError(['client id not found'])
        return services

    def validate_products(self, products):
        if len(products) > settings.PRODUCT_LIMIT:
            raise ValidationError(['Product limit exceeded'])
        for i in products:
            if i.mysql_user_id != int(self.context['view'].client_id):
                raise ValidationError(['client id not found'])
        return products
