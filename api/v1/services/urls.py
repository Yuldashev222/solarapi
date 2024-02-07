from django.urls import path, include

from api.v1.services.views import ServiceViewSet

urlpatterns = [
    path('', ServiceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                              'put': 'update', 'patch': 'partial_update'})),
]
