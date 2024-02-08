from rest_framework import viewsets

from api.v1.services.models import Service
from api.v1.services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    client_id = None
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        print(self.client_id)
        serializer.save(mysql_user_id=self.client_id)
