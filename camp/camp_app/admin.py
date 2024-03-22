# from django.contrib import admin
# from camp_app.models import *

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):        
#     list_display = ['full_name', 'address', 'mobile_number', 'email_address', 'number_of_people', 'PAYMENT_CHOICES', 'payment_method', 'booking_date']
#     list_filter = ['booking_date']
#     search_fields = ['mobile_number']
    
#     def __str__(self):
#         return f'{self.user_name} - {self.email}'

from django.contrib import admin
from camp_app.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):        
    list_display = ['full_name', 'camp_name', 'booking_date', 'mobile_number', 'number_of_people', 'get_payment_method', 'email_address', 'address']
    list_filter = ['booking_date']
    search_fields = ['mobile_number']
    
    def get_payment_method(self, obj):
        payment_choices = dict(Booking.PAYMENT_CHOICES)
        return payment_choices.get(obj.payment_method, 'Unknown')
    
    get_payment_method.short_description = 'Payment Method'
