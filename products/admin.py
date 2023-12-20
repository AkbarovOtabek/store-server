from django.contrib import admin
from products.models import ProductCategory, Products, Basket

admin.site.register(ProductCategory)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['image', 'name', 'description',
              ('price', 'quantity'), 'category']
    # readonly_fields = ['description']
    search_fields = ['name']
    ordering = ['-name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

