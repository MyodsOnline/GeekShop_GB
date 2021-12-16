from django.contrib import admin

from products.models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    search_fields = ('name', 'updated_at',)
    list_filter = ('id', 'name', 'created_at', 'updated_at',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'price', 'quantity',)
    search_fields = ('name', 'price',)
    readonly_fields = ('created_at',)
    list_display_links = ('name',)
    list_editable = ('price',)
    list_filter = ('name', 'updated_at',)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
