from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='specialization/icons/', blank=True, null=False)

    def __str__(self):
        return self.name
    
class HealthProfessional(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Specializations = models.ManyToManyField(Specialization)

    def __str__(self):
        return self.name
