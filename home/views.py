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
from django.contrib.auth.models import Group 
from Gallery.models import GalleryImage
from .models import FeedbackItems


@admin_only
def home(request):
    
    Destination_List_items = Destination_List.objects.all()
    gallery = GalleryImage.objects.all()
    package = Packages.objects.all()
    
    return render (request,'index.html',{'Destination_List_items':Destination_List_items,'package':package,"gallery":gallery})



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
    
    return render(request,'registration/login.html')

def signout(request):
    
    logout(request)
    return redirect('home')

@unautenticated_user
def registration(request):
    
    form = UserAddform()
    
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
                group = Group.objects.get(name='customer')
                new_user.groups.add(group) 
                
                messages.success(request,"User Created Successfully...")
                return redirect('signup')
    
    return render(request,'register.html',{'form':form})

@login_required(login_url='signup')
def FeedBacks(request):
    feedback1 = FeedbackItems.objects.filter(user = request.user)
    if request.method == "POST":
        feedback = request.POST['feedback']
        fb = FeedbackItems.objects.create(user = request.user,feedback = feedback)
        fb.save()
        messages.info(request,'feddback submitted')
        return redirect('FeedBacks')
    context = {
        "feedback":feedback1
    }
    
    return render(request,'feedbacks.html',context)

@login_required(login_url='signup')
def CustomerFeedbacks(request):
    feedback1 = FeedbackItems.objects.all()
    
    context = {
        "feedback":feedback1
    } 
    return render(request,"feddbacksadmin.html",context)

def ReplayFeed(request,pk):
    if request.method == "POST":
        replay = request.POST['replay']
        feed = FeedbackItems.objects.get(id = pk)
        feed.replay = replay
        feed.save()
        messages.info(request,"Replayed feedback success ")    
    
    return redirect('CustomerFeedbacks')