from django.conf import settings
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.v1.clients.services import get_client_discounts
from api.v1.products.models import Product
from api.v1.services.models import Service
from api.v1.clients.validators import client_limit_exists
from api.v1.solarapiinfos.models import SolarInfo
from api.v1.services.serializers import ServiceSerializer
from api.v1.products.serializers import ProductSerializer
from api.v1.solarapiinfos.serializers import SolarInfoSerializer
from api.v1.solarapiinfos.services import get_solar_api_info

error_temp = {
    "error": {
        "code": 401,
        "message": 'Authentication credentials were not provided.',
        "status": status.HTTP_401_UNAUTHORIZED,
    },
}


class SolarInfoAPIView(ReadOnlyModelViewSet):
    domain = None
    client_id = None

    def retrieve(self, request, *args, **kwargs):
        queryset = SolarInfo.objects.filter(mysql_user_id=self.client_id)
        instance = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return Response(SolarInfoSerializer(instance).data)

    def list(self, request, *args, **kwargs):
        longitude = request.query_params.get('location.longitude')
        latitude = request.query_params.get('location.latitude')

        if not (longitude or latitude):
            error_temp['code'] = 400
            error_temp['message'] = 'longitude and latitude are required'
            error_temp['status'] = status.HTTP_400_BAD_REQUEST
            raise ValidationError(error_temp)

        if not client_limit_exists(mysql_user_id=self.client_id):
            error_temp['code'] = 403
            error_temp['message'] += ' limit yoq'
            raise PermissionDenied(error_temp)

        data = get_solar_api_info(longitude=longitude, latitude=latitude)
        success = data.get('error') is not None
        obj = SolarInfo.objects.create(mysql_user_id=self.client_id, json_data=str(data) if success else str({}),
                                       success=success)

        data['object_id'] = obj.pk
        data['discount_product'], data['discount_service'] = get_client_discounts(mysql_user_id=self.client_id)
        data['services'] = ServiceSerializer(Service.objects.filter(mysql_user_id=self.client_id), many=True,
                                             context={'request': request}).data
        data['products'] = ProductSerializer(Product.objects.filter(mysql_user_id=self.client_id), many=True,
                                             context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
