from rest_framework import serializers

from api.v1.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['mysql_user_id']
