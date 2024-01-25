from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.admin import AdminSite

admin.site.unregister(Group)

admin.site.site_header = settings.ADMIN_SITE_HEADER


class MyAdminSite(AdminSite):
    def get_app_list(self, request, app_label=None):
        # Get the app list as usual
        app_list = super().get_app_list(request, app_label=app_label)
        user = request.user

        # Filter apps based on the user's role
        if not user.is_superuser:
            app_list = [app for app in app_list if app['app_label'] != 'app_to_hide']

        return app_list


# Create an instance of your custom admin site
my_admin_site = MyAdminSite(name='myadmin')

