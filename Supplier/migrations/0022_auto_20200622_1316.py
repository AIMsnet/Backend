# Generated by Django 3.0.6 on 2020-06-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0021_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='requested_quote',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=65),
        ),
    ]