# Generated by Django 4.2.2 on 2024-04-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp_app', '0011_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='completedbooking',
            name='booking_date',
            field=models.DateField(default=''),
        ),
    ]
