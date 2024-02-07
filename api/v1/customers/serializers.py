from rest_framework import serializers

from api.v1.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Customer
        exclude = ['mysql_user_id']
