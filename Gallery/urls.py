from django.urls import path  
from .import views

urlpatterns = [
    path("GalleryAdd",views.GalleryAdd,name="GalleryAdd"),
    path("DeleteGallery/<int:pk>",views.DeleteGallery,name="DeleteGallery"),
    path("GalleryView",views.GalleryView,name="GalleryView"),
    path("AddNews",views.AddNews,name="AddNews"),
    path("DeleteNews/<int:pk>",views.DeleteNews,name="DeleteNews"),
    path("NewsView",views.NewsView,name="NewsView")
]
