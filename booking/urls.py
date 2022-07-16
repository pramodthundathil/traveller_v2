from django.urls import path
from .import views

urlpatterns = [
    path('booking_form',views.booking_form,name="booking_form"),
    path('booking_create',views.booking_create,name='booking_create'),
    path('update_booking',views.update_booking,name = 'update_booking'),
    path('edit_booking',views.edit_booking,name='edit_booking'),
    
]
