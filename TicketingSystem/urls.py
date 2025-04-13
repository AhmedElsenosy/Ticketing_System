from django.urls import path
from . import views

urlpatterns = [
    path('get_guests', views.get_guests, name='get_guests'),
    path('add_guest', views.add_guest, name='add_guest'),
    path('get_guest/<str:pk>', views.get_guest, name='get_guest'),
    path('update_guest/<str:pk>', views.update_guest, name='update_guest'),
    path('delete_guest/<str:pk>', views.delete_guest, name='delete_guest'),
]
