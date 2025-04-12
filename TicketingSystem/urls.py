from django.urls import path
from . import views

urlpatterns = [
    path('get_guests', views.get_guests, name='get_guests'),
]
