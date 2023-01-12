from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from .forms import LoginForm

def loginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    return render(request,'login.html',context)