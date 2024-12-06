from django.contrib import admin
from .models import Client, Photographer, Booking

admin.site.register(Client)
admin.site.register(Photographer)
admin.site.register(Booking)
