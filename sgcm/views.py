from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from sgcm.forms import CustomUserCreationForm
from sgcm.models import HealthProfessional

def home(request):
    context = {}
    if request.user.is_authenticated:
        username_formatted = request.user.username.replace("_", " ")
        context['username_formatted'] = username_formatted

    query = request.GET.get("search", "")
    if query:
        professionals = HealthProfessional.objects.filter(specializations_name_icontains=query)
    else:
        professionals = HealthProfessional.objects.all()

    context['profissionais'] = professionals
    context['query'] = query
    
    return render(request, 'sgcm/pages/home.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.replace(" ", "_")
            user.save()
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