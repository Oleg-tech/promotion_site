# Generated by Django 4.0.3 on 2022-07-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_shop_alter_product_options_product_shop_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'category'], 'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_name',
            field=models.CharField(max_length=20, verbose_name='Магазин'),
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]