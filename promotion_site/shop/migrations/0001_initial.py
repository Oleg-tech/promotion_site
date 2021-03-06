# Generated by Django 4.0.3 on 2022-07-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('old_price', models.CharField(max_length=20, verbose_name='Старая цена')),
                ('new_price', models.CharField(max_length=20, verbose_name='Новая цена')),
                ('picture', models.CharField(max_length=100, verbose_name='Фото')),
                ('percent_of_sale', models.CharField(max_length=10, verbose_name='Скидка')),
                ('date_of_end', models.CharField(max_length=10, verbose_name='Окончание')),
                ('category', models.CharField(max_length=20, verbose_name='Категория')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
                ('shop_name', models.CharField(max_length=20, verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'category'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('mail', models.CharField(max_length=30, verbose_name='Почта')),
                ('date_of_registration', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
        ),
    ]
