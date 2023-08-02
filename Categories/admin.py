from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(products)
class productadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_name', 'price']
    search_fields = ['id',  "category_name__name"]