from rest_framework import viewsets

from api.v1.customers.models import Customer
from api.v1.customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsMYQLUser,)

    def get_queryset(self):
        client_id = self.request.query_params.get('client_id')
        try:
            queryset = Customer.objects.filter(mysql_user_id=client_id)
        except ValueError:
            return Customer.objects.none()
        return queryset

    serializer_class = CustomerSerializer
