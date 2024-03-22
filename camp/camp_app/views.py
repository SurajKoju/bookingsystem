import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from camp_app.models import Booking
from . forms import *

def index(request):
    return render(request, 'index.html')


def check_availability(request):
    availability_form = AvailabilityCheckForm()
    booking_form = BookingForm()
    availability_message = ""  # Initialize the variable before the 'if' block
    status = "available"  # Initialize status before the loop

    if request.method == 'POST':
        availability_form = AvailabilityCheckForm(request.POST)

        if availability_form.is_valid():
            selected_date = availability_form.cleaned_data.get('availability_date')
            # selected_date = timezone.datetime.strptime(selected_date_str, '%Y-%m-%d').date()
            selected_camp_name = availability_form.cleaned_data.get('camp_name') 
            
            bookings_for_date = Booking.objects.filter(booking_date=selected_date, camp_name=selected_camp_name)

            if bookings_for_date.exists():
                status = "Not available"
                availability_message = f"{selected_camp_name} is not available on {selected_date}. Please choose any other date"
            else:
                availability_message = f"{selected_camp_name} is available on {selected_date}. Make a Booking by filling the form below."

    context = {
        'availability_form': availability_form,
        'booking_form': booking_form,
        'availability_message': availability_message,
        'status': status,
    }

    return render(request, 'book/availability_form.html', context)


def camp_one(request):
    form = BookingForm()
    camp_name = "Camp One"
    initial_data = {'camp_name': camp_name}  # Set initial data for the form
    form = BookingForm(initial=initial_data)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponse("<h4 class = 'text-center'>Success</h4>")
        else:
            form = BookingForm()
            
    return render(request, 'camp/camp_one.html', {'form': form, 'camp_name': camp_name})


def camp_two(request):
    camp_name = "Camp Two"
    initial_data = {'camp_name': camp_name}
    
    availability_form = AvailabilityCheckForm(initial=initial_data)
    booking_form = BookingForm(initial=initial_data)
    
    availability_message = ""  
    status = "Not available"


    if request.method == 'POST':
        if 'availability_submit' in request.POST:
            availability_form = AvailabilityCheckForm(request.POST)
            if availability_form.is_valid():
                selected_date = availability_form.cleaned_data.get('availability_date')
                selected_camp_name = "Camp Two"
                bookings_for_date = Booking.objects.filter(booking_date=selected_date, camp_name=selected_camp_name)

                if bookings_for_date.exists():
                    status = "Not available"
                    availability_message = f"{selected_camp_name} is not available on {selected_date}. Please choose any other date"
                else:
                    status = "available"
                    availability_message = f"{selected_camp_name} is available on {selected_date}. Make a Booking by filling the form below."
        
        # Check if the booking form is being submitted
        elif 'booking_submit' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save() 
                return HttpResponse("<h4 class='text-center'>Success</h4>")
            else:
                form = BookingForm()

        
        
    context = {
        'availability_form': availability_form,
        'booking_form': booking_form,
        'availability_message': availability_message,
        'status': status,
        'camp_name': camp_name
    }

    return render(request, 'camp/camp_two.html', context)