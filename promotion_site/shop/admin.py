from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'old_price', 'new_price', 'percent_of_sale',
        'date_of_end', 'image_tag'
    ]
    list_display_links = ['name']
    list_filter = ['category', 'shop_name']    # filters for products
    search_fields = ['category', ]
    # readonly_fields = ('image_tag',)


admin.site.register(User)
admin.site.register(Product, ProductAdmin)  # adds Products to admin panel
