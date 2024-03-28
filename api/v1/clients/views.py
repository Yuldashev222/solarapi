from django.conf import settings
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response

from api.v1.clients.permissions import FromSuncountRequest, IsMYSQLClient
from api.v1.clients.serializers import ClientCreateSerializer
from api.v1.clients.services import get_client_limit
from api.v1.solarapiinfos.models import SolarInfo


class ClientCreateAPIView(CreateAPIView):
    permission_classes = (FromSuncountRequest,)
    serializer_class = ClientCreateSerializer


class ClientLimitAPIView(GenericAPIView):
    permission_classes = (IsMYSQLClient,)

    def get(self, request, *args, **kwargs):
        order_limit = get_client_limit(self.client_id)
        solar_api_requests = SolarInfo.objects.filter(mysql_user_id=self.client_id, success=True).count()

        return Response({'limit': order_limit + settings.CLIENT_FREE_LIMIT - solar_api_requests})
