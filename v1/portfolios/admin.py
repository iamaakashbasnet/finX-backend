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
    list_display = ['portfolio', 'security', 'transaction_type', 'quantity', 'rate', 'total_investment',
                    'created_at']
    ordering = ('created_at',)


@admin.register(ClientPortfolioEntry)
class ClientPortfolioEntryAdmin(admin.ModelAdmin):
    list_display = ['portfolio', 'security', 'transaction_type', 'quantity', 'rate', 'total_investment',
                    'created_at']
    ordering = ('created_at',)
