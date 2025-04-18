from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'guest_name', 'guest_mobile']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation 
        fields = '__all__'