from django.conf import settings
from rest_framework import permissions

from api.v1.products.models import Product


class ProductLimitExists(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action != 'create':
            return True
        return Product.objects.filter(mysql_user_id=view.client_id).count() < settings.PRODUCT_LIMIT
