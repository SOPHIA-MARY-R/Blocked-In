from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.conf import settings
from authentication.forms import UserRegisterForm
from datetime import date
# Create your views here.
def welcome(request):
    return render(request, 'authentication/welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form, 'title':'reqister here'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
    form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form':form, 'title':'log in'})

def home(request):
    return render(request, 'block/home.html')
