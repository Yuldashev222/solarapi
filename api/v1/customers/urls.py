from django.urls import path

from api.v1.customers.views import CustomerAPIView

urlpatterns = [
    path('create/', CustomerAPIView.as_view(), name='customer-create')
]
