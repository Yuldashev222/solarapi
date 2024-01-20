from django.contrib import admin

from api.v1.solarapiinfos.models import SolarInfo


@admin.register(SolarInfo)
class SolarInfoAdmin(admin.ModelAdmin):
    list_display = ('customer_latitude', 'customer_longitude', 'solar_api_latitude', 'solar_api_longitude',
                    'required_quality', 'created_at', 'success')
    exclude = ('client',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(client_id=request.user.pk)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
