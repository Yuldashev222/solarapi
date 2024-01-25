from django.contrib import admin

from api.v1.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'city',
        'full_name',
        'email',
        'phone_number',
        'full_address',
        'zip_code',
        'created_at',
    )
    list_display_links = list_display

    readonly_fields = ('solar_info',)

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        return super().get_queryset(request).filter(solar_info__client_id=request.user.pk)

    def has_module_permission(self, request):
        return not request.user.is_superuser and request.user.has_module_perms(self.opts.app_label)
