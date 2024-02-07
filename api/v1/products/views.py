from rest_framework import viewsets

from api.v1.customers.permissions import IsMYSQLUser
from api.v1.products.models import Product
from api.v1.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    client_id = None
    # permission_classes = (IsMYSQLUser,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        serializer.save(mysql_user_id=self.client_id)
