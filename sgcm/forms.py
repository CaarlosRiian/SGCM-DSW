from django.contrib.auth.forms import UserCreationForm
from django import forms
from sgcm import models

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.replace(" ", "_")

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = models.HealthProfessional
        fields = [
            'crm', 
            'medical_id', 
            'full_name', 
            'cep', 
            'address', 
            'neighborhood', 
            'number', 
            'rg', 
            'profile_pic'
        ]