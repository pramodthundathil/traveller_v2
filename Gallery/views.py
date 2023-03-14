from django.shortcuts import render, redirect
from .forms import GalleryForm, NewsAddForm
from .models import GalleryImage,News
from django.contrib import messages

# Create your views here.
def GalleryAdd(request):
    form = GalleryForm
    gallery = GalleryImage.objects.all()
    if request.method == "POST":
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Gallery Added")
            return redirect('GalleryAdd')
    context = {
        "form":form,
        "gallery":gallery
    }
    return render(request,'adminaddgallery.html',context)

def DeleteGallery(request,pk):
    gallery = GalleryImage.objects.get(id = pk)
    gallery.delete()
    messages.info(request,'Item deleted')
    return redirect('GalleryAdd')

def GalleryView(request):
    gallery = GalleryImage.objects.all()
    context = {
        "gallery":gallery
    }
    return render(request,'gallery.html',context)

def AddNews(request):
    form = NewsAddForm()
    news = News.objects.filter()
    if request.method == "POST":
        form = NewsAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"News Saved")
            return redirect("AddNews")
    context = {
        "form":form,
        "news":news
    }
    return render(request,'addnews.html',context)

def DeleteNews(request,pk):
    news = News.objects.get(id = pk)
    news.news_image.delete()
    news.delete()
    messages.info(request,'News Deleted')
    return redirect('AddNews')

def NewsView(request):
    news = News.objects.all()
    context = {
        "news":news
    }
    return render(request,'news.html',context)