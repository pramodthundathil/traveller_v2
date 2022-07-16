from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookingPackage(models.Model):
    
    Bookingid = models.AutoField(primary_key=True)
    Package_id = models.CharField(max_length=100)
    Destination_id = models.CharField(max_length=100,null=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Number_of_Gusts  = models.CharField(max_length=100)
    Number_of_Gusts_below5 = models.CharField(max_length=100, null=True)
    Address_House = models.CharField(max_length=300)
    Locality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    trip_start_date = models.DateField(auto_now_add=False,null=False)
    additional_request = models.CharField(max_length=500,null = True)
    customer_feedback = models.CharField(max_length=500,null=True)
    Payment_amount = models.FloatField(max_length=100)
    Payment_status = models.BooleanField(null=True)
    approval_status = models.BooleanField(null=True)
    

