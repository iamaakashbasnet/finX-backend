from django.db import models

from v1.firms.models import Firm
from v1.clients.models import GeneralClient


class Portfolio(models.Model):
    """
    Abstract class for common portfolio properties.
    """
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PoolInvestmentPortfolio(Portfolio):
    def __str__(self):
        return f'Pool Investment Portfolio for {self.firm.name}'


class ClientPortfolio(Portfolio):
    client = models.OneToOneField(GeneralClient, on_delete=models.CASCADE)

    def __str__(self):
        return f'Portfolio for {self.client.user.get_full_name()} at {self.client.firm.name}'
