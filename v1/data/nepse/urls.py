from django.urls import path

from .views import (
    LiveMarketView,
    NepseIndexView,
    NepseSubIndicesView
)

urlpatterns = [
    path('live-market/', LiveMarketView.as_view(), name='nepse-live-market'),
    path('nepse-index/', NepseIndexView.as_view(), name='nepse-index'),
    path('nepse-sub-indices/', NepseSubIndicesView.as_view(), name='nepse-sub-indices'),
]
