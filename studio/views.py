from django.shortcuts import render, redirect
from .models import Client, Photographer, Booking
from .forms import BookingForm, ClientForm, PhotographerForm

def home(request):
    return render(request, 'studio/home.html')
    

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'studio/booking_list.html', {'bookings': bookings})



def new_booking(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        photographer_form = PhotographerForm(request.POST)
        booking_form = BookingForm(request.POST)
        
        if client_form.is_valid() and photographer_form.is_valid() and booking_form.is_valid():
            client = client_form.save()
            photographer = photographer_form.save()
            
            booking = booking_form.save(commit=False)
            booking.client = client
            booking.photographer = photographer
            booking.save()
            
            print(f"Booking Saved: {booking}")  
            
            return redirect('booking_list')
    
    else:
        client_form = ClientForm()
        photographer_form = PhotographerForm()
        booking_form = BookingForm()
    
    return render(request, 'studio/new_booking.html', {
        'client_form': client_form,
        'photographer_form': photographer_form,
        'booking_form': booking_form
    })
