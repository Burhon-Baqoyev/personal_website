from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput,ModelForm,Textarea
from .models import Blog

class CustomLoginForm(AuthenticationForm):

    class Meta:
        model = User
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
            'password':TextInput(attrs={'class':'form-control'}),
        }

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','text','images']
        labels={
            
        }
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'text':Textarea(attrs={'class':'form-control'}),
        }