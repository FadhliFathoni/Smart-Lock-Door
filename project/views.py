from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def loginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        akun = authenticate(username = uname, password = pwd)
        if akun is not None:
            login(request, akun)
            return redirect('/')
    return render(request,'login.html',context)

def landingPage(request):
    return render(request, 'kosong.html')

def logoutView(request):
    logout(request)
    return redirect('/login/')