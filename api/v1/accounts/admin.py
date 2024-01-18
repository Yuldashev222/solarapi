from django.contrib import admin
from django.contrib.auth.hashers import make_password

from api.v1.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('client_domain', 'email', 'first_name', 'last_name')
    list_display_links = ('client_domain', 'email', 'first_name', 'last_name')
    search_fields = ('client_domain', 'email', 'first_name', 'last_name')

    fields = ('client_domain', 'email', 'password', 'first_name', 'last_name', 'is_active', 'date_joined')
    readonly_fields = ('date_joined',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_staff=False)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.set_password(obj.password)
        elif obj.password != CustomUser.objects.get(pk=obj.pk).password:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
