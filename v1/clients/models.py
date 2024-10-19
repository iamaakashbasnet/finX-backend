from django.contrib.auth import get_user_model
from django.db import models

from v1.firms.models import Firm


class PoolInvestmentClient(models.Model):
    """
    Model for holding data of client which is part of the pool investment
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    shares_amount = models.DecimalField(max_digits=10, decimal_places=2)
    nav_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)


class GeneralClient(models.Model):
    """
    Model for holding data of client which is not part of the pool investment
    and their portfolios are maintained separately
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Client {self.user.get_full_name()} @ {self.firm}'
