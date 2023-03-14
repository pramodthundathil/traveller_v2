from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import DestinationAddForm
from .models import Destination_List
from django.contrib.auth.decorators import login_required

from home.decorators import allowed_users


# Create your views here.
@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def destiantion_list(request):
    
    Destination_List_items = Destination_List.objects.all()
    
    return render(request,'destination/destination_view.html',{'Destination_List_items':Destination_List_items})

@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def add_destination(request):
    
    Destination_add_form = DestinationAddForm()
    if request.method == 'POST':
        
        form = DestinationAddForm(request.POST, request.FILES)
        
        if form. is_valid():
            form_data = form.save()
            form_data.save()
            
            messages.info(request,"Destination Added To List")
            return redirect('add_destination')
        
        else:
            form = DestinationAddForm()
            messages.info(request,"Not Done")
            return redirect('add_destination')
    
    return render(request,'Destination/add_destination.html',{'Destination_add_form':Destination_add_form})

@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def update_destination(request):
    
    Destination_List_items = Destination_List.objects.all()
    
    return render(request,'destination/update_destination.html',{'Destination_List_items':Destination_List_items})

@allowed_users(allowed_roles=["admin"])
@login_required(login_url='signup')
def delete_destination(request):
    
    Destination_List_items = Destination_List.objects.all()
    return render(request,"destination/delete_destination.html",{'Destination_List_items':Destination_List_items})

def deletedestinationdone(request,pk):
    dest = Destination_List.objects.get(Destination_id = pk)
    dest.Destination_image.delete()
    dest.delete()
    messages.info(request,'Destination deleted')
    return redirect('delete_destination')

def destination_customer_view(request):
    
    Destination_List_items = Destination_List.objects.all()
    
    return render (request,'home/destinations.html',{'Destination_List_items':Destination_List_items})
