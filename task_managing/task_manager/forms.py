from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task

class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2")


class UpdateUser(forms.ModelForm):
    password=None
    class Meta:
        model=User
        fields=("username", "email")
        exclude = ['password1','password2']


class CreateTask(ModelForm):
    class Meta:
        model=Task
        fields=['title','content',]
        exclude=['user',]

