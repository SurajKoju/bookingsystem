# Generated by Django 4.2.2 on 2024-07-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0002_remove_booking_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(default='cash', max_length=100),
        ),
        migrations.AddField(
            model_name='completedbooking',
            name='payment_method',
            field=models.CharField(default='cash', max_length=100),
        ),
    ]
