from rest_framework import serializers

from api.v1.clients.models import Client


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email', 'mysql_user_id', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return Client.objects.create_user(**validated_data)
