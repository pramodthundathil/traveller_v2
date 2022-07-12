from django.http import HttpResponse
from django.shortcuts import render,redirect
from .froms import UserAddform
from django.contrib.auth import authenticate,login,logout

from .decorators import unautenticated_user, admin_only, allowed_users
from django.contrib.auth.decorators import login_required

from Destination.models import Destination_List
from packages.models import Packages


from django.contrib import messages
from django.contrib.auth.models import User 

# Create your views here.

@admin_only
def home(request):
  
    Destination_List_items = Destination_List.objects.all()
    package = Packages.objects.all()
    
    return render (request,'index.html',{'Destination_List_items':Destination_List_items,'package':package})

@login_required(login_url='signup')
@allowed_users(allowed_roles=["admin"])
def admin_page(request):
    return render(request,'admin_index.html')

@unautenticated_user
def signup(request):
    
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('home')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('signup')
    
    return render(request,'login.html')

def signout(request):
    
    logout(request)
    return redirect('home')

@unautenticated_user
def registration(request):
    
    UserCreateForm = UserAddform()
    
    if request.method == 'POST':
        
        form = UserAddform(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                new_user = form.save()
                new_user.save()
                
                messages.success(request,"User Created Successfully...")
                return redirect('signup')
    
    return render(request,'register.html',{'UserCreateForm':UserCreateForm})