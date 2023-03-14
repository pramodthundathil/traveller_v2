from django.db import models

class GalleryImage(models.Model):
    destination_name = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    image = models.FileField(upload_to='Gallery')
    
class News(models.Model):
    news_title = models.CharField(max_length=255)
    news = models.CharField(max_length=2000)
    news_image = models.FileField(upload_to='news_image')
    date = models.DateTimeField(auto_now_add=True)



