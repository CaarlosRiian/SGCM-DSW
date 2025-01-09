from django.urls import path
from sgcm import views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar-profissional/', views.view_register_professional, name='register_professionals'),
]