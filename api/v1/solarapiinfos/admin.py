from django.contrib import admin

from api.v1.solarapiinfos.models import SolarInfo


@admin.register(SolarInfo)
class SolarInfoAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'success')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
