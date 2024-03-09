from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.site_header = settings.ADMIN_SITE_HEADER
