# Generated by Django 3.0.6 on 2020-06-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0009_auto_20200610_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='ownership_type',
            field=models.CharField(choices=[('Proprietor', 'Proprietor'), ('Partnership Firm', 'Partnership Firm'), ('Limited Company (Ltd/Pvt.Ltd)', 'Limited Company (Ltd/Pvt.Ltd)'), ('Limited Liability Partnership (LLP)', 'Limited Liability Partnership (LLP)')], max_length=255),
        ),
    ]
