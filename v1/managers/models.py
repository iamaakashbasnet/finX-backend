from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class FirmManager(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    role_created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Firm Manager")
        verbose_name_plural = _("Firm Managers")


class FirmExecutive(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    role_created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Firm Executive")
        verbose_name_plural = _("Firm Executives")
