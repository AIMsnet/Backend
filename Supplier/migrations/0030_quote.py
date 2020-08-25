# Generated by Django 3.0.6 on 2020-08-22 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_auto_20200529_1512'),
        ('Supplier', '0029_auto_20200807_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('requirement', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.Supplier')),
            ],
        ),
    ]