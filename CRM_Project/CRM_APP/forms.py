from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record

class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class adduserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']