from django.urls import path

from .views import FirmCreateView, FirmListView

urlpatterns = [
    path('create/', FirmCreateView.as_view(), name='firm-create'),
    path('list/', FirmListView.as_view(), name='firm-list'),
]
