from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from api.v1.orders.models import Order
from api.v1.orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    client_id = None
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['order_id', 'email', 'first_name', 'last_name', 'phone_number']
    filterset_fields = ['status']

    def get_queryset(self):
        return Order.objects.filter(mysql_user_id=self.client_id).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(order_id=Order.generate_unique_order_id(mysql_user_id=self.client_id),
                        status=Order.STATUS[0][0], mysql_user_id=self.client_id)
        # send_message_on_new_order.delay(mysql_user_id=self.client_id)
