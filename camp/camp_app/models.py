from django.db import models

class Booking(models.Model):
    camp_name = models.CharField(max_length=20, default = "", null=False)
    full_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    mobile_number = models.CharField(max_length=15, null=False)
    email_address = models.EmailField(null=True)
    number_of_people = models.PositiveIntegerField(null=False)
    PAYMENT_CHOICES = [
        ('ESEWA', 'Esewa'),
        ('KHALTI', 'Khalti'),
        ('ONCASH', 'On-Cash Payment'),
    ]
    payment_method = models.CharField(max_length=6, choices=PAYMENT_CHOICES, null=False)
    booking_date = models.DateField(null=False)

class availability_form(models.Model):
    camp_name = models.CharField(max_length=20, default = "", null=False)
    availability_date = models.DateField(null=False)

