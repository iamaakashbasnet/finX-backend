from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView as _TokenObtainPairView,
    TokenRefreshView as _TokenRefreshView,
    TokenVerifyView as _TokenVerifyView,
    TokenBlacklistView as _TokenBlacklistView,
)

from v1.users.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
    TokenVerifySerializer,
    TokenBlacklistSerializer,
)


class BaseTokenView:
    cookie_name = 'rt'

    def set_refresh_token_cookie(self, response, refresh_token):
        cookie_max_age = settings.SIMPLE_JWT.get('REFRESH_TOKEN_LIFETIME')
        response.set_cookie(
            self.cookie_name,
            refresh_token,
            max_age=cookie_max_age,
            httponly=True,
            secure=True,
        )


class TokenObtainPairView(_TokenObtainPairView, BaseTokenView):
    serializer_class = TokenObtainPairSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('access'):
            response.data['at'] = response.data.pop('access')

        if response.data.get('refresh'):
            self.set_refresh_token_cookie(response, response.data['refresh'])
            del response.data['refresh']

        return super().finalize_response(request, response, *args, **kwargs)


class TokenRefreshView(_TokenRefreshView, BaseTokenView):
    serializer_class = TokenRefreshSerializer
    refresh = None

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('access'):
            response.data['at'] = response.data.pop('access')

        if response.data.get('refresh'):
            self.set_refresh_token_cookie(response, response.data['refresh'])
            del response.data['refresh']

        return super().finalize_response(request, response, *args, **kwargs)


class TokenVerifyView(_TokenVerifyView):
    serializer_class = TokenVerifySerializer


class TokenBlacklistView(_TokenBlacklistView, BaseTokenView):
    serializer_class = TokenBlacklistSerializer
    refresh = None
