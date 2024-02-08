from rest_framework import viewsets

from api.v1.clients.permissions import IsMYSQLClient
from api.v1.services.models import Service
from api.v1.services.permissions import ServiceLimitExists
from api.v1.services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    client_id = None
    permission_classes = (IsMYSQLClient, ServiceLimitExists)
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        serializer.save(mysql_user_id=self.client_id)
