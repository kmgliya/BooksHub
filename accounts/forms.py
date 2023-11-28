from django.forms import ModelForm, EmailField, BooleanField, RadioSelect, EmailInput, CharField, TextInput
from .models import JustUser
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class JustUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input input-area'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input input-area'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
