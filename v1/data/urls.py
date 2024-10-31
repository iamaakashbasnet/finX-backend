from django.urls import path, include

urlpatterns = [
    path("nepse/", include('v1.data.nepse.urls'))
]
