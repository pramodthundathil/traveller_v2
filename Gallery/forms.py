from django.forms import ModelForm
from .models import GalleryImage,News

class GalleryForm(ModelForm):
    class Meta:
        model = GalleryImage
        fields = "__all__"
        
class NewsAddForm(ModelForm):
    class Meta:
        model = News
        fields = ["news_title","news","news_image"]
