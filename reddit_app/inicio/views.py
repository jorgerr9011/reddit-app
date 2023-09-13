from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib import messages
from django.views.defaults import page_not_found


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try: 
                form.save()
                username = form.cleaned_data['username']
                #Si se completa exitosamente el registro mandamos mensaje de exito
                messages.success(request, f'Usuario {username} creado')
                return redirect('index')
            except:
                return redirect('error')    
    else:
        form = RegistrationForm()
    
    context = {'form' : form}
    return render(request, 'inicio/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def error500(request):
    return render(request, 'inicio/error500.html')


def error400(request, exception):
    return render(request, 'inicio/error400.html')


def error(request):
    return render(request, "inicio/error.html")


#Redireccion a pagina de error cuando introduzan url erronea
def error_404_view(request, exception):
    return render(request, 'inicio/error.html')


def index(request):
    loginError = ""
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            loginError = "Error de login"
    signupForm=RegistrationForm()
    #loginForm=LoginForm()
    if request.user.is_authenticated:
        context={'user':request.user,'signup_form':signupForm,'loginError':loginError}
    else:
        context={'signup_form':signupForm,'loginError':loginError}
	
    return render(request,'inicio/base.html', context)

