from django.conf import settings
from rest_framework import permissions

from api.v1.services.models import Service


class ServiceLimitExists(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action != 'create':
            return True
        return Service.objects.filter(mysql_user_id=view.client_id).count() < settings.SERVICE_LIMIT
