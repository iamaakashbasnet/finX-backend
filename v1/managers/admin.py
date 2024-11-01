from django.contrib import admin

from .models import FirmManager, FirmExecutive


@admin.register(FirmManager)
class GeneralClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'role_created_at', 'is_active']


@admin.register(FirmExecutive)
class FirmExecutiveAdmin(admin.ModelAdmin):
    list_display = ['user', 'role_created_at', 'is_active']
