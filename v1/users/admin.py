from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
