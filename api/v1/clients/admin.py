from django.contrib import admin
from django.db.models import Count

from api.v1.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'domain', 'company_name', 'requests', 'email', 'first_name', 'last_name', 'is_active'
    )
    list_filter = ('is_active', 'created_at')
    list_display_links = ('domain', 'email', 'first_name', 'last_name')
    search_fields = ('domain', 'email', 'first_name', 'last_name')

    fields = (
        'domain', 'email', 'country', 'city', 'full_address', 'first_name', 'last_name',
        'phone_number', 'company_name', 'zip_code', 'is_active', 'created_at'
    )
    readonly_fields = ('created_at',)

    def requests(self, obj):
        return obj.solarinfo_set.count()
