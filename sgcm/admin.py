from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Specialization)

admin.site.register(HealthProfessional)