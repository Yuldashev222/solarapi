from rest_framework import viewsets

from api.v1.orders.models import Order
from api.v1.orders.serializers import OrderSerializer
from api.v1.orders.tasks import send_email_order_accepted


class OrderViewSet(viewsets.ModelViewSet):
    client_id = None
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        serializer.save(status=Order.STATUS[0][0], mysql_user_id=self.client_id)
