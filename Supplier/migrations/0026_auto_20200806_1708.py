# Generated by Django 3.0.6 on 2020-08-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0025_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_main_category',
            name='image',
            field=models.FileField(upload_to='./HomePage/static/Pics'),
        ),
    ]
