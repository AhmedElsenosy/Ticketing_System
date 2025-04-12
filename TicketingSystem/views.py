from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_guests(request):
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests , many=True)
    return Response(serializer.data)
