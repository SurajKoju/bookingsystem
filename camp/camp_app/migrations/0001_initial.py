# Generated by Django 4.2.2 on 2024-03-20 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('number_of_people', models.PositiveIntegerField()),
                ('payment_method', models.CharField(choices=[('ESEWA', 'Esewa'), ('KHALTI', 'Khalti'), ('ONCASH', 'On-Cash Payment')], max_length=6)),
                ('booking_date', models.DateField()),
            ],
        ),
    ]
