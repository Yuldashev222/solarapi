from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from api.v1.accounts.models import CustomUser
from api.v1.solarapiinfos.models import SolarInfo
from api.v1.solarapiinfos.services import get_solar_api_info


class SolarInfoAPIView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        domain = request.query_params.get('domain')
        if domain is None:
            raise AuthenticationFailed(detail='domain is required')
        get_object_or_404(CustomUser, client_domain=domain, is_active=True, is_staff=False)

        query_params = {
            'longitude': request.query_params.get('location.longitude'),
            'latitude': request.query_params.get('location.latitude'),
            'required_quality': request.query_params.get('required_quality', settings.SOLAR_API_REQUIRED_QUALITY)
        }

        data = get_solar_api_info(**query_params)
        obj = SolarInfo.objects.create(success=bool(data.get('center')), **query_params)  # last
        data['object_id'] = obj.pk
        return Response(data=data, status=status.HTTP_200_OK)
