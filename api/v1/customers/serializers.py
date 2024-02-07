from rest_framework import serializers

from api.v1.customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    def validate_mysql_user_id(self, user_id):
        return user_id

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'source': 'mysql_user_id'}
        }
