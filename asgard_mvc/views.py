from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .forms import *

# Create your views here.
@login_required
def index(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'dashboard.html', context=context)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            response = redirect('login')
            return response
        else:
            pass
    else:
        form = UserRegistrationForm

    context = {'form': form}
    return render(request, 'registration/register.html', context=context)

@csrf_exempt
def login_view(request):
    message = ''

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = redirect('/')
                return response
            else:
                message = 'Username dan Password Tidak Cocok'
        else:
            pass
    else:
        form = UserLoginForm()

    context = {'form': form, 'message': message}
    return render(request, 'registration/login.html', context=context)