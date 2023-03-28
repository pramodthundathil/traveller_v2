from django.urls import path
from.import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('signup',views.signup,name='signup'),
    path('registration',views.registration,name="registration"),
    path('signout',views.signout,name='signout'),
    path('FeedBacks',views.FeedBacks,name='FeedBacks'),
    path('CustomerFeedbacks',views.CustomerFeedbacks,name='CustomerFeedbacks'),
    path('ReplayFeed/<int:pk>',views.ReplayFeed,name='ReplayFeed'), 
    
] 