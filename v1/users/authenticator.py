from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from v1.clients.models import PoolInvestmentClient, GeneralClient
from v1.managers.models import FirmExecutive, FirmManager


# Public Backend
class PublicBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
        if username is None or password is None:
            return

        try:
            if "@" in username:
                user = user_model.objects.get(email=username)
            else:
                user = user_model.objects.get(username=username)

        except user_model.DoesNotExist:
            # Handle invalid user gracefully
            user_model().set_password(password)
        else:
            # Only superusers are allowed in the public context
            if user.is_superuser and user.check_password(password) and self.user_can_authenticate(user):
                return user

        return None


# Tenant Backend
class TenantBackend(ModelBackend):
    def is_user_associated_with_tenant(self, user, tenant):
        return (
                PoolInvestmentClient.objects.filter(user=user, is_active=True).exists() or
                GeneralClient.objects.filter(user=user, is_active=True).exists() or
                FirmManager.objects.filter(user=user, is_active=True).exists() or
                FirmExecutive.objects.filter(user=user, is_active=True).exists()
        )

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)
        if username is None or password is None:
            return

        try:
            if "@" in username:
                user = user_model.objects.get(email=username)
            else:
                user = user_model.objects.get(username=username)

        except user_model.DoesNotExist:
            # Handle invalid user gracefully
            user_model().set_password(password)
        else:
            if not self.is_user_associated_with_tenant(user, request.tenant):
                return None

            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        return None
