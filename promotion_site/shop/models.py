from django.db import models
from datetime import date

from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=255, verbose_name="Имя пользователя")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    mail = models.CharField(max_length=30, verbose_name="Почта")
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    old_price = models.CharField(max_length=20, verbose_name="Старая цена")
    new_price = models.CharField(max_length=20, verbose_name="Новая цена")
    # picture = models.ImageField(upload_to='photos', null=True, verbose_name="Фото")
    percent_of_sale = models.CharField(max_length=10, verbose_name="Скидка")
    date_of_end = models.CharField(max_length=10, verbose_name="Окончание")
    category = models.CharField(max_length=20, verbose_name="Категория")
    # shop_name = models.ForeignKey("Shop", on_delete=models.PROTECT, null=True, verbose_name="Магазин")
    shop_name = models.CharField(max_length=20, verbose_name="Магазин")

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ['name', 'category']

    # def absolute_url(self):
    #     return reverse('name', kwargs={'shop': self.name})

#
# class Shop(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Название")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Магазины"
#         verbose_name_plural = "Магазины"
#         # ordering = ['name']

