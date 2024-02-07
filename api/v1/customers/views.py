from rest_framework import viewsets

from api.v1.customers.models import Customer
from api.v1.customers.permissions import IsMYSQLUser
from api.v1.customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    client_id = None
    # permission_classes = (IsMYSQLUser,)
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(mysql_user_id=self.client_id)

    def perform_create(self, serializer):
        serializer.save(status=Customer.STATUS[0][0], mysql_user_id=self.client_id)
