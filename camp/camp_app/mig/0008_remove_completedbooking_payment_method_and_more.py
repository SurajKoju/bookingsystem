# Generated by Django 4.2.2 on 2024-04-01 05:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0007_booking_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedbooking',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='completedbooking',
            name='mobile_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='completedbooking',
            name='number_of_people',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='completedbooking',
            name='package',
            field=models.CharField(choices=[('basic', 'Basic (Rs. 800 per person)'), ('medium', 'Medium (Rs. 1200 per person)'), ('deluxe', 'Deluxe (Rs. 1800 per person)')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email_address',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='completedbooking',
            name='camp_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='completedbooking',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='completedbooking',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]