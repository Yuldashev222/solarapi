from django.urls import path

from api.v1.clients.views import ClientCreateAPIView

urlpatterns = [
    path('', ClientCreateAPIView.as_view()),
]
