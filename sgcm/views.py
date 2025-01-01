from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def login(request):
    if request.method == "GET":   
        return render(request, 'sgcm/pages/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home') 

def register(request):
    if request.method == "GET":
        return render(request, 'sgcm/pages/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha = request.POST.get('senha')
        confirm_passw = request.POST.get('confirm_passw')

        if senha != confirm_passw:
            return HttpResponse('As senhas não coincidem.')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário Criado com sucesso!')

@login_required
def home(request):
        return render(request, 'sgcm/pages/home.html')