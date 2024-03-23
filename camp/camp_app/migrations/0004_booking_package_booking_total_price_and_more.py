# Generated by Django 4.2.2 on 2024-03-23 05:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0003_availability_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.CharField(choices=[('basic', 'Basic (Rs. 800 per person)'), ('medium', 'Medium (Rs. 1200 per person)'), ('deluxe', 'Deluxe (Rs. 1800 per person)')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_people',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]