from email.headerregistry import Address
import imp
from importlib.resources import Package
from django.shortcuts import render
from packages.models import Packages
from .models import BookingPackage

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signup')
def booking_form(request):
    
    package_id = request.POST["submit"]
    packages = Packages.objects.filter(Package_id = package_id)    
    
    if request == 'POST':
        
        customer_fullname = request.POST["fname"]
        guest_count = request.POST["gcount"]
        infent_number = request.POST["ccount"]
        start_date = request.POST["sdate"]
        end_date = request.POST["Edate"]
        phone_number = request.POST['pnumber']
        email = request.POST['email']
        address = request.POST['Address']
        locality = request.POST['locality']
        state = request.POST['state']
        contry = request.POST['contry']
        destination_id = request.POST['DID']
        
        booking = BookingPackage.objects.create(Package_id = package_id,Destination_id = destination_id ,customer_id = request.user,Name = customer_fullname,Number_of_Gust = guest_count,Number_of_Gusts_below5 = infent_number,Address_House = address ,Locality = locality ,state = state,Country = contry,phone = phone_number,email = email ,trip_start_date = start_date ,Payment_amount =False,approval_status = False)
        
        booking.save()
        booking_id = booking.Bookingid
        
        return render(request,"booking/paymet.html",{"Packages":packages,"booking_id":booking_id})
        
    
    return render(request,"booking/booking_form.html",{'packages': packages})
