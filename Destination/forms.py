from django import forms

from .models import *
from django.forms import ModelForm

class DestinationAddForm(forms.ModelForm):
    
    class Meta:
        model = Destination_List
        fields = '__all__'