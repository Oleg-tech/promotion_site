# Generated by Django 4.0.3 on 2022-07-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_alter_user_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=0, max_length=20, verbose_name='Категория'),
            preserve_default=False,
        ),
    ]