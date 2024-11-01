from django.db.models.signals import post_save
from django.dispatch import receiver

from v1.portfolios.models import ClientPortfolio
from v1.clients.models import GeneralClient


@receiver(post_save, sender=GeneralClient)
def create_client_portfolio(sender, instance, created, **kwargs):
    if created:
        ClientPortfolio.objects.create(client=instance)
