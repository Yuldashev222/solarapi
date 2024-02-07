from django.urls import path, include

from api.v1.products.views import ProductViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                              'put': 'update', 'patch': 'partial_update'})),
]
