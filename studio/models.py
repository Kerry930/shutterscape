from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    SHOOT_TYPE_CHOICES = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, null=True)
    shoot_type = models.CharField(max_length=20, choices=SHOOT_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.shoot_type} - {self.client.name} ({self.date})"
