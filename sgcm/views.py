from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
def login(request):
    return render(request, 'sgcm/pages/login.html')

def register(request):
    if request.method == 'POST':
        return redirect(reverse_lazy('login'))
    return render(request, 'sgcm/pages/register.html')