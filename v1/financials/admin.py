from django.contrib import admin
from .models import (
    FundDetail,
    CapitalDetail,
    ProfitDetail
)


@admin.register(FundDetail)
class FundDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(CapitalDetail)
class CapitalDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfitDetail)
class ProfitDetailsAdmin(admin.ModelAdmin):
    pass
