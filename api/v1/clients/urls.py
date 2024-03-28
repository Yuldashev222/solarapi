from django.urls import path

from api.v1.clients.views import ClientCreateAPIView, ClientLimitAPIView

urlpatterns = [
    path('', ClientCreateAPIView.as_view()),
    path('limit/', ClientLimitAPIView.as_view()),
]
