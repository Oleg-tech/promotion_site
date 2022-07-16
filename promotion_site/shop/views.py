from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# from .forms import RegisterUser
from .models import Product


upper_menu = ['Всі магазини', 'Novus', 'Сільпо']
title = 'shop'
present_shop = None


def main_page(request):
    return render(request, 'shop/main.html', {'title': title, "upper_menu": upper_menu})


# def reg(request):
#     form = RegisterUser()
#     return render(request, 'shop/registration.html', {'form': form})
    # return HttpResponse('200')


class ShowShop(ListView):
    model = Product
    paginate_by = 28
    template_name = 'shop/shop_print.html'
    context_object_name = 'products'
    # p = Paginator(model, 10)

    def get_queryset(self, **kwargs):
        return Product.objects.filter(shop_name=self.kwargs.get('shop'))


class ShowCategory(ListView):
    model = Product
    template_name = 'shop/shop_print.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        return Product.objects.filter(shop_name=self.kwargs.get('shop'), category=self.kwargs.get('cat'))
