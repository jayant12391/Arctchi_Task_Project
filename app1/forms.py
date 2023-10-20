from django.forms import ModelForm
from .models import Task
from django import forms


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status')

        widgets = {
        'id': forms.TextInput(attrs={'class':'form-control'}),  
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}), 
        'status': forms.Select(attrs={'class':'form-control'}), 
    }