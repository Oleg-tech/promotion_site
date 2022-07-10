from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'old_price', 'new_price', 'percent_of_sale', 'date_of_end', "category", "shop_name"]
    list_display_links = ['name', 'old_price']
    list_filter = ['category', 'shop_name']    # фильтры по категориям
    search_fields = ['category', ]


# class ShopAdmin(admin.ModelAdmin):
#     list_display = ['name']


admin.site.register(User)   # добавляет юзеров в админ панель
admin.site.register(Product, ProductAdmin)
# admin.site.register(Shop, ShopAdmin)
