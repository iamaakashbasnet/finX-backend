from rest_framework import routers

from .views import FirmExecutiveViewSet, FirmManagerViewSet

router = routers.DefaultRouter()

router.register(r'executive', FirmExecutiveViewSet, basename='firm-executive')
router.register(r'manager', FirmManagerViewSet, basename='firm-manager')

urlpatterns = router.urls
