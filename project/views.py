from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from .forms import LoginForm

def loginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    uname = request.POST['username']
    pwd = request.POST['password']
    akun = authenticate(user = uname, password = pwd)
    if akun is not None:
        login(request, akun)
    return render(request,'login.html',context)