from django.contrib import admin

# from Categories.pagination import *
from .models import *
# Register your models here.


@admin.register(CustomUser)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'created_at', 'updated_at']
    list_editable = ['is_active']
    search_fields = ['id', 'email']
