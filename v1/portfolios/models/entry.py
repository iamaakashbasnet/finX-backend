from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PortfolioEntry(models.Model):
    """
    Represents an entry in a portfolio, containing details about the investments made.
    """
    # Generic Foreign Key to allow linking to both ClientPortfolio and PoolInvestmentPortfolio
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    portfolio = GenericForeignKey('content_type', 'object_id')  # General or Pool Portfolio

    date = models.DateField()
    company_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)  # Computed from quantity * rate

    def __str__(self):
        return f'{self.company_name} - {self.portfolio}'

    class Meta:
        verbose_name = "Portfolio Entry"
        verbose_name_plural = "Portfolio Entries"
