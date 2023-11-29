from django.forms import ModelForm, EmailField, BooleanField, RadioSelect, EmailInput, CharField, TextInput
from .models import JustUser
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input input-area'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-input input-area'}))
    password1 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input input-area'}))
    password2 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input input-area'}))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input input-area'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input input-area'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
