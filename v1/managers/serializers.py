from django.contrib.auth import get_user_model
from rest_framework import serializers

from v1.users.serializers import UserSerializer
from .models import FirmExecutive, FirmManager


class FirmExecutiveSerializer(serializers.ModelSerializer):
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
        model = FirmExecutive
        fields = ['user', 'user_id', 'role_created_at', 'is_active']


class FirmManagerSerializer(serializers.ModelSerializer):
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
        model = FirmManager
        fields = ['user', 'user_id', 'role_created_at', 'is_active']
