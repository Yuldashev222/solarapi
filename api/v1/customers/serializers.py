from rest_framework import serializers

from api.v1.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True}
        }
