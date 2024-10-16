from django.contrib import admin

from .models import Security, SecurityData


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ['security_name']
    list_filter = ['security_name']
    search_fields = ['security_name']
    ordering = ['security_name']


@admin.register(SecurityData)
class SecurityDataAdmin(admin.ModelAdmin):
    list_display = ['security', 'last_traded_price',
                    'open_price', 'high_price', 'low_price', 'previous_close']
    list_filter = ['security']
    search_fields = ['security__security_name', 'security__symbol']
    ordering = ['-last_updated_datetime']
