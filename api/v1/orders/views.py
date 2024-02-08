from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.v1.orders.models import Order
from api.v1.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    client_id = None
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Order.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        serializer.save(status=Order.STATUS[0][0], mysql_user_id=self.client_id)
