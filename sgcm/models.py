from django.db import models
from django.contrib.auth.models import AbstractUser

# Teste
from django.contrib.auth.models import User
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='specialization/icons/', blank=True, null=False)

    def __str__(self):
        return self.name
    
# class HealthProfessional(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     crm = models.CharField(max_length=20, default='Sem CRM')
#     medical_id = models.FileField(upload_to='medical_ids/',  null=True, blank=True)
#     full_name = models.CharField(max_length=100, null=True, blank=False)
#     cep = models.CharField(max_length=10, null=True)
#     address = models.CharField(max_length=255, default='Sem endereço')
#     neighborhood = models.CharField(max_length=100, null=True, blank=False)
#     number = models.CharField(max_length=15, null=True, blank=False)
#     rg = models.CharField(max_length=20, null=True, blank=False)
#     profile_pic = models.ImageField(upload_to='profile_pics/',  null=True, blank=True)
#     Specializations = models.ManyToManyField(Specialization)

#     def __str__(self):
#         return self.full_name if self.full_name else 'Nome não disponível'

class HealthProfessional(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    crm = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=255, default="Nome não especificado")
    medical_id = models.FileField(upload_to='medical_ids/',  null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  
    cep = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, default='Sem endereço')
    neighborhood = models.CharField(max_length=100, null=True, blank=False)
    number = models.CharField(max_length=15, null=True, blank=False)
    rg = models.CharField(max_length=20, null=True, blank=False)
    Specializations = models.ManyToManyField('Specialization')  

    def __str__(self):
        return self.full_name or "Nome não especificado"