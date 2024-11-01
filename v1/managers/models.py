from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class FirmManager(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Firm Manager")
        verbose_name_plural = _("Firm Managers")
