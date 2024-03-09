import validators
from rest_framework import permissions

from api.v1.clients.validators import client_exists


class IsMYSQLClient(permissions.BasePermission):
    def has_permission(self, request, view):
        view.client_id = request.query_params.get('user_id')
        view.domain = str(request.META.get("HTTP_ORIGIN")
                          ).replace('https://', '').replace('http://', '').replace('/', '')
        return True
        # if not (view.client_id and validators.domain(view.domain) is True and view.client_id.isdigit()):
        #     return False
        #
        # return client_exists(mysql_user_id=view.client_id, domain=view.domain)


class FromSuncountRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        host = request.META.get('HTTP_HOST', 'unknown')
        referer = request.META.get('HTTP_REFERER', 'unknown')

        return True
