from rest_framework import viewsets

from api.v1.products.models import Product
from api.v1.clients.permissions import IsMYSQLClient
from api.v1.products.serializers import ProductSerializer
from api.v1.services.permissions import ServiceLimitExists


class ProductViewSet(viewsets.ModelViewSet):
    client_id = None
    permission_classes = (IsMYSQLClient, ServiceLimitExists)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(mysql_user_id=self.client_id).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(mysql_user_id=self.client_id)
