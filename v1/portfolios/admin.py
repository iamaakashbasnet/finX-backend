from django.contrib import admin

from v1.portfolios.models import PoolInvestmentPortfolio, ClientPortfolio
from v1.portfolios.models.entry import PortfolioEntry


@admin.register(PoolInvestmentPortfolio)
class PoolInvestmentPortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientPortfolio)
class ClientPortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(PortfolioEntry)
class PortfolioEntryAdmin(admin.ModelAdmin):
    pass
