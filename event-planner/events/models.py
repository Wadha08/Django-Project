from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='organizer')
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()

    def get_seats_booked(self):
        books = self.bookings.all()
        total = 0
        for book in books:
            total = total + book.num_seats
        return total

    def get_seats_left(self):
        return self.seats - self.get_seats_booked()

    def full(self):
        return self.get_seats_left == 0

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'event_id':self.id})

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='attended')
    num_seats = models.IntegerField()
    event = models.ForeignKey(Event, default=1, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return self.user.username

