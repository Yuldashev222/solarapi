from rest_framework import serializers

from api.v1.services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['mysql_user_id']
