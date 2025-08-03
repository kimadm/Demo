from django.contrib import admin
from .models import Category, Product, ShopContact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name', 'description']

@admin.register(ShopContact)
class ShopContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']