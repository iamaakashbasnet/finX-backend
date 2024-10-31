from django.urls import path, include

urlpatterns = [
    path('', include('v1.firms.urls')),

    path('users/', include('v1.users.urls')),

    path('clients/', include('v1.clients.urls')),
]
