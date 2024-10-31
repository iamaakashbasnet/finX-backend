from django.contrib import admin
from django.urls import path, include

from .views import index
from .admin import tenant_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-tenant/', tenant_admin_site.urls),
    path('users/', include('v1.users.urls')),
    path('', index),
]
