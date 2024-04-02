from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Booking(models.Model):
    camp_name = models.CharField(max_length=20, default = "", null=False)
    full_name = models.CharField(default = '', max_length=100, null=False)
    address = models.CharField(default = '', max_length=255, null=False)
    mobile_number = models.CharField(default = '', max_length=10, null=False)
    email_address = models.EmailField(default = '', blank=True, null=True)
    number_of_people = models.PositiveIntegerField(default=2, blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    PAYMENT_CHOICES = [
        ('ESEWA', 'Esewa'),
        ('KHALTI', 'Khalti'),
        ('ONCASH', 'On-Cash Payment'),
    ]
    
    PACKAGE_CHOICES = [
        ('basic', 'Basic (Rs. 800 per person)'),
        ('medium', 'Medium (Rs. 1200 per person)'),
        ('deluxe', 'Deluxe (Rs. 1800 per person)'),
    ]

    package = models.CharField(max_length=10, default = '', choices=PACKAGE_CHOICES, null=False)
    payment_method = models.CharField(max_length=6, choices=PAYMENT_CHOICES, null=False)
    booking_date = models.DateField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    completed = models.BooleanField(default=False, editable=True)
    
    def __str__(self):
        return self.full_name

class CompletedBooking(models.Model):
    camp_name = models.CharField(max_length=20, default="", null=False)
    full_name = models.CharField(default = '', max_length=100, null=False)
    mobile_number = models.CharField(default = '', max_length=10, null=False)
    email_address = models.EmailField(blank=True, null=True)
    number_of_people = models.PositiveIntegerField(default=2, blank=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    package = models.CharField(max_length=10, default='', choices=Booking.PACKAGE_CHOICES, null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.full_name


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Booking)
def move_to_completed(sender, instance, created, **kwargs):
    if instance.completed:
        CompletedBooking.objects.create(
            camp_name=instance.camp_name,
            full_name=instance.full_name,
            mobile_number=instance.mobile_number,
            email_address=instance.email_address,
            number_of_people=instance.number_of_people,
            package=instance.package,
            total_price=instance.total_price
        )
        instance.delete()


class availability_form(models.Model):
    camp_name = models.CharField(max_length=20, default = "", null=False)
    availability_date = models.DateField(blank= True,null=True)

