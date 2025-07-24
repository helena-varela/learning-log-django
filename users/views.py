from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def login_view(request):
    """Login utilizando um username e uma senha"""
    if request.method == 'POST':
        username = request.POST['username']    
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('logado com sucesso')
            return redirect('index')
        else:
            print("credenciais invalidas")

    return render(request, 'users/login.html')

def logout_view(request):
    """Logout"""
    logout(request)
    return render(request, 'users/login.html')

def register_view(request):
    """Cadastrando um usuário no sistema"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect(reverse('login'))

    return render(request,'users/register.html')