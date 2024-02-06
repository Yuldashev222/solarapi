from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError, PermissionDenied

from api.v1.clients.models import Client
from api.v1.clients.validators import client_limit_exists
from api.v1.solarapiinfos.models import SolarInfo
from api.v1.solarapiinfos.services import get_solar_api_info


class SolarInfoAPIView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        temp_test = {}
        for i, j in request.META.items():
            if i in ['SERVER_NAME', 'REMOTE_ADDR', 'HTTP_HOST', 'HTTP_ORIGIN']:
                temp_test[i] = j
        customer_id = request.query_params.get('customer_id')
        if customer_id is None or not customer_id.isdigit():
            raise AuthenticationFailed({'error': 'authentication failed'})

        if not client_limit_exists(customer_id=customer_id):
            raise PermissionDenied({'error': 'denied access'})

        # try:
        #     client = Client.objects.get_or_create(domain=customer_id, is_active=True)
        # except Client.DoesNotExist:
        #     raise AuthenticationFailed({'error': 'authentication failed'})

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
        #
        # obj = SolarInfo.objects.create(client_id=client.pk,
        #                                customer_longitude=longitude,
        #                                customer_latitude=latitude,
        #                                solar_api_longitude=solar_api_longitude,
        #                                solar_api_latitude=solar_api_latitude,
        #                                required_quality=settings.SOLAR_API_REQUIRED_QUALITY,
        #                                success=bool(solar_api_center))

        # data['object_id'] = obj.pk
        data['temp_test'] = temp_test
        return Response(data=data, status=status.HTTP_200_OK)
