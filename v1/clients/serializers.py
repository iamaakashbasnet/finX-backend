from rest_framework import serializers

from v1.users.serializers.user import UserSerializer
from .models import PoolInvestmentClient, GeneralClient


class PoolInvestmentClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, instance):
        # Only for GET requests: return expanded user info
        return UserSerializer(instance.user).data

    class Meta:
        model = PoolInvestmentClient
        fields = ['id', 'user', 'shares_amount', 'nav_value', 'is_active']


class GeneralClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, instance):
        return UserSerializer(instance.user).data

    class Meta:
        model = GeneralClient
        fields = ['id', 'user', 'is_active']
