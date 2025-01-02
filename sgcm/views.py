from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from sgcm.forms import CustomUserCreationForm

def home(request):
    return render(request, 'sgcm/pages/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
              
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "(Usuario) Email ou senha inválidas")
    return render(request, 'registration/login.html')
        
def logout_view(request):
    logout(request)
    return redirect('login')