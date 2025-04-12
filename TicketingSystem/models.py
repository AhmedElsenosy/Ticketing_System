from django.db import models

# Create your models here.

# Guest -- Movie -- Reservation 

class Movie(models.Model):
    movie_name = models.CharField( max_length=50)
    movie_room = models.IntegerField()
    movie_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name


class Guest(models.Model):
    guest_name = models.CharField( max_length=50)
    guest_mobile = models.CharField( max_length=11)

    def __str__(self):
        return self.guest_name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reservation')