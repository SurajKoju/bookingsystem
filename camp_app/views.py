import datetime
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import requests
import uuid
import hashlib
import base64


from camp_app.models import Booking
from .forms import *


def index(request):
    return render(request, 'index.html')

def camp(request):
    return render(request, 'camp/camp.html')

def handle_booking(request, camp_name, template_name):
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
                bookings_for_date = Booking.objects.filter(booking_date=selected_date, camp_name=camp_name)
    
                if bookings_for_date.exists():
                    status = "Not available"
                    availability_message = f"{camp_name} is not available on {selected_date}. Please choose any other date"
                else:
                    status = "available"
                    availability_message = f"{camp_name} is available on {selected_date}. Make a Booking by filling the form below."
        
        elif 'booking_submit' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                payment_method = form.cleaned_data['payment_method']
                total_price = request.POST.get('hidden_package_amount')
                form.instance.total_price = total_price

                if payment_method == 'cash':
                    form.save()
                    return redirect("thankyou")
                elif payment_method == 'esewa':
                    # Prepare eSewa payment details
                    transaction_uuid = str(uuid.uuid4())
                    esewa_payment_url = "https://rc-epay.esewa.com.np/api/epay/main/v2/form"
                    esewa_merchant_code = "EPAYTEST"
                    esewa_success_url = request.build_absolute_uri('esewa_return/')
                    esewa_failure_url = request.build_absolute_uri('esewa_failure/')
                    esewa_amount = float(total_price)
                    esewa_tax_amount = 0.0
                    esewa_service_charge = 0.0
                    esewa_delivery_charge = 0.0
                    esewa_total_amount = esewa_amount + esewa_tax_amount + esewa_service_charge + esewa_delivery_charge

                    # Save the form data without committing to the database
                    booking = form.save(commit=False)
                    booking.transaction_uuid = transaction_uuid
                    booking.payment_method = 'esewa'
                    booking.save()

                    context = {
                        'esewa_payment_url': esewa_payment_url,
                        'amount': esewa_amount,
                        'tax_amount': esewa_tax_amount,
                        'total_amount': esewa_total_amount,
                        'transaction_uuid': transaction_uuid,
                        'product_code': esewa_merchant_code,
                        'product_service_charge': esewa_service_charge,
                        'product_delivery_charge': esewa_delivery_charge,
                        'success_url': esewa_success_url,
                        'failure_url': esewa_failure_url,
                        'signed_field_names': "total_amount,transaction_uuid,product_code",
                    }

                    return render(request, 'esewa/esewa_redirect.html', context)
    
    context = {
        'availability_form': availability_form,
        'booking_form': booking_form,
        'availability_message': availability_message,
        'status': status,
        'camp_name': camp_name,
    }

    return render(request, template_name, context)

def esewa_return(request):
    data = request.GET.get('data')
    
    # Decode the data
    import json
    decoded_data = json.loads(base64.b64decode(data).decode('utf-8'))
    
    transaction_uuid = decoded_data.get('transaction_uuid')
    amount = decoded_data.get('total_amount')
    status = decoded_data.get('status')

    if status == 'COMPLETED':
        booking = get_object_or_404(Booking, transaction_uuid=transaction_uuid)
        booking.payment_status = 'Completed'
        booking.save()
        return redirect('thankyou')
    else:
        return redirect('esewa/esewa_failure')

def esewa_failure(request):
    return render(request, 'esewa/esewa_failure.html')

def camp_one(request):
    return handle_booking(request, "Camp One", 'camp/camp_one.html')

def camp_two(request):
    return handle_booking(request, "Camp Two", 'camp/camp_two.html')

def camp_three(request):
    return handle_booking(request, "Camp Three", 'camp/camp_three.html')

def about(request):
    return render(request, 'about_us.html')

def thankyou(request):
    return render(request, 'thankyou.html')
