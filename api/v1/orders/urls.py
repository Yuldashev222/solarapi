from django.urls import path

from api.v1.orders.views import OrderViewSet, OrderReadOnlyAPIView

urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                            'put': 'update', 'patch': 'partial_update'})),

    path('zapier/', OrderReadOnlyAPIView.as_view({'get': 'list'}))
]
