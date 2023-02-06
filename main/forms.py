from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "decision"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'class': 'list-group-item list-group-item-action list-group-item-info', 'placeholder': 'Введите название'}),
            "task": Textarea(attrs={'class': 'form-control', 'class': 'list-group-item list-group-item-action list-group-item-info', 'placeholder': 'Введите описание'}),
            "decision": Textarea(attrs={'class': 'form-control','class': 'list-group-item list-group-item-action list-group-item-info', 'placeholder': 'Введите решение'}),
        } 
           
    

