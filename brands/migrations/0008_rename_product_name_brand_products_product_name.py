# Generated by Django 3.2 on 2022-10-17 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0007_auto_20220909_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand_products',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
