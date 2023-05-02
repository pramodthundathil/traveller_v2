from django.urls import path
from .import views

urlpatterns = [
    path('booking_form',views.booking_form,name="booking_form"),
    path('booking_create',views.booking_create,name='booking_create'),
    path('update_booking',views.update_booking,name = 'update_booking'),
    path('approve_booking',views.approve_booking,name='approve_booking'),
    
    path('reject_booking',views.reject_booking,name='reject_booking'),
    path('pending_booking',views.pending_booking,name="pending_booking"),
    path('customer_booking',views.customer_booking,name='customer_booking'),
    path('delete_booking',views.delete_booking,name='delete_booking'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path("BookingCancelbyCustomer/<int:pk>",views.BookingCancelbyCustomer,name="BookingCancelbyCustomer")
    
    
]
