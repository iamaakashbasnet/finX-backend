from django.contrib import admin

from v1.clients.models import PoolInvestmentClient, GeneralClient


@admin.register(PoolInvestmentClient)
class PoolInvestmentClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'firm', 'shares_amount', 'nav_value', 'is_active')


@admin.register(GeneralClient)
class GeneralClientAdmin(admin.ModelAdmin):
    pass
