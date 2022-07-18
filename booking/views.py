
from importlib.resources import Package
from django.contrib import messages
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
    booking.save()
    
    packages = Packages.objects.filter(Package_id = package_id)
    package = Packages.objects.get(Package_id = package_id) 
    price = package.Package_price
    
    total_amount = float(price) * int(guest_count) + float(price)/2 * int(infent_number)
    
    booking_id = booking.Bookingid
    
        
    return render(request,"booking/payment.html",{"Packages":packages,"booking":booking,"total_amount":total_amount})

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
def approve_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = True
    booking.save()
    return redirect ('update_booking')

@login_required(login_url='signup')
def reject_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = False
    booking.save()
    return redirect ('update_booking')
@login_required(login_url='signup')
def pending_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = None
    booking.save()
    return redirect ('update_booking')

@login_required(login_url='signup')
def customer_booking(request):
    
    user = request.user
    bookings = BookingPackage.objects.filter(customer_id = user)
    
    if request.method == 'POST':
        
        booking_id = request.POST['submit']
        booking = BookingPackage.objects.get(Bookingid=booking_id)
        booking.Payment_status = None
        booking.save()
        return redirect ('customer_booking')
    
    return render(request,'booking/customer_booking.html',{"bookings":bookings})

@login_required(login_url="signup")
def delete_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.delete()
    messages.info(request,"Booking Deleted successfuly")
    return redirect ('update_booking')

    
    
        
