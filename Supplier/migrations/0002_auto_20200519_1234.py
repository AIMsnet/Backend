# Generated by Django 3.0.6 on 2020-05-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_type', models.CharField(max_length=255)),
                ('ownership_type', models.CharField(max_length=255)),
                ('business_type', models.CharField(max_length=255)),
                ('business_email', models.EmailField(max_length=255)),
                ('website_link', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('year_of_establishment', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='areaStreet',
            new_name='area_street',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='emailOptional',
            new_name='email_optional',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='middleName',
            new_name='middle_name',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='mobileNumber',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='supplier',
            name='designation',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='DD/MM/YYYY')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='DD/MM/YYYY')),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('clicks', models.DecimalField(decimal_places=0, max_digits=12)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.Business')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.Supplier'),
        ),
    ]
