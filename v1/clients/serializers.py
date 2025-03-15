from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import serializers

from v1.users.serializers.user import UserSerializer
from .models import PoolInvestmentClient, GeneralClient
from v1.users.utils.send_account_creation_email import send_account_verification_email
from v1.users.utils.username_generator import generate_unique_username


class PoolInvestmentClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_email = serializers.EmailField(write_only=True)  # Use email instead of user_id

    def get_user(self, instance):
        """Return expanded user info for GET requests."""
        return UserSerializer(instance.user).data

    def create(self, validated_data):
        """Handle creation with email."""
        user_email = validated_data.pop('user_email')
        try:
            user = get_user_model().objects.get(email=user_email)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({"user_email": "User with this email does not exist."})

        validated_data['user'] = user  # Set the user in validated data
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Prevent changing the user field."""
        if 'user_email' in validated_data:
            raise serializers.ValidationError({"user_email": "The user field cannot be updated."})

        return super().update(instance, validated_data)

    class Meta:
        model = PoolInvestmentClient
        fields = ['id', 'user', 'user_email', 'shares_amount', 'nav_value', 'is_active']


class GeneralClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    user_email = serializers.EmailField(write_only=True)

    def get_user(self, instance):
        """Return expanded user info for GET requests."""
        return UserSerializer(instance.user).data

    def create(self, validated_data):
        """Handle creation with email."""
        user_email = validated_data.pop('user_email')
        try:
            user = get_user_model().objects.get(email=user_email)
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create(email=user_email, username=generate_unique_username(user_email))
            toke_generator = PasswordResetTokenGenerator()
            token = toke_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            send_account_verification_email(self.context.get('request'), user, token, uid)

        validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Prevent changing the user field."""
        if 'user_email' in validated_data:
            raise serializers.ValidationError({"user_email": "The user field cannot be updated."})

        return super().update(instance, validated_data)

    class Meta:
        model = GeneralClient
        fields = ['id', 'user', 'user_email', 'payments', 'is_active']
