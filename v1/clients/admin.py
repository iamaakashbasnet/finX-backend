from django.contrib import admin

from .models import PoolInvestmentClient, GeneralClient


@admin.register(PoolInvestmentClient)
class PoolInvestmentClientAdmin(admin.ModelAdmin):
    readonly_fields = ('get_nav_value',)
    list_display = ['user', 'shares_amount', 'get_nav_value', 'payments', 'is_active', 'joined_at']

    @admin.display(description="NAV Value")
    def get_nav_value(self, obj):
        return obj.nav_value if obj.nav_value else "N/A"


@admin.register(GeneralClient)
class GeneralClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'payments', 'is_active', 'joined_at']
