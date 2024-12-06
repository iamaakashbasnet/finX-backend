from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class PoolInvestmentClient(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    shares_amount = models.DecimalField(max_digits=10, decimal_places=2)
    nav_value = models.DecimalField(max_digits=10, decimal_places=2)
    payments = models.DecimalField(max_digits=10, decimal_places=2)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Pool Investment Client")
        verbose_name_plural = _("Pool Investment Clients")

    def __str__(self):
        return f'Pool Investment Client: {self.user.email}'


class GeneralClient(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    payments = models.DecimalField(max_digits=10, decimal_places=2)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("General Client")
        verbose_name_plural = _("General Clients")

    def __str__(self):
        return f'General Client: {self.user.email}'
