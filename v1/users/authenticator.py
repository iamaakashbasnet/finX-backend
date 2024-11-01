from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from v1.clients.models import PoolInvestmentClient, GeneralClient
from v1.managers.models import FirmExecutive, FirmManager


class UsernameAndEmailBackend(ModelBackend):
    def is_user_associated_with_tenant(self, user, tenant):
        associated = (
                PoolInvestmentClient.objects.filter(user=user, is_active=True).exists() or
                GeneralClient.objects.filter(user=user, is_active=True).exists() or
                FirmManager.objects.filter(user=user, is_active=True).exists() or
                FirmExecutive.objects.filter(user=user, is_active=True).exists()
        )
        return associated

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
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            # decreases the chances of timing attack to check for valid username
            user_model().set_password(password)
        else:
            if not self.is_user_associated_with_tenant(user, request.tenant):
                if user.is_superuser:
                    return user
                else:
                    return None

            if user.check_password(password) and self.user_can_authenticate(user):
                return user
