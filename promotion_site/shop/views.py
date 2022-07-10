import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


upper_menu = ['Всі магазини', 'Novus', 'Сільпо']
title = 'shop'
present_shop = None


def main_page(request):
    return render(request, 'shop/main.html', {'title': title, "upper_menu": upper_menu})


class ShowShop(ListView):
    model = Product
    template_name = 'shop/shop_print.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        return Product.objects.filter(shop_name=self.kwargs.get('shop'))


class ShowCategory(ListView):
    model = Product
    template_name = 'shop/shop_print.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        return Product.objects.filter(shop_name=self.kwargs.get('shop'), category=self.kwargs.get('cat'))


# def show_shop(request, shop):
#     shop_products = Product.objects.filter(shop_name=shop)
#     return render(request, 'shop/shop_print.html', {'products': shop_products})


# def show_category(request, shop, cate):
#     shop_products = Product.objects.filter(shop_name=shop, category=cate)
#     return render(request, 'shop/shop_print.html', {'products': shop_products})


# def silpo(request):
#     with open('shop/static/json/products.json', 'r') as file:
#         names_of_products = json.load(file)
#     return render(request, 'shop/index.html', {'products': names_of_products})


def reg(request):
    return HttpResponse('200')
