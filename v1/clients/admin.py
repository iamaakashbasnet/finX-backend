from django.contrib import admin

from .models import PoolInvestmentClient, GeneralClient


@admin.register(PoolInvestmentClient)
class PoolInvestmentClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'shares_amount', 'nav_value', 'payments', 'is_active', 'joined_at']


@admin.register(GeneralClient)
class GeneralClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'payments', 'is_active', 'joined_at']
