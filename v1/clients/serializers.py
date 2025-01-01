from django.contrib.auth import get_user_model
from rest_framework import serializers

from v1.users.serializers.user import UserSerializer
from .models import PoolInvestmentClient, GeneralClient


class PoolInvestmentClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=get_user_model().objects.all(), write_only=True
    )

    def get_user(self, instance):
        # Only for GET requests: return expanded user info
        return UserSerializer(instance.user).data

    def update(self, instance, validated_data):
        # Prevent changing the user field
        user = validated_data.get('user', None)
        if user and user != instance.user.id:
            raise serializers.ValidationError("The user field cannot be updated.")

        # Remove user from validated data as we are not updating it
        validated_data.pop('user', None)

        # Update other fields
        return super().update(instance, validated_data)

    class Meta:
        model = PoolInvestmentClient
        fields = ['user', 'user_id', 'shares_amount', 'nav_value', 'is_active']


class GeneralClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=get_user_model().objects.all(), write_only=True
    )

    def get_user(self, instance):
        # Only for GET requests: return expanded user info
        return UserSerializer(instance.user).data

    def update(self, instance, validated_data):
        # Prevent changing the user field
        user = validated_data.get('user', None)
        if user and user != instance.user.id:
            raise serializers.ValidationError("The user field cannot be updated.")

        # Remove user from validated data as we are not updating it
        validated_data.pop('user', None)

        # Update other fields
        return super().update(instance, validated_data)

    class Meta:
        model = GeneralClient
        fields = ['user', 'user_id', 'payments', 'is_active']
