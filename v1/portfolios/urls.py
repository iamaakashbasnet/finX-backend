from rest_framework import routers

from .views import PoolInvestmentPortfolioViewSet, ClientPortfolioViewSet

router = routers.DefaultRouter()

router.register(r'pool', PoolInvestmentPortfolioViewSet, basename='pool-portfolio')
router.register(r'client', ClientPortfolioViewSet, basename='client-portfolio')

urlpatterns = router.urls
