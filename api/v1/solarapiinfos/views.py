import validators
from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from api.v1.accounts.models import CustomUser
from api.v1.services.models import SolarPanel, ExtraProduct
from api.v1.services.serializers import SolarPanelSerializer, ExtraProductSerializer
from api.v1.solarapiinfos.models import SolarInfo
from api.v1.solarapiinfos.services import get_solar_api_info


class SolarInfoAPIView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        domain = request.query_params.get('domain')
        if domain is None or not validators.domain(domain):
            raise AuthenticationFailed({'error': 'authentication failed'})

        try:
            client = CustomUser.objects.get(domain=domain, is_active=True, is_superuser=False)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed({'error': 'authentication failed'})

        longitude = request.query_params.get('location.longitude')
        latitude = request.query_params.get('location.latitude')
        if not (longitude or latitude):
            raise ValidationError({'error': 'longitude and latitude are required'})

        data = get_solar_api_info(longitude=longitude, latitude=latitude)

        solar_api_center = data.get('center')
        if solar_api_center is not None:
            solar_api_longitude = solar_api_center['longitude']
            solar_api_latitude = solar_api_center['latitude']
        else:
            solar_api_longitude = None
            solar_api_latitude = None

        obj = SolarInfo.objects.create(client_id=client.pk,
                                       customer_longitude=longitude,
                                       customer_latitude=latitude,
                                       solar_api_longitude=solar_api_longitude,
                                       solar_api_latitude=solar_api_latitude,
                                       required_quality=settings.SOLAR_API_REQUIRED_QUALITY,
                                       success=bool(solar_api_center))

        data['object_id'] = obj.pk
        client_solar_panels = SolarPanel.objects.filter(client_id=client.pk)[:settings.CLIENT_MAX_SERVICES]
        client_extra_products = ExtraProduct.objects.filter(client_id=client.pk)[:settings.CLIENT_MAX_SERVICES]
        data['client_solar_panels'] = SolarPanelSerializer(client_solar_panels, many=True).data
        data['client_extra_products'] = ExtraProductSerializer(client_extra_products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
