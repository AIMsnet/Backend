# Generated by Django 3.0.6 on 2020-06-22 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0017_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit',
        ),
    ]