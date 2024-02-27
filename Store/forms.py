from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class customuserform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']