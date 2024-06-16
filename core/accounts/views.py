from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['user_name'], cd['email'], cd['password'])
            messages.success(request, f'Account created for {cd["user_name"]}', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def  user_logout(request):
    logout(request)
    messages.success(request, 'You are now logged out', 'success')
    return redirect('home')
