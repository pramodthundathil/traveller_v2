
from django.contrib import messages
from django.shortcuts import redirect, render

from .froms import PackageAddForm
from Destination.models import Destination_List
from .models import Packages

from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users

# Create your views here.
@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def view_packages(request):
    
    package_list = Packages.objects.all()
    
    return render(request,'Packages/view_packages.html',{"package_list":package_list})


@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def add_package(request):
    
    package_add_form = PackageAddForm()
    destination_list = Destination_List.objects.all()
    
    if request.method == 'POST':
        
        destination = request.POST['destination']
        duration = request.POST['duration']
        price = request.POST['price']
        food_status = request.POST['f_status']
        transportation = request.POST['trans']
        discription = request.POST['dis']
        
        destination_one = Destination_List.objects.get(Destination_Name = destination)
        destination_id = destination_one.Destination_id 
        
        package = Packages.objects.create(Package_duration= duration ,Package_foodstatus= food_status,Package_destination= destination,Package_destination_id= destination_id ,Package_price= price, Package_discription= discription ,Package_Transpotation_status= transportation)
        package.save()
        
        messages.info(request,"Package Added Successfully")
        return redirect('add_package')
         
    context = {"package_add_form":package_add_form,'destination_list':destination_list}
    
    return render(request,'Packages/add_package.html',context)


@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def edit_package(request):
    
    package_list = Packages.objects.all()
    
    if request.method == 'POST':
        
        package_id = request.POST['submit']
        package = Packages.objects.filter(Package_id = package_id)
        
        return render (request,'Packages/update_package.html',{'package':package})
        
    return render(request,'Packages/edit_package.html',{"package_list":package_list})

@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def update_package(request):
    
    duration = request.POST['duration']
    price = request.POST['price']
    food_status = request.POST['f_status']
    transportation = request.POST['trans']
    discription = request.POST['dis']
    package_id = request.POST['pack_id']
    
    package = Packages.objects.get(Package_id = package_id)
    package.Package_duration = duration
    package.Package_foodstatus = food_status
    package.Package_price = price
    package.Package_Transpotation_status = transportation
    package.Package_discription = discription
    package.save()
    
    messages.info(request,'Package Updated Succesfully')
    return redirect('edit_package')

@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def delete_package(request):
    
    if request.method == 'POST':
        
        package_id = request.POST['submit']
        package = Packages.objects.get(Package_id = package_id)
        package.delete()
        
        messages.info(request,'Package Deleted')
        return redirect('delete_package')
    
    package_list = Packages.objects.all()
    return render(request,'Packages/delete_package.html',{"package_list":package_list})

def package_customer_view(request):
    
    package = Packages.objects.all()
    return render(request,'home/packages.html',{'package':package})

def package_customer_view_Destination_click(request,pk):
    
    desti = Destination_List.objects.get(Destination_id = pk)
    package = Packages.objects.filter(Package_destination_id = desti.Destination_id)
    return render(request,'home/packages.html',{'package':package})
