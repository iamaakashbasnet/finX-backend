from rest_framework import routers

from .views import GeneralClientViewSet, PoolInvestmentClientViewSet

router = routers.DefaultRouter()

router.register(r'general', GeneralClientViewSet, basename='general-client')
router.register(r'pool', PoolInvestmentClientViewSet, basename='pool-client')

urlpatterns = router.urls
