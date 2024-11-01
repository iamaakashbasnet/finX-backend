from django.db import models


class AbstractPortfolioEntry(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PoolInvestmentPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('PoolInvestmentPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.portfolio.name} - Amount: {self.amount}, Description: {self.description}'

    class Meta:
        verbose_name = "Pool Investment Portfolio Entry"
        verbose_name_plural = "Pool Investment Portfolio Entries"


class ClientPortfolioEntry(AbstractPortfolioEntry):
    portfolio = models.ForeignKey('ClientPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return f'Client Entry for {self.portfolio.client.user.get_full_name()} - Amount: {self.amount}'

    class Meta:
        verbose_name = "Client Portfolio Entry"
        verbose_name_plural = "Client Portfolio Entries"
