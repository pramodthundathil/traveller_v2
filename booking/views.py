from email.headerregistry import Address
import imp
from importlib.resources import Package
from django.shortcuts import redirect, render
from packages.models import Packages
from .models import BookingPackage

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signup')
def booking_form(request):
    
    package_id = request.POST["submit"]
    packages = Packages.objects.filter(Package_id = package_id)    
    
    return render(request,"booking/booking_form.html",{'packages': packages})

@login_required(login_url='signup')
def booking_create(request):
    
    package_id = request.POST["submit"]
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
    
    booking = BookingPackage.objects.create(Package_id = package_id,customer_id = request.user,Name = customer_fullname,Number_of_Gusts = guest_count,Number_of_Gusts_below5 = infent_number,Address_House = address ,Locality = locality ,state = state,Country = contry,phone = phone_number,email = email ,trip_start_date = start_date ,Payment_amount =False,approval_status = False)
    
    packages = Packages.objects.filter(Package_id = package_id)    
    booking.save()
    booking_id = booking.Bookingid
    
        
    return render(request,"booking/payment.html",{"Packages":packages,"booking_id":booking_id})

@login_required(login_url='signup')
def update_booking(request):
    bookings = BookingPackage.objects.all()
    
    if request.method == "POST":
        booking_id = request.POST['submit']
        booking = BookingPackage.objects.filter(Bookingid=booking_id)
        bookings = BookingPackage.objects.get(Bookingid=booking_id)
        package_id = bookings.Package_id
        package = Packages.objects.filter(Package_id = package_id )
        return render(request,"booking/edit_booking.html",{"booking":booking,"package":package})
    
    return render(request,'booking/update_booking.html',{"bookings":bookings})

@login_required(login_url='signup')
def edit_booking(request):
    
    pass
        
