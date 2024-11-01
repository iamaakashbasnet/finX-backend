from django.contrib import admin

from .models import (
    PoolInvestmentPortfolio,
    ClientPortfolio,
    PoolInvestmentPortfolioEntry,
    ClientPortfolioEntry
)


@admin.register(PoolInvestmentPortfolio)
class PoolInvestmentClientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientPortfolio)
class GeneralClientAdmin(admin.ModelAdmin):
    pass


@admin.register(PoolInvestmentPortfolioEntry)
class PoolInvestmentPortfolioEntryAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientPortfolioEntry)
class ClientPortfolioEntryAdmin(admin.ModelAdmin):
    pass
