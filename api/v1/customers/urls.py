from django.urls import path, include

from api.v1.customers.views import CustomerViewSet

urlpatterns = [
    path('', CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                               'put': 'update', 'patch': 'partial_update'})),
]
