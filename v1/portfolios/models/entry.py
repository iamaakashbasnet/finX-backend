from django.db import models

from v1.data.nepse.models import Security


class AbstractPortfolioEntry(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    TRANSACTION_TYPE_CHOICES = [
        (BUY, "Buy"),
        (SELL, "Sell"),
    ]

    security = models.ForeignKey(Security, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=4,
        choices=TRANSACTION_TYPE_CHOICES,
        default=BUY,
    )
    
    @property
    def total_investment(self):
        return self.quantity * self.rate

    class Meta:
        abstract = True


class PoolInvestmentPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('PoolInvestmentPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'Entry for {self.portfolio.name} | Total - {self.total_investment}'

    class Meta:
        verbose_name = "Pool Investment Portfolio Entry"
        verbose_name_plural = "Pool Investment Portfolio Entries"


class ClientPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('ClientPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'Entry for {self.portfolio.client.user.email} | Total - {self.total_investment}'

    class Meta:
        verbose_name = "Client Portfolio Entry"
        verbose_name_plural = "Client Portfolio Entries"
