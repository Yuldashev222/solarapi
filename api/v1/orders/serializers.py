from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.v1.orders.models import Order
from api.v1.products.serializers import ProductSerializer
from api.v1.services.serializers import ServiceSerializer


class OrderSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        exclude = ['mysql_user_id']
        extra_kwargs = {
            'order_id': {'read_only': True}
        }

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

    def validate_product(self, product):
        if product and product.mysql_user_id != int(self.context['view'].client_id):
            raise ValidationError(['client id not found'])
        return product


class OrderReadOnlySerializer(OrderSerializer):
    product = ProductSerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
