from rest_framework import serializers

from api.v1.services.models import SolarPanel, ExtraProduct


class SolarPanelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

    class Meta:
        model = SolarPanel
        exclude = ['client']


class ExtraProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

    class Meta:
        model = ExtraProduct
        exclude = ['client']
