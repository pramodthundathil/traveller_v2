from django.urls import path
from. import views

urlpatterns = [
    path('view_packages',views.view_packages,name="view_packages"),
    path('add_package',views.add_package,name='add_package'),
    path('delete_package',views.delete_package,name='delete_package'),
    path('edit_package',views.edit_package,name='edit_package'),
    path('update_package',views.update_package,name='update_package'),
    
    path('package_customer_view',views.package_customer_view,name='package_customer_view')
]
