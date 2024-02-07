import validators
from rest_framework import permissions

from api.v1.clients.validators import client_exists


class IsMYSQLUser(permissions.BasePermission):
    def has_permission(self, request, view):
        view.client_id = request.query_params.get('client_id')
        view.domain = str(request.META.get("HTTP_ORIGIN")
                          ).replace('https://', '').replace('http://', '').replace('/', '')

        if not (view.client_id and validators.domain(view.domain) is True):
            return False

        return client_exists(mysql_user_id=view.client_id, domain=view.domain)
