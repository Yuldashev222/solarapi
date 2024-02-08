from rest_framework import serializers

from api.v1.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        exclude = ['mysql_user_id']
