from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as _TokenObtainPairSerializer,
    TokenRefreshSerializer as _TokenRefreshSerializer,
    TokenVerifySerializer as _TokenVerifySerializer,
    TokenBlacklistSerializer as _TokenBlacklistSerializer,
)
from rest_framework_simplejwt.exceptions import InvalidToken


class BaseCookieTokenSerializer:
    def get_refresh_token(self):
        refresh_token = self.context['request'].COOKIES.get('rt')
        print('Getting refresh token', refresh_token)
        if not refresh_token:
            raise InvalidToken('No valid token found.')
        return refresh_token


class TokenObtainPairSerializer(_TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data


class TokenRefreshSerializer(_TokenRefreshSerializer, BaseCookieTokenSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.get_refresh_token()
        return super().validate(attrs)


class TokenVerifySerializer(_TokenVerifySerializer):
    pass


class TokenBlacklistSerializer(_TokenBlacklistSerializer, BaseCookieTokenSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.get_refresh_token()
        return super().validate(attrs)
