from django import forms

from .models import *
from django.forms import ModelForm

class PackageAddForm(forms.ModelForm):
    
    class Meta:
        model = Packages
        fields = '__all__'