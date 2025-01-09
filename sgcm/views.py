from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from sgcm.forms import CustomUserCreationForm
from sgcm.models import *
from sgcm.forms import *

# Teste
from django.contrib.auth.models import User


def home(request):
    context = {}
    if request.user.is_authenticated:
        username_formatted = request.user.username.replace("_", " ")
        context['username_formatted'] = username_formatted

    specialization_id = request.GET.get("search", "")
    if specialization_id:
        professionals = HealthProfessional.objects.filter(specializations__name__icontains=specialization_id).distinct()
    else:
        professionals = HealthProfessional.objects.all()

    specializations = Specialization.objects.all()
    context['profissionais'] = professionals
    context['specializations'] = specializations
    
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

# @login_required
# def view_register_professional(request):
#     if not request.user.is_staff:
#         return redirect('home')
    
#     specializations = Specialization.objects.all()
    
#     if request.method == "POST":
#         crm = request.POST.get('crm')
#         medical_id = request.FILES.get('medical_id')  
#         full_name = request.POST.get('full_name')
#         cep = request.POST.get('cep')
#         address = request.POST.get('address')
#         neighborhood = request.POST.get('neighborhood')
#         number = request.POST.get('number')
#         rg = request.POST.get('rg')
#         profile_pic = request.FILES.get('profile_pic')  

#         health_professional = HealthProfessional.objects.create(
#             crm=crm,
#             medical_id=medical_id,
#             full_name=full_name,
#             cep=cep,
#             address=address,
#             neighborhood=neighborhood,
#             number=number,
#             rg=rg,
#             profile_pic=profile_pic
#         )

#         selected_specializations = request.POST.getlist('specializations')
#         print(f"Especializações selecionadas: {selected_specializations}")  
#         if selected_specializations:
#             health_professional.Specializations.set(selected_specializations)

#         return redirect('register_professionals')
    
#     return render(request, 'sgcm/pages/register_professionals.html', {'specializations': specializations})

@login_required
def view_register_professional(request):
    if not request.user.is_staff:  # Apenas administradores podem cadastrar médicos
        return redirect('home')

    if request.method == "POST":
        # Obtendo os campos do formulário
        user_email = request.POST.get('user_email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        crm = request.POST.get('crm')
        full_name = request.POST.get('full_name')

        # Validando se as senhas coincidem
        if password != confirm_password:
            # Renderiza a página com uma mensagem de erro
            return render(request, 'sgcm/pages/register_professionals.html', {
                'error': 'As senhas não coincidem. Tente novamente.',
                'specializations': Specialization.objects.all(),  # Passa as especializações se necessário
            })

        # Criando o usuário
        try:
            user = User.objects.create_user(
                username=user_email,
                email=user_email,
                password=password,
            )

            # Criando o médico (HealthProfessional)
            HealthProfessional.objects.create(
                user=user,
                crm=crm,
                full_name=full_name,
                # Preencha os outros campos que você tem no formulário
            )

            # Redireciona para a lista de médicos ou uma página de sucesso
            return redirect('list_professionals')  # Altere conforme necessário

        except Exception as e:
            # Renderiza a página com um erro genérico
            return render(request, 'sgcm/pages/register_professionals.html', {
                'error': f'Ocorreu um erro: {str(e)}',
                'specializations': Specialization.objects.all(),
            })

    return render(request, 'sgcm/pages/register_professionals.html', {
        'specializations': Specialization.objects.all(),  # Passa as especializações se necessário
    })