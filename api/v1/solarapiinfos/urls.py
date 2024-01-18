from django.urls import path

from api.v1.solarapiinfos.views import SolarInfoAPIView

urlpatterns = [
    path('', SolarInfoAPIView.as_view(), name='solar-info')
]
