import django


from django.urls import path
from.import views

urlpatterns = [
    path('destiantion_list',views.destiantion_list,name='destiantion_list'),
    path('add_destination',views.add_destination,name='add_destination'),
    path('update_destination',views.update_destination,name='update_destination'),
    path('delete_destination',views.delete_destination,name='delete_destination'),
    
    path('destination_customer_view',views.destination_customer_view,name="destination_customer_view"),
    
]
