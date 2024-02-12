from rest_framework import serializers

from api.v1.solarapiinfos.models import SolarInfo


class SolarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarInfo
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['json_data'] = eval(ret['json_data'])
        return ret
