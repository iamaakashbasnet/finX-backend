from django.urls import path

from .views import (
    UpdateDataView,
    ListedSecuritiesView,
    ListedSecuritiesDataView,
    NepseIndexView,
    NepseSubIndicesView,
)

urlpatterns = [
    path('listed-securities/', ListedSecuritiesView.as_view(), name='nepse-listed-securities'),
    path('listed-securities-data/', ListedSecuritiesDataView.as_view(), name='nepse-live-market'),
    path('nepse-index/', NepseIndexView.as_view(), name='nepse-index'),
    path('nepse-sub-indices/', NepseSubIndicesView.as_view(), name='nepse-sub-indices'),

    path('update-data/', UpdateDataView.as_view(), name='nepse-update-data'),
]
