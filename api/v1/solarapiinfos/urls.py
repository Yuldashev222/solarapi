from django.urls import path

from api.v1.solarapiinfos.views import SolarInfoAPIView

urlpatterns = [
    path('', SolarInfoAPIView.as_view({'get': 'list'}), name='solar-info'),
    path('<int:pk>/', SolarInfoAPIView.as_view({'get': 'retrieve'}), name='solar-info-detail')
]
