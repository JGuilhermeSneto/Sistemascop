from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Autenticacao(request):
    if request.POST:
        Usuario = request.POST['Usuario']
        senha = request.POST['Senha']
        user = authenticate(request, username=Usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('Perfil') 
        else:
            return render(request,'login.html')
    else:    
        return render(request,'login.html')


@login_required
def Perfil(request):
    return render(request,'perfil.html')


def Desconectar(request):
    logout(request)
    return redirect('index.html')