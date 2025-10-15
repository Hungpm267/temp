from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
   
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # create new user form form
            login(request, user) # tu dong signin cho user sau khi signup
            return redirect('profile')
    else:
        form = UserCreationForm() # tao form dang ki trong
    return render(request, 'user/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST) #khi user an nut login
        if form.is_valid():
            user = form.get_user() # lay username va password tu form
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm() # tao form dangnhap trong
    
    return render(request, 'user/login.html', {'form' : form})
        
@login_required(login_url='login')
def profile_view(request):
    return render(request, 'user/profile.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


