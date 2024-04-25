from django.contrib import admin
from camp_app.models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):        
    list_display = ['full_name', 'camp_name', 'booking_date', 'mobile_number', 'package', 'number_of_people', 'total_price', 'email_address', 'completed']
    list_filter = ['booking_date']
    search_fields = ['mobile_number']

@admin.register(CompletedBooking)
class CompletedBookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'camp_name', 'mobile_number', 'package', 'number_of_people', 'total_price', 'email_address']
    list_filter = ['full_name']
    search_fields = ['full_name', 'email_address']
    
    def __str__(self):
        return f'{self.full_name} - {self.email_address}'
    
   