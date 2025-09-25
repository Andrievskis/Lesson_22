from django.contrib import admin
from .models import Product, Category, ContactInfo

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name', 'category_description')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'inn', 'address', 'phone', 'email', 'created_at')
    search_fields = ('country', 'inn', 'address', 'phone', 'email')