from rest_framework.generics import CreateAPIView

from api.v1.clients.permissions import FromSuncountRequest
from api.v1.clients.serializers import ClientCreateSerializer


class ClientCreateAPIView(CreateAPIView):
    permission_classes = (FromSuncountRequest,)
    serializer_class = ClientCreateSerializer
