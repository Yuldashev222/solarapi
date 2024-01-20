from django.contrib import admin
from django.urls import path, include

from django.conf import settings # setting.py ni import qildik
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/solar-info/', include('api.v1.solarapiinfos.urls')),
    path('api/v1/customers/', include('api.v1.customers.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
