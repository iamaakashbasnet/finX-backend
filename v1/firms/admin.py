from django.contrib import admin

from v1.firms.models import Firm


@admin.register(Firm)
class FirmsAdmin(admin.ModelAdmin):
    pass
