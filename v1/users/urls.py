from django.urls import path

from .views.token import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)
from .views.user import RequestUserView, UserWithEmailCheckView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token-blacklist'),

    path('request-user-data/', RequestUserView.as_view(), name='request-user-data'),
    path('user-with-email-check/', UserWithEmailCheckView.as_view(), name='user-with-email-check'),
]
