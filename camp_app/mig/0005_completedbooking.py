# Generated by Django 4.2.2 on 2024-04-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0004_booking_package_booking_total_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('camp_name', models.CharField(max_length=60)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
