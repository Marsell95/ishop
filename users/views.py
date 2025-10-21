from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from typing import Any

from traitlets import Instance

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):  
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user := auth.authenticate(username=username, password=password):
                auth.login(request, user)
                messages.success(request, f'{username}, You enter in account')
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context: dict[str, Any] = {
        'title': 'Home - Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, You have successfully registered and logged in')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context: dict[str, str] = {
        'title': 'Home - Реєстрація',  
        'form': form,
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):   
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was successfully updated')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context: dict[str, str] = {
        'title': 'Home - Кабінет',
        'form': form        
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, You logout')
    auth.logout(request)
    return redirect(reverse('main:index'))