import validators
from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError, PermissionDenied

from api.v1.clients.validators import client_limit_exists, client_exists
from api.v1.solarapiinfos.models import SolarInfo
from api.v1.solarapiinfos.services import get_solar_api_info

error_temp = {
    "error": {
        "code": 401,
        "message": 'Authentication credentials were not provided.',
        "status": status.HTTP_401_UNAUTHORIZED,
    },
    "object_id": None
}


class SolarInfoAPIView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        mysql_user_id = request.query_params.get('user_id')
        longitude = request.query_params.get('location.longitude')
        latitude = request.query_params.get('location.latitude')
        domain = str(request.META.get("HTTP_ORIGIN")).replace('https://', '').replace('http://', '').replace('/', '')

        if validators.domain(domain) is not True or mysql_user_id is None or not mysql_user_id.isdigit():
            raise AuthenticationFailed(error_temp)

        if not (longitude or latitude):
            error_temp['code'] = 400
            error_temp['message'] = 'longitude and latitude are required'
            error_temp['status'] = status.HTTP_400_BAD_REQUEST
            raise ValidationError(error_temp)

        if not client_exists(mysql_user_id=mysql_user_id, domain=domain):
            raise AuthenticationFailed(error_temp)

        if not client_limit_exists(mysql_user_id=mysql_user_id):
            error_temp['code'] = 403
            error_temp['message'] += ' limit yoq'
            raise PermissionDenied(error_temp)

        data = get_solar_api_info(longitude=longitude, latitude=latitude)

        solar_api_center = data.get('center')
        if solar_api_center is not None:
            solar_api_longitude = solar_api_center['longitude']
            solar_api_latitude = solar_api_center['latitude']
            success = True
        else:
            solar_api_longitude = None
            solar_api_latitude = None
            success = False

        obj = SolarInfo.objects.create(mysql_user_id=mysql_user_id,
                                       customer_longitude=longitude,
                                       customer_latitude=latitude,
                                       solar_api_longitude=solar_api_longitude,
                                       solar_api_latitude=solar_api_latitude,
                                       required_quality=settings.SOLAR_API_REQUIRED_QUALITY,
                                       success=success)

        data['object_id'] = obj.pk
        return Response(data=data, status=status.HTTP_200_OK)
