from django.db import models

from v1.data.nepse.models import Security


class AbstractPortfolioEntry(models.Model):
    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    total_investment = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        return self.quantity * self.rate

    @property
    def current_value(self):
        return self.quantity * self.security.securitydata.last_traded_price

    def save(self, *args, **kwargs):
        self.total_investment = self.calculate_total()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class PoolInvestmentPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('PoolInvestmentPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'Entry for {self.portfolio.name} | Total - {self.total_investment} | Current Value - {self.current_value}'

    class Meta:
        verbose_name = "Pool Investment Portfolio Entry"
        verbose_name_plural = "Pool Investment Portfolio Entries"


class ClientPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('ClientPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'Entry for {self.portfolio.client.user.email} | Total - {self.total_investment} | Current Value - {self.current_value}'

    class Meta:
        verbose_name = "Client Portfolio Entry"
        verbose_name_plural = "Client Portfolio Entries"
