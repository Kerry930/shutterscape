from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/new/', views.new_booking, name='new_booking'),
]
