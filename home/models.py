from django.db import models
from django.contrib.auth.models import User

class FeedbackItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=1000)
    replay = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
