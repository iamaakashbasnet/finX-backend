from django.urls import path
from rest_framework import routers

from .views import PoolInvestmentPortfolioViewSet, ClientPortfolioViewSet
from .views.entry import (
    PoolInvestmentPortfolioEntryViewSet,
    ClientPortfolioEntryViewSet,
    EntriesSummaryView
)

router = routers.DefaultRouter()

router.register(r'pool', PoolInvestmentPortfolioViewSet, basename='pool-portfolio')
router.register(r'pool/entry', PoolInvestmentPortfolioEntryViewSet, basename='pool-entry')

router.register(r'client', ClientPortfolioViewSet, basename='client-portfolio')
router.register(r'client/entry', ClientPortfolioEntryViewSet, basename='client-entry')

urlpatterns = [
    path('pool/entries-summary/<int:portfolio_pk>', EntriesSummaryView.as_view(), name='entries-summary'),
]

urlpatterns += router.urls
