from django.contrib import admin
from django.db.models import Count

from api.v1.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'domain', 'company_name', 'requests',
        'customers', 'email', 'first_name', 'last_name', 'is_active'
    )
    list_filter = ('is_active',)
    list_display_links = ('domain', 'email', 'first_name', 'last_name')
    search_fields = ('domain', 'email', 'first_name', 'last_name')

    fields = (
        'domain', 'email', 'password', 'country', 'city', 'full_address', 'first_name', 'last_name',
        'phone_number', 'company_name', 'zip_code', 'is_active', 'date_joined'
    )
    readonly_fields = ('date_joined',)

    def requests(self, obj):
        return obj.solarinfo_set.count()

    def customers(self, obj):
        return obj.solarinfo_set.aggregate(counts=Count('customer'))['counts']

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=False)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.set_password(obj.password)
        elif obj.password != CustomUser.objects.get(pk=obj.pk).password:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
