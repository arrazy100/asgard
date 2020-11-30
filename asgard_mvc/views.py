from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django import forms

from .forms import *
from .models import *

def get_current_imageprofile(username):
    profile = UserProfileModel.objects.get(username=username)
    image_profile = profile.image_profile.url
    return image_profile

# Create your views here.
@login_required
def index(request):
    username = request.user.username
    image_profile = get_current_imageprofile(username)
    context = {'username': username, 'image_profile': image_profile}
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
            UserProfileModel.objects.create(username=username, image_profile='marmut.jpeg')
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

@login_required
@csrf_exempt
def userprofile_view(request):
    message = ''
    user = UserProfileModel.objects.get(username=request.user.username)
    image = user.image_profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        form.fields['username'].widget = forms.HiddenInput()
        if form.is_valid():
            image_profile = request.FILES['image_profile']
            user.image_profile = image_profile
            user.save()
            message = 'Update Profil Sukses'
            response = redirect('user_profile')
            return response
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
        form.fields['username'].widget = forms.HiddenInput()

    context = {'form': form, 'message': message, 'current_profile': image.url, 'image_profile': image.url}
    return render(request, 'edit_profile.html', context=context)