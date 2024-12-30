from django.urls import path
from sgcm import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.register, name='register'),
]
