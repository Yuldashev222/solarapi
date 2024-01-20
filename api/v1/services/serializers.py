from rest_framework import serializers

from api.v1.services.models import SolarPanel, ExtraProduct


class SolarPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarPanel
        exclude = ['client']


class ExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraProduct
        exclude = ['client']
