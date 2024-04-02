import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from camp_app.models import Booking
from . forms import *

def index(request):
    return render(request, 'index.html')

def camp(request):
    return render(request, 'camp/camp.html')


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
    camp_name = "Camp One"
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
                selected_camp_name = camp_name
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
                total_price = request.POST.get('hidden_package_amount')
                form.instance.total_price = total_price
                form.save() 
                
                fullname = form.cleaned_data['full_name']
                package = form.cleaned_data['package']
                people = form.cleaned_data['number_of_people']
                email = form.cleaned_data['email_address']
                contact_number = form.cleaned_data['mobile_number']
                date = form.cleaned_data['booking_date']
                
                subject = 'Booking Confirmation'
                html_message = render_to_string('camp/booking_confirmation.html', {
                    'camp_name': camp_name,
                    'fullname': fullname,
                    'package': package,
                    'people': people,
                    'email': email,
                    'contact_number': contact_number,
                    'date': date,
                    'total_price': total_price                    
                })  
                          
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to_email = ['ghosthunter5470@gmail.com']
                send_mail(subject, plain_message, from_email, to_email, html_message=html_message, fail_silently=False)
                    
                return redirect("thankyou")
            else:
                form = BookingForm()

        
        
    context = {
        'availability_form': availability_form,
        'booking_form': booking_form,
        'availability_message': availability_message,
        'status': status,
        'camp_name': camp_name
    }

    return render(request, 'camp/camp_one.html', context)


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
                selected_camp_name = camp_name
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
                total_price = request.POST.get('hidden_package_amount')
                form.instance.total_price = total_price
                form.save() 
                
                fullname = form.cleaned_data['full_name']
                package = form.cleaned_data['package']
                people = form.cleaned_data['number_of_people']
                email = form.cleaned_data['email_address']
                contact_number = form.cleaned_data['mobile_number']
                date = form.cleaned_data['booking_date']
                
                subject = 'Booking Confirmation'
                html_message = render_to_string('camp/booking_confirmation.html', {
                    'camp_name': camp_name,
                    'fullname': fullname,
                    'package': package,
                    'people': people,
                    'email': email,
                    'contact_number': contact_number,
                    'date': date,
                    'total_price': total_price                    
                })  
                          
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to_email = ['ghosthunter5470@gmail.com']
                send_mail(subject, plain_message, from_email, to_email, html_message=html_message, fail_silently=False)
                    
                return redirect("thankyou")
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



def camp_three(request):
    camp_name = "Camp Three"
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
                selected_camp_name = camp_name
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
                total_price = request.POST.get('hidden_package_amount')
                form.instance.total_price = total_price
                form.save() 
                
                fullname = form.cleaned_data['full_name']
                package = form.cleaned_data['package']
                people = form.cleaned_data['number_of_people']
                email = form.cleaned_data['email_address']
                contact_number = form.cleaned_data['mobile_number']
                date = form.cleaned_data['booking_date']
                
                subject = 'Booking Confirmation'
                html_message = render_to_string('camp/booking_confirmation.html', {
                    'camp_name': camp_name,
                    'fullname': fullname,
                    'package': package,
                    'people': people,
                    'email': email,
                    'contact_number': contact_number,
                    'date': date,
                    'total_price': total_price                    
                })  
                          
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to_email = ['ghosthunter5470@gmail.com']
                send_mail(subject, plain_message, from_email, to_email, html_message=html_message, fail_silently=False)
                    
                return redirect("thankyou")
            else:
                form = BookingForm()

        
        
    context = {
        'availability_form': availability_form,
        'booking_form': booking_form,
        'availability_message': availability_message,
        'status': status,
        'camp_name': camp_name
    }

    return render(request, 'camp/camp_three.html', context)


def thankyou(request):
    return render(request, 'thankyou.html')