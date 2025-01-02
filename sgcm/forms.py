from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
