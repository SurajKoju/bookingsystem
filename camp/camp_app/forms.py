from django import forms
from . models import *
from django.utils import timezone


class BookingForm(forms.ModelForm):


    class Meta:
        model = Booking
        fields = ['camp_name','full_name', 'address', 'mobile_number', 'email_address', 'number_of_people', 'package', 'booking_date', 'payment_method']
        
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat(), 'max': timezone.now().date().replace(month=12, day=31).isoformat()}),
        }
        
        
class AvailabilityCheckForm(forms.ModelForm):
    availability_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 
                                      'min': timezone.now().date().isoformat(),
                                      'max': timezone.now().date().replace(month=12, day=31).isoformat()})
    )

    class Meta:
        model = availability_form
        fields = ['availability_date', 'camp_name']