from django.urls import path, include
from django.contrib import admin

from .views import index

urlpatterns = [
    path('', index, name='firm-index'),

    path('admin/', admin.site.urls),

    path('users/', include('v1.users.urls')),
]
