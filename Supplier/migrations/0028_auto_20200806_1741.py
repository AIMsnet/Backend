# Generated by Django 3.0.6 on 2020-08-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0027_auto_20200806_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_main_category',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
