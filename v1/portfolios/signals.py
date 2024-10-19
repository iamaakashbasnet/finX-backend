from django.db.models.signals import post_save
from django.dispatch import receiver

from v1.firms.models import Firm
from v1.portfolios.models import PoolInvestmentPortfolio, ClientPortfolio
from v1.clients.models import GeneralClient


@receiver(post_save, sender=Firm)
def create_pool_investment_portfolio(sender, instance, created, **kwargs):
    if created:
        PoolInvestmentPortfolio.objects.create(firm=instance)


@receiver(post_save, sender=GeneralClient)
def create_client_portfolio(sender, instance, created, **kwargs):
    if created:
        ClientPortfolio.objects.create(client=instance)
