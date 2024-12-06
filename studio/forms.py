from django import forms
from .models import Client, Photographer, Booking

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }

class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = ['name', 'expertise']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Photographer Name'}),
            'expertise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expertise (e.g., Portraits, Weddings)'}),
        }

class BookingForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    photographer = forms.ModelChoiceField(queryset=Photographer.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    shoot_type = forms.ChoiceField(choices=Booking.SHOOT_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    location = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'})
    notes = forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Additional Notes'})

    class Meta:
        model = Booking
        fields = ['client', 'photographer', 'shoot_type', 'date', 'time', 'location', 'notes']
