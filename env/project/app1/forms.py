from django import forms
from .models import Read

class Add(forms.ModelForm):
    class Meta:
        model = Read  
        fields = ['name', 'email', 'contact']
