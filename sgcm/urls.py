from django.urls import path
from sgcm import views

urlpatterns = [
    path('', views.index, name='index'),
]
