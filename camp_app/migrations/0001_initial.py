# Generated by Django 4.2.2 on 2024-04-01 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='availability_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(default='', max_length=20)),
                ('availability_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(default='', max_length=20)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=255)),
                ('mobile_number', models.CharField(default='', max_length=10)),
                ('email_address', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('number_of_people', models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('package', models.CharField(choices=[('basic', 'Basic (Rs. 800 per person)'), ('medium', 'Medium (Rs. 1200 per person)'), ('deluxe', 'Deluxe (Rs. 1800 per person)')], default='', max_length=10)),
                ('payment_method', models.CharField(choices=[('ESEWA', 'Esewa'), ('KHALTI', 'Khalti'), ('ONCASH', 'On-Cash Payment')], max_length=6)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(default='', max_length=20)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('mobile_number', models.CharField(default='', max_length=10)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('number_of_people', models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('package', models.CharField(choices=[('basic', 'Basic (Rs. 800 per person)'), ('medium', 'Medium (Rs. 1200 per person)'), ('deluxe', 'Deluxe (Rs. 1800 per person)')], default='', max_length=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
