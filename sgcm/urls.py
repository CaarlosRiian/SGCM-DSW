from django.urls import path, include
from sgcm import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  
]