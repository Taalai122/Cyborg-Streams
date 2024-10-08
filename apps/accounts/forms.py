from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(label ='username', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Username'}))

    email = forms.EmailField(label ='email',widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Email'}))
    # Подключи label к паролю
    password1 = forms.CharField(label ='password1',widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password',
               }))

    password2 = forms.CharField(label ='password2',widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Password2'}))
    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'Username'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
        'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
        'placeholder': 'Password'}))