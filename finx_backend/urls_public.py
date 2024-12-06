from django.contrib import admin
from django.urls import path, include

from v1.firms.admin import tenant_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin-tenant/', tenant_admin_site.urls),

    path('data/', include('v1.data.urls')),
]
