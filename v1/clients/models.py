from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class PoolInvestmentClient(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    shares_amount = models.DecimalField(max_digits=10, decimal_places=2)
    nav_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Pool Investment Client")
        verbose_name_plural = _("Pool Investment Clients")


class GeneralClient(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("General Client")
        verbose_name_plural = _("General Clients")
