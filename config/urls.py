from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/solar-info/', include('api.v1.solarapiinfos.urls')),
    path('api/v1/customers/', include('api.v1.customers.urls'))
]
