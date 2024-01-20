from rest_framework.generics import CreateAPIView

from api.v1.customers.models import Customer
from api.v1.customers.serializers import CustomerSerializer


class CustomerAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
