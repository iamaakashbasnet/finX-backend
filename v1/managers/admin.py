from django.contrib import admin
from .models import FirmManager


@admin.register(FirmManager)
class GeneralClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active']
