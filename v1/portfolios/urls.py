from rest_framework import routers

from .views import PoolInvestmentPortfolioViewSet, ClientPortfolioViewSet
from .views.entry import PoolInvestmentPortfolioEntryViewSet, ClientPortfolioEntryViewSet

router = routers.DefaultRouter()

router.register(r'pool', PoolInvestmentPortfolioViewSet, basename='pool-portfolio')
router.register(r'client', ClientPortfolioViewSet, basename='client-portfolio')
router.register(r'entry/pool', PoolInvestmentPortfolioEntryViewSet, basename='pool-entry')
router.register(r'entry/client', ClientPortfolioEntryViewSet, basename='client-entry')

urlpatterns = router.urls
