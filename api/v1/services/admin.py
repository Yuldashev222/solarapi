from django.contrib import admin

from api.v1.services.models import ExtraProduct, SolarPanel


class ServiceAbstractAdmin(admin.ModelAdmin):
    exclude = ('client',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(client_id=request.user.pk)

    def save_model(self, request, obj, form, change):
        obj.client_id = request.user.pk
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return not request.user.is_superuser

    def has_module_permission(self, request):
        return not request.user.is_superuser and request.user.has_module_perms(self.opts.app_label)


@admin.register(SolarPanel)
class SolarPanelAdmin(ServiceAbstractAdmin):
    list_display = ('name', 'energy', 'price', 'image')
    list_display_links = ('name', 'energy', 'price')


@admin.register(ExtraProduct)
class ExtraProductAdmin(ServiceAbstractAdmin):
    list_display = ('name', 'price', 'image')
    list_display_links = ('name', 'price')
