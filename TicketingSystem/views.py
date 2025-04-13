from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_guests(request):   #get all guests
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests , many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_guest(request):    #add a new guest
    serializer = GuestSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def get_guest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)   
    except Guest.DoesNotExist:
        return Response({"error":"guest not found"},status=status.HTTP_404_NOT_FOUND)
    serializer = GuestSerializer(guest)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_guest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)   
    except Guest.DoesNotExist:
        return Response({"error":"guest not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = GuestSerializer(guest, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def delete_guest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)   
    except Guest.DoesNotExist:
        return Response({"error":"guest not found"},status=status.HTTP_404_NOT_FOUND)
    
    guest.delete()
    return Response({'Success':'Deleted Successfully...'}, status=status.HTTP_204_NO_CONTENT)
    