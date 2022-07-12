from django.db import models
from sklearn.metrics import max_error

# Create your models here.

class Packages(models.Model):
    
    Package_id = models.AutoField(primary_key=True)
    Package_duration = models.CharField(max_length=500)
    Package_foodstatus = models.CharField(max_length=500)
    Package_destination = models.CharField(max_length=100)
    Package_destination_id = models.CharField(max_length=100)
    Package_price = models.CharField(max_length=100)
    Package_discription = models.CharField(max_length=1000)
    Package_Transpotation_status = models.CharField(max_length=500) 
