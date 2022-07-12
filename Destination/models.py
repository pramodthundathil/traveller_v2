from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Destination_List(models.Model):
    
    Destination_id = models.AutoField(primary_key=True)
    Destination_Name = models.CharField(max_length=100)
    Destination_state = models.CharField(max_length=100)
    Destination_contry = models.CharField(max_length=100)
    Destination_discription = models.CharField(max_length=1000)
    Destination_image = models.ImageField(upload_to = 'Destination_image')
    
